from Page import *  # Pour lier URL, contenu, calcul des mots
from URLWords import *  # Pour gérer le résultat
from db import *  #  Pour sauvegarder les résultats dans la base
from lxml import etree  # Pour générer un XML à partir du résultat

def analysis(lien, largeur, pourcentage):

    reclevel = 1  # indicateur du niveau de récursion; crade, mais pour l'instant on tient ça
    lienparse = urlparse(lien)
    if lienparse.scheme == '':  # ici on pourrait ajouter d'autres tests: vérifier par exemple que celui fourni est un nom de domaine valide
        lien = 'http://' + lien

    # ici tester si la page donne un 200 (r.status_code), else "veuillez tester votre url"

    Page1 = Page(lien, largeur)
    # Page1.stopwords(lien)  # fonction à revoir et à intégrer directement dans Page.wordcount
    Page1.wordcount()  # On récupère les mots dans la page et leur occurrence. Dans la fonction définie dans la classe Page.py il faut intégrer le travail sur les stopwords.
    level = []  # liste qui n'aura qu'une seule case occupée, mais cela permet d'uniformiser le traitement pour l'affichage
    res_lev = URLWords(Page1)  # On crée un objet URLWords, il ne contient que l'URL de Page1.

    res_lev.results = Page1.results_level1(5)  # On ajoute les mots plus présents
    level.append(res_lev)  # on met l'objet dans la liste level1
    crawling = []
    crawling.append(level)  # Tous les résultats iront dans une seule variable faite de listes d'éléments URLWords.

    database = db()  # On est arrivé jusque là, on a des résultats à sauvegarder en base de données, donc autant créer notre objet db
    try:  # tout sauvegarde en BDD est mise dans un `try` afin d'éviter que cela puisse bloquer l'exécution du programme
        crawling[reclevel -1 ][0].save1(database)  # URL et mots associés sont sauvegardés dans les tables url et words
    except:
        pass

# ----------------------
# Traitement du niveau 2

    reclevel += 1
    level2_links = []  # ici on mettra tous les liens présents dans toutes les pages du deuxième niveau
    level = []  # On vide la liste
    largeurmoitie = int(largeur/2)
    for link in Page1.links:  # [:largeur] pas besoin de limiter l'itération horizontale ici, car nous avons déjà limité les liens collectés dans Page.links via le paramètre `largeur`
        PageN = Page(link, largeurmoitie)  # de chaque lien on fait un objet Page. On ne prendra que la moitié du paramètre `largeur` afin de ne pas trop grossir la taille du résultat (car pour exploiter tout ce qu'on récolte les pages de niveau 3 devront être largeur*(largeur/2))
        # print("2 Un nouvel objet page")  # debug
        for link in PageN.links:  # test pour éviter de mettre plusieurs fois le même lien dans la liste. On ne veut pas mettre à nouveau le lien de la page source ni plusieurs fois le même lien
            if link != Page1.url and link != PageN.url and link not in level2_links:
                level2_links.append(link)
        PageN.wordcount()  # de chaque page on compte les mots
        res_lev = URLWords(PageN)  # On crée un objet pour chaque page
        res_lev.results = PageN.find_same_words(crawling[0][0], pourcentage)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent `pourcentage`% ou plus, la liste sera vide.
        level.append(res_lev)  # on ajoute le résultat dans la liste
    crawling.append(level)
    try:
        for i in crawling[reclevel -1]:
            i.savefollow(database, reclevel)
    except:
        pass
# ----------------------
# Traitement du niveau 3


    level = []
    for link in level2_links:  # cette fois, troisième itération, on boucle sur les liens trouvés au deuxième niveau.
        PageN = Page(link, 0)  # Nous n'allos pas garder d'informations sur les liens trouvés à ce niveau, donc 0
        # print("3 Encore un objet page")  # on crée un objet pour chaque lien
        PageN.wordcount()  # de chaque page on compte les mots
        res_lev = URLWords(PageN)  # On crée un objet pour chaque page
        res_lev.results = PageN.find_same_words(crawling[0][0], pourcentage)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent `pourcentage`% ou plus, la liste res_lev3 sera vide.
        level.append(res_lev)  # on ajoute le résultat dans le tableau
    crawling.append(level)  # Tous les résultats dans une seule variable. `level1`, `level2` et `level3` sont des listes d'éléments URLWords (la limite max horizontale imposée avec `largeur` et ses ajustements).
    reclevel += 1  # crade, mais pour le moment on tient ça
    try:
        for i in crawling[reclevel -1]:
            i.savefollow(database, reclevel)
    except:
        pass
    return crawling


def show(crawling):
    """
    Fonction pour afficher le résultat d'un crawling.
    Travaille sur une liste dont chaque élément contient une liste d'objets URLWords.
    1. Contrôle le fait que le niveau (créé en fonction du niveau de récursion verticale demandé) a été rempli. Si vide, arrêt.
    2. Si plein, itère sur les objets URLWords présents en faisant appel à leur fonction showcrawling.
    """
    cptniveaux = 0
    while cptniveaux < len(crawling):
        if crawling[cptniveaux]:
            cptinterne = 0
            while cptinterne < len(crawling[cptniveaux]):
                crawling[cptniveaux][cptinterne].showcrawling()
                cptinterne += 1
        else:
            print("Pas de résultats pour le niveau " + str(cptniveaux+1))
        cptniveaux += 1
      # affichage des résultats du crawling


def xprtxml(crawling):
    """
    Fonction pour traduire les résultats gardés dans la liste crawling, en un fichier XML.
    http://lxml.de/tutorial.html
    """
    root = etree.Element("crawling")
    count = 1
    while count < len(crawling):
        level = etree.SubElement(root, "level")
        level.set("iteration", str(count))
        for c in crawling[count-1]:
            page = etree.SubElement(level, "page")
            url = etree.SubElement(page, "url")
            if count == 1:
                page.set("content", "base")
            elif not c.results:
                page.set("content", "empty")
            else:
                page.set("content", "present")
                results = etree.SubElement(page, "results")
                for r in c.results:
                    word = etree.SubElement("word")
                    for w in r:
                        item = etree.SubElement("item")
                        item.text = w[2]
                        occurrences = etree.SubElement("occurrences")
                        occurrences.text = str(w[0])
                        percentage = etree.SubElement("percentage")
                        percentage.text = str(w[1])
        count += 1
    # now to file print(etree.tostring(root, encoding='UTF-8' pretty_print=True, xml_declaration=True)

from Page import *
from URLWords import *


def analysis(lien, largeur, pourcentage):
    lienparse = urlparse(lien)
    if lienparse.scheme == '':  # ici on pourrait ajouter d'autres tests: vérifier par exemple que celui fourni est un nom de domaine valide
        lien = 'http://' + lien

    # ici tester si la page donne un 200 (r.status_code)

    Page1 = Page(lien, largeur)
    # Page1.stopwords(lien)  # fonction à revoir et à intégrer directement dans Page.wordcount
    Page1.wordcount()  # On récupère les mots dans la page et leur occurrence. Dans la fonction définie dans la classe Page.py il faut intégrer le travail sur les stopwords.
    level1 = []  # liste qui n'aura qu'une seule case occupée, mais cela permet d'uniformiser le traitement pour l'affichage
    res_lev1 = URLWords(Page1)  # On crée un objet URLWords, il ne contient que l'URL de Page1.
    res_lev1.results = Page1.results_level1()  # On ajoute les mots plus récurrents
    level1.append(res_lev1)  # on met l'objet dans la liste level1
    crawling = []
    crawling.append(level1)  # Tous les résultats iront dans une seule variable faite de listes d'éléments URLWords.

# ----------------------
# Traitement du niveau 2

    level2_links = []  # ici on mettra tous les liens présents dans toutes les pages du deuxième niveau
    level2 = []  # contrairement à `level1`, cette variable est une liste. Chaque élément de la liste est un URLWords.
    largeurmoitie = int(largeur/2)
    for link in Page1.links:  # [:largeur] pas besoin de limiter l'itération horizontale ici, car nous avons déjà limité les liens collectés dans Page.links via le paramètre `largeur`
        Page2 = Page(link, largeurmoitie)  # de chaque lien on fait un objet Page. On ne prendra que la moitié du paramètre `largeur` afin de ne pas trop grossir la taille du résultat (car pour exploiter tout ce qu'on récolte les pages de niveau 3 devront être largeur*(largeur/2))
        # print("2 Un nouvel objet page")  # debug
        for link in Page2.links:  # test pour éviter de mettre plusieurs fois le même lien dans la liste. On ne veut pas mettre à nouveau le lien de la page source ni plusieurs fois le même lien
            if link != Page1.url and link != Page2.url and link not in level2_links:
                level2_links.append(link)
        Page2.wordcount()  # de chaque page on compte les mots
        res_lev2 = URLWords(Page2)  # On crée un objet pour chaque page
        res_lev2.results = Page2.find_same_words(level1[0], pourcentage)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent `pourcentage`% ou plus, la liste sera vide.
        level2.append(res_lev2)  # on ajoute le résultat dans la liste
    crawling.append(level2)

# ----------------------
# Traitement du niveau 3


    level3 = []  # comme `level2`, cette variable est une liste. Chaque élément de la liste est un URLWords.
    for link in level2_links:  # cette fois, troisième itération, on boucle sur les liens trouvés au deuxième niveau.
        Page3 = Page(link, 0)  # Nous n'allos pas garder d'informations sur les liens trouvés à ce niveau, donc 0
        # print("3 Encore un objet page")  # on crée un objet pour chaque lien
        Page3.wordcount()  # de chaque page on compte les mots
        res_lev3 = URLWords(Page3)  # On crée un objet pour chaque page
        res_lev3.results = Page3.find_same_words(level1, pourcentage)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent `pourcentage`% ou plus, la liste res_lev3 sera vide.
        level3.append(res_lev3)  # on ajoute le résultat dans le tableau
    crawling.append(level3)  # Tous les résultats dans une seule variable. `level1`, `level2` et `level3` sont des listes d'éléments URLWords (la limite max horizontale imposée avec `largeur` et ses ajustements).
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

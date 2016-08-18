from Page import *  # Pour lier URL, contenu, calcul des mots
from URLWords import *  # Pour gérer le résultat
from db import *  #  Pour sauvegarder les résultats dans la base
from lxml import etree  # Pour générer un XML à partir du résultat

def analysis(links_list, top_mots, crawling, width, coherence, recursions):  # pour compter à quelle récursion nous sommes il suffit d'avoir len(links_list)
    if len(links_list) == 1:
        lienparse = urlparse(links_list[0][0])
        if lienparse.scheme == '':  # ici on pourrait ajouter d'autres tests: vérifier par exemple que celui fourni est un nom de domaine valide
            links_list[0][0] = 'http://' + links_list[0][0]

        # ici tester si la page donne un 200 (r.status_code), else "veuillez tester votre url"

        Page1 = Page(links_list[0][0], width)

        Page1.wordcount()  # On récupère les mots dans la page et leur occurrence. Dans la fonction définie dans la classe Page.py il faut intégrer le travail sur les stopwords.

        res_lev = URLWords(Page1)  # On crée un objet URLWords, il ne contient que l'URL de Page1.

        res_lev.results = Page1.results_level1(top_mots)  # On ajoute les mots plus présents
        crawling = []
        crawling.append(res_lev)  # Tous les résultats iront dans une seule variable faite de listes d'éléments URLWords.

        database = db()  # On est arrivé jusque là, on a des résultats à sauvegarder en base de données, donc autant créer notre objet db
        try:  # tout sauvegarde en BDD est mise dans un `try` afin d'éviter que cela puisse bloquer l'exécution du programme
            crawling[len(links_list) -1 ][0].save1(database)  # URL et mots associés sont sauvegardés dans les tables url et words
        except:
            pass
        links_list.append(Page1.links)
        analysis(links_list, top_mots, crawling, width, coherence, recursions)
    else:
        results_level = []  # On vide la liste
        links_level = []
        for link in links_level[len(links_level) - 1]:  # pas besoin de limiter l'itération horizontale ici, car nous avons déjà limité les liens collectés dans Page.links via le paramètre `width`
            if len(links_list) == recursions:
                PageN = Page(link, 0)  # quand on est au dernier niveau de la récursion on ne va pas chercher les liens contenus dans les pages
            else:
                PageN = Page(link, width)  # de chaque lien on fait un objet Page.
            for lk in PageN.links:  # test pour éviter de mettre plusieurs fois le même lien dans la liste. On ne veut pas mettre à nouveau le lien de la page source ni plusieurs fois le même lien
                if lk not in links_list and lk not in links_level:  # test à améliorer: www.example.com et example.com seront pris tous les deux.
                    links_level.append(link)
            PageN.wordcount()  # de chaque page on compte les mots
            res_lev = URLWords(PageN)  # On crée un objet pour chaque page
            res_lev.results = PageN.find_same_words(crawling[0][0], coherence)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent `coherence`% ou plus, la liste sera vide.
            level.append(res_lev)  # on ajoute le résultat dans la liste
        crawling.append(level)
        try:
            for i in crawling[len(links_list) -1]:
                i.savefollow(database, len(links_list))
        except:
            pass
    if len(links_list) < recursions:
        analysis(links_list, top_mots, crawling, width, coherence, recursions)
    return crawling


def xprtxml(crawling):
    """
    Fonction pour traduire les résultats gardés dans la liste crawling, en un fichier XML.
    """
    root = etree.Element("crawling")
    count = 1
    while count < len(crawling):
        level = etree.SubElement(root, "level")
        level.set("iteration", str(count))
        for c in crawling[count-1]:
            page = etree.SubElement(level, "page")
            url = etree.SubElement(page, "url")
            url.text = c.address
            if count == 1:
                page.set("content", "base")
            elif not c.results:
                page.set("content", "empty")
            else:
                page.set("content", "present")
                results = etree.SubElement(page, "results")
                for r in c.results:
                    word = etree.SubElement(results, "word")
                    item = etree.SubElement(word, "item")
                    item.text = r[2]
                    occurrences = etree.SubElement(word, "occurrences")
                    occurrences.text = str(r[0])
                    percentage = etree.SubElement(word, "percentage")
                    percentage.text = str(r[1])
        count += 1
    filename = "crawling-results.xml"
    file = open(filename, 'wb')
    file.write(etree.tostring(root, encoding='UTF-8', pretty_print=True, xml_declaration=True))

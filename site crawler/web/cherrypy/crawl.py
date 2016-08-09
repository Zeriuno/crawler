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
    level1 = URLWords(Page1)  # On crée un objet URLWords, il ne continet que l'URL de Page1.
    level1.results = Page1.results_level1()


    # print("RESULTATS DU CRAWLING")
    # print("\n")
    # # VERIF print(level1.results)
    # print("     Résultats du crawling de la page 1 ")
    # print("Liens de la page 1", ", ".join(Page1.links))
    # print("Mot : ", level1.results[0][2], ", nombre d'occurences du mot : ", level1.results[0][0],
    #       ",pourcentage de présence du mot : ", level1.results[0][1], "%")
    # print("Mot : ", level1.results[1][2], ", nombre d'occurences du mot : ", level1.results[1][0],
    #       ",pourcentage de présence du mot : ", level1.results[1][1], "%")
    # print("Mot : ", level1.results[2][2], ", nombre d'occurences du mot : ", level1.results[2][0],
    #       ",pourcentage de présence du mot : ", level1.results[2][1], "%")

    # level1.results = Page1.results_level1()  # La fonction renvoie les trois premiers résultats, et ils sont passés dans la liste results

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
        res_lev2.results = Page2.find_same_words(level1, pourcentage)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent X% ou plus, la liste sera vide.
        level2.append(res_lev2)  # on ajoute le résultat dans la liste
        level3 = []  # comme `level2`, cette variable est une liste. Chaque élément de la liste est un URLWords.
    for link in level2_links:  # cette fois, troisième itération, on boucle sur les liens trouvés au deuxième niveau.
        Page3 = Page(link, 0)  # Nous n'allos pas garder d'informations sur les liens trouvés à ce niveau, donc 0
        # print("3 Encore un objet page")  # on crée un objet pour chaque lien
        Page3.wordcount()  # de chaque page on compte les mots
        res_lev3 = URLWords(Page3)  # On crée un objet pour chaque page
        res_lev3.results = Page3.find_same_words(level1, pourcentage)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent X% ou plus, la liste res_lev3 sera vide.
        level3.append(res_lev3)  # on ajoute le résultat dans le tableau

    crawling = [level1, level2, level3]  # Tous les résultats dans une seule variable. `level1` est un URLWords, `level2` et `level3` sont des listes d'éléments URLWords (la limite max horizontale imposée avec `largeur` et ses ajustements).
    # show_results(crawling)  # on pourrait appeller la fonction qui fait l'affichage des résultats
    print("     Résultats du crawling de la page 2 ")
    if res_lev2.results:
        print("Liens de la page 2 ", ", ".join(Page2.links))
    else:
        print("Pas de liens pour la page 2")  # on affiche pas les listes vides

    # verif print(res_lev2.results)
    print("Mot : ", res_lev2.results[0][2], ", nombre d'occurences du mot : ", res_lev2.results[0][0],
          ",pourcentage de présence du mot : ", res_lev2.results[0][1], "%")
    print("Mot : ", res_lev2.results[1][2], ", nombre d'occurences du mot : ", res_lev2.results[1][0],
          ",pourcentage de présence du mot : ", res_lev2.results[1][1], "%")
    print("Mot : ", res_lev2.results[2][2], ", nombre d'occurences du mot : ", res_lev2.results[2][0],
          ",pourcentage de présence du mot : ", res_lev2.results[2][1], "%")

    print("\n")

    print("     Résultats du crawling de la page 3 ")

    if res_lev3.results:
        print("Liens de la page 3", ", ".join(Page3.links))
    else:
        print("Pas de liens pour la page 3")  # on affiche pas les listes vides

    # verif print(res_lev3.results)
    print("Mot : ", res_lev3.results[0][2], ", nombre d'occurences du mot : ", res_lev3.results[0][0],
          ",pourcentage de présence du mot : ", res_lev3.results[0][1], "%")
    print("Mot : ", res_lev3.results[1][2], ", nombre d'occurences du mot : ", res_lev3.results[1][0],
          ",pourcentage de présence du mot : ", res_lev3.results[1][1], "%")
    print("Mot : ", res_lev3.results[2][2], ", nombre d'occurences du mot : ", res_lev3.results[2][0],
          ",pourcentage de présence du mot : ", res_lev3.results[2][1], "%")

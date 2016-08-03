# from urllib.parse import urlparse
# import requests
# from bs4 import BeautifulSoup
# from Page import *
# from URLWords import *
# from stopwords import *
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# lien = "http://news.ycombinator.com"
# lienparse = urlparse(lien)
# if lienparse.scheme == '':
#     lien = 'http://' + lien
#
# # ici tester si la page donne un 200 (r.status_code)
#
# Page1 = Page(lien)  # cette opération nous donne Page1.url, avec l'adresse; Page1.soup avec l'objet BeautifulSoup; Page1.links avec tous les liens.
# Page1.stopwords(lien)
# Page1.wordcount()  # On récupère les mots dans la page et leur occurrence. Dans la fonction définie dans la classe Page.py il faut intégrer le travail sur les stopwords.
#
# level1 = URLWords(Page1)  # On crée un objet URLWords, il ne continet que l'URL de Page1.
# words_level1 = [Page1.wordset[0], Page1.wordset[1], Page1.wordset[2]]
# level1.results = words_level1
# print("RESULTATS DU CRAWLING")
# print("\n")
# #VERIF print(level1.results)
# print("     Résultats du crawling de la page 1 ")
# print("Liens de la page 1", ", ".join(Page1.links))
# print("Mot : ", level1.results[0][2], ", nombre d'occurences du mot : ", level1.results[0][0], ",pourcentage de présence du mot : ", level1.results[0][1],"%")
# print("Mot : ", level1.results[1][2], ", nombre d'occurences du mot : ", level1.results[1][0], ",pourcentage de présence du mot : ", level1.results[1][1],"%")
# print("Mot : ", level1.results[2][2], ", nombre d'occurences du mot : ", level1.results[2][0], ",pourcentage de présence du mot : ", level1.results[2][1],"%")
#
# # level1.results = Page1.results_level1()  # La fonction renvoie les trois premiers résultats, et ils sont passés dans la liste results
#
# level2_links = []  # ici on mettra tous les liens présents dans toutes les pages
# level2 = []  # contrairement à `level1`, cette variable est une liste. Chaque élément de la liste est un URLWords.
# for index, link in enumerate(Page1.links):  # tous les liens des pages du deuxième niveau sont dans cette liste. On y boucle sur un nombre limité d'éléments.
#     # debug print("Dans la boucle enumerate(Page1.links)")
#     if index == 10:  # limitation horizontale: il n'y aura l'analyse que de dix liens pour niveau
#         print("index == 10")  # debug
#         break
#     Page2 = Page(link)  # de chaque lien on fait un objet Page
#     Page2.stopwords(lien)
#     #print("2 Un nouvel objet page")
#     #print("2 Un nouvel objet page")  # debug
#     for link in Page2.links:  # test pour éviter de mettre plusieurs fois le même lien dans la liste. On ne veut pas mettre à nouveau le lien de la page source ni plusieurs fois le même lien
#         if link != Page1.url and link not in level2_links:
#             level2_links.append(link)
#         Page2.wordcount()  # de chaque page on compte les mots
#         res_lev2 = URLWords(Page2)  # On crée un objet pour chaque page
#         res_lev2.results = Page2.find_same_words(level1)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent 2% ou plus, la liste sera vide.
#         level2.append(res_lev2)  # on ajoute le résultat dans le tableau
#         level3 = []  # comme `level2`, cette variable est une liste. Chaque élément de la liste est un URLWords.
#         for index, link in enumerate(level2_links):  # cette fois, troisième itération, on boucle sur les liens trouvés au deuxième niveau.
#             if index == 10:
#                 break
#             Page3 = Page(link)
#             #print("3 Encore un objet page")
#             # on crée un objet pour chaque lien
#             Page3.wordcount()  # de chaque page on compte les mots
#         res_lev3 = URLWords(Page3)  # On crée un objet pour chaque page
#         res_lev3.results = Page3.find_same_words(level1)  # On garde trace des résultats. S'il n'y a pas de mots qui reviennent 2% ou plus, la liste sera vide.
#         level3.append(res_lev3)  # on ajoute le résultat dans le tableau
#
#         crawling = [level1, level2, level3]  # Tous les résultats dans une seule variable. `level1` est un URLWords, `level2` et `level3` sont des tableaux de 10 éléments de URLWords chacun (la limite horizontale imposée avec `index == 10`).
#         # show_results(crawling)  # on pourrait appeller la fonction qui fait l'affichage des résultats
# print("     Résultats du crawling de la page 2 ")
# if res_lev2.results:
#    print("Liens de la page 2 ", ", ".join(Page2.links))
# else:
#     print("Pas de liens pour la page 2") # on affiche pas les listes vides
#
# #verif print(res_lev2.results)
# print("Mot : ", res_lev2.results[0][2], ", nombre d'occurences du mot : ", res_lev2.results[0][0], ",pourcentage de présence du mot : ", res_lev2.results[0][1],"%")
# print("Mot : ", res_lev2.results[1][2], ", nombre d'occurences du mot : ", res_lev2.results[1][0], ",pourcentage de présence du mot : ", res_lev2.results[1][1],"%")
#
# print("\n")
#
# print("     Résultats du crawling de la page 3 ")
#
# if res_lev3.results:
#       print("Liens de la page 3", ", ".join(Page3.links))
# else:
#       print("Pas de liens pour la page 3") # on affiche pas les listes vides
#
# # verif print(res_lev3.results)
# print("Mot : ", res_lev3.results[0][2], ", nombre d'occurences du mot : ", res_lev3.results[0][0], ",pourcentage de présence du mot : ", res_lev3.results[0][1],"%")
# print("Mot : ", res_lev3.results[1][2], ", nombre d'occurences du mot : ", res_lev3.results[1][0], ",pourcentage de présence du mot : ", res_lev3.results[1][1],"%")

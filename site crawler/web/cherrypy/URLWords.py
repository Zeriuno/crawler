

class URLWords(object):
    '''
    Objet pour traiter les résultats des analyses des pages en vue de les afficher.


    Attributs:
        address: l'url de la page analysée
        results: une liste avec mots, leur occurrence, leur pourcentage ([3, 42.86, 'salut'], [2, 28.57, 'bonjour'], [2, 28.57, 'adieu'])
    '''

    def __init__(self, Page: object) -> object:
        '''
        Pour créer un objet URLWords en passant la classe Page.
        Exemple d'utilisation:
        analysePage = URLWords(Page1)
        '''
        self.address = Page.url
        self.results = []


    def showcrawling(self):
        print("Résultats de la page " + self.address)
        if self.results  # test: si la liste est remplie, c'est TRUE, et on a donc des résultats à afficher.
                         # Si la liste est vide, c'est qu'on n'a pas de résultats, donc test donne FALSE
   # for result in crawling:
        #print("1er lien: " + str(level1.Page1.url))
        #print("Mots les plus frequents: " + str(level1.Page1.results))
        #for link in Page2.links:
           # print("lien: " + str(level2.Page2.url))
           # print("Mots les plus frequents: " + str(level2.Page2.results))
        #for link in Page3.links:
           # print("lien: " + str(level3.Page3.url))
           # print("Mots les plus frequents: " + str(level3.Page3.results))


#sauvegarder les resultats

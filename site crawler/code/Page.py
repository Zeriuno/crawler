class Page:
    '''
    Objet pour traiter une page.

    Attributs:
        url : pour garder l'adresse de la page.
        soup: pour traiter la page via BeautifulSoup
        links: liste avec les liens présents dans la page, sans doublons.
    '''

    def __init__(self, url):
        '''
        '''
        self.url = url
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        # Récupère les liens de la page et les place dans un tableau.
        self.links = []
        for link in self.soup.find_all('a'):
            url = link.get('href')
            if(url not in self.links):
                self.links.append(url)

    def wordcount():
        '''
        Fonction qui construit le compte des mots de la page. Elle est appellée avec `NomObjetPage.wordcount()`
        '''
        words = self.soup.get_text() #On récupère le texte
        items = [word.replace('"', '').lower() for word in words.split()] #découpage en mots, imparfait: les mots avec apostrophe restent unis.
        totitems = 0 #un compteur, initialisé à 0
        for word in set(items):
            totitems += items.count(word) #combien d'occurrences, tout mot confondu?
        itemsfreqs = sorted([(items.count(word), (items.count(word)*100)/ totitems, word) for word in set(items)], reverse=True) #dans itemsfreqs on a ainsi une liste d'éléments constitués de nombre d'occurrences, pourcentage et mot, la liste est ordonnée par nombre décroissant d'occurrences.

class Page:
    '''
    Objet pour traiter une page.

    Attributs:
        url : pour garder l'adresse de la page.
        soup: pour traiter la page via BeautifulSoup
        links: liste avec les liens présents dans la page, sans doublons.
        wordlist: lista delle parole con numero occorrenze, percentuale presenza, lemma
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
        text = self.soup.get_text() #On récupère le texte
        items = [text.replace('"', '').lower() for t in text.split()] #découpage en mots, imparfait: les mots avec apostrophe restent unis.
        #avant le reste il faut éliminer les mots communs
        totitems = 0 #un compteur, initialisé à 0
        for word in set(items):
            totitems += items.count(word) #combien d'occurrences, tout mot confondu?
        self.wordlist = sorted([(items.count(word), (items.count(word)*100)/ totitems, word) for word in set(items)], reverse=True) #dans itemsfreqs on a ainsi une liste d'éléments constitués de nombre d'occurrences, pourcentage et mot, la liste est ordonnée par nombre décroissant d'occurrences.

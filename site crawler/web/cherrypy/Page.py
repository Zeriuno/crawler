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
        for link in self.soup.find_all('a'): #il faudra améliorer ça en utilisant urllib.parse et urllib.join
            url = link.get('href')
            if(url not in self.links):
                self.links.append(url)


    def wordcount():
        '''
        Fonction qui construit le compte des mots de la page. Elle est appellée avec `NomObjetPage.wordcount()`

        Exemples
        Page1.wordlist = [(12, 30.00, "salut"),(1, 2.000, "adieu")]

        Comment accéder aux éléments de la liste:

        Page1[0] = (12, 30.00, "salut")
        Page1[1] = (1, 2.000, "adieu")
        Page1[0][0] = 12
        Page1[0][1] = 30.00
        Page1[0][3] = "salut"

        '''
        text = self.soup.get_text() #On récupère le texte
        items = [text.replace('"', '').lower() for t in text.split()] #découpage en mots, imparfait: les mots avec apostrophe restent unis.
        #avant le reste il faut éliminer les mots communs
        totitems = 0 #un compteur, initialisé à 0
        for word in set(items):
            totitems += items.count(word) #combien d'occurrences, tout mot confondu?
        self.wordlist = sorted([(items.count(word), (items.count(word)*100)/ totitems, word) for word in set(items)], reverse=True) #dans wordlist on a ainsi une liste d'éléments constitués de nombre d'occurrences, pourcentage et mot, la liste est ordonnée par nombre décroissant d'occurrences.


    def results_level1():
        '''
        Sélectionne dans self.wordlist les trois mots les plus présents dans la page et leur présence, les mets dans une liste qui est renvoyée.
        '''
        words_level1 = [self.wordlist[0], self.wordlist[1], self.wordlist[2]]
        return words_level1

    def find_same_words(URLWords):
        '''
        La fonction prend un `URLWords` en argument et travaille sur son élément `results`.
        La liste est formatée de cette manière:
        [(12, 30.00, "salut"),(1, 2.000, "adieu"), (1, 2.000, "hellogoodbye")].

        La fonction confronte les mots présents dans self.wordlist avec ceux de la liste passée en argument. Si leur présence est supérieure à X%, les mots de self.worlist sont mis dans une liste (avec occurrences et pourcentage).
        La liste est retournée par la fonction.
        '''

        comparison_list = [] # création de la liste où l'on mettra le résultat de la comparaison.

        for item in self.wordlist:
            for result in URLWords.results:
                if item[2] == result[2]:
                    comparison_list.append(item)

        return comparison_list

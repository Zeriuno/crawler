from urllib.parse import *  # pour parser les url dans les pages et obtenir des adresses absolues au lieu de relatives
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import requests
import re  # pour découper le texte en mots

class Page:
    '''
    Objet pour traiter une page.

    Attributs:
        url : pour garder l'adresse de la page.
        soup: pour traiter la page via BeautifulSoup
        links: liste avec les liens présents dans la page, sans doublons.
        wordset: lista delle parole con numero occorrenze, percentuale presenza, lemma
    '''

    def __init__(self, url):
        '''
        Pour créer un objet Page; nécesaire de passer en paramètre une URL.

        Exemple
        Page1 = Page(url)
        '''
        self.url = url
        homeparse = urlparse(self.url)  # servira pour reconstruire des url absolues
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        # Récupère les liens de la page et les place dans un tableau.
        self.links = []
        self.wordset = []
        index = 0;
        for link in self.soup.find_all('a'): #il faudra améliorer ça en utilisant urllib.parse et urllib.join
<<<<<<< HEAD
            url = link.get('href', index)
            urlanalysis = urlparse(url)
            if urlanalysis.scheme == '' and urlanalysis.netloc == '':
                url = homeparse.scheme + '://' + homeparse.netloc + url
            if urlanalysis.scheme == '':
               lien = 'http://' + url
               print("J'ai pris ce lien :" + url, +index)
            if(url not in self.links):
                self.links.append(url)
                index += 1
=======
            try:
                url = link.get('href')  # debug: print("J'ai vu ce lien: " + url)
                urlanalysis = urlparse(url)
                if url is None or urlanalysis.scheme == 'mailto' or urlanalysis.scheme == 'javascript':
                    url = ''  # debug print("Je tue ce lien: " + url)
                if urlanalysis.scheme == '' and urlanalysis.netloc == '':
                    if url[0] == '/':
                        url = homeparse.scheme + '://' + homeparse.netloc + url
                    else:
                        url = homeparse.scheme + '://' + homeparse.netloc + '/' + url
                if urlanalysis.scheme == '' and urlanalysis.netloc != '':
                    url = 'http://' + url
                if url != '' and url not in self.links:
                    self.links.append(url)  # debug print("J'ai pris ce lien :" + url)
            except TypeError:
                pass

>>>>>>> origin/master

    def stopwords(self, lien):
        '''
        Filtrer les mots
        '''
        #dictionnaire français des mots à exclure
        stop_words = set(stopwords.words("french"))
        words = word_tokenize(lien)
        filtered_phrase = []
        for w in words:
            if w not in stop_words:
                lien = filtered_phrase.append(w)


    def wordcount(self):
        '''
        Fonction qui construit le compte des mots de la page. Elle est appellée avec `NomObjetPage.wordcount()`

        Exemples
        Page1.wordset = [(12, 30.00, "salut"),(1, 2.000, "adieu")]

        Comment accéder aux éléments de la liste:

        Page1[0] = (12, 30.00, "salut")
        Page1[1] = (1, 2.000, "adieu")
        Page1[0][0] = 12
        Page1[0][1] = 30.00
        Page1[0][3] = "salut"
        '''
        text = self.soup.get_text() #On récupère le texte
        items = re.sub("[^\w]", " ",  text).split()
        #  items = [text.replace('"', '').lower() for t in text.split()] #découpage en mots, imparfait: les mots avec apostrophe restent unis. Il faudrait passer par nltk avec la tokenization
        # stopwords(text) #avant le reste il faut éliminer les mots communs
        totitems = len(items)
        self.wordset = sorted([(items.count(word), (items.count(word)*100 / totitems), word) for word in set(items)], reverse=True)  # dans wordset on a ainsi une liste d'éléments constitués de nombre d'occurrences, pourcentage et mot, la liste est ordonnée par nombre décroissant d'occurrences.


    @property
    def results_level1(self):
        """
        Sélectionne dans self.wordset les trois mots les plus présents dans la page et leur présence, les mets dans une liste qui est renvoyée.
        """
        words_level1 = [self.wordset[0], self.wordset[1], self.wordset[2]]
        return words_level1

    def find_same_words(self, URLWords):
        '''
        La fonction prend un `URLWords` en argument et travaille sur son élément `results`.
        La liste est formatée de cette manière:
        [(12, 30.00, "salut"),(1, 2.000, "adieu"), (1, 2.000, "hellogoodbye")].

        La fonction confronte les mots présents dans self.wordset avec ceux de la liste passée en argument. Si leur présence est supérieure à X%, les mots de self.worlist sont mis dans une liste (avec occurrences et pourcentage).
        La liste est retournée par la fonction.
        '''

        comparison_list = [] # création de la liste où l'on mettra le résultat de la comparaison.

        for item in self.wordset:
            for result in URLWords.results:
                if item[2] == result[2] and item[1] >= 2:
                    comparison_list.append(item)

        return comparison_list

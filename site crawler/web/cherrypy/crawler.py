import cherrypy
import pymysql
from jinja2 import Environment, FileSystemLoader

import requests
from bs4 import BeautifulSoup

env = Environment(loader=FileSystemLoader('templates'))

#affichage de la page index.html

class Crawler(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    index.exposed = True

#récupérer le lien soumis
    def prendreURL (self, lien=None):
        if lien:


            #ici nous allons dérouler tout notre programme. Ce sera notre "main"
            #print("Crawling en cours") par exemple.

            #on prend `lien`, la variable qui nous est renvoyée par la page, et on la donne aux fonctions que nous avons définies par ailleurs.

            Page1 = Page(lien) #cette opération nous donne Page1.url, avec l'adresse; Page1.soup avec l'objet BeautifulSoup; Page1.links avec tous les liens.

            Page1.wordcount() #On récupère les mots dans la page et leur occurrence. Dans la fonction définie dans la classe Page.py il faut intégrer le travail sur les stopwords.

            level1 = URLWords(Page1) #On crée un objet URLWords, il ne continet que l'URL de Page1.
            level1.results = Page1.results_level1() #La fonction renvoie les trois premiers résultats, et ils sont passés dans la liste results

            level2_links = [] #ici on mettra tous les liens présents dans toutes les pages
            for index, link in enumerate(Page1.links): #tous les liens du deuxième niveau sont dans cette liste. On y boucle sur un nombre limité d'éléments.
                if index == 10: #limitation horizontale: il n'y aura l'analyse que de dix liens pour niveau
                    break
                Page2 = Page(link) #de chaque lien on fait un objet Page
                for link in Page2.links: #test pour éviter de mettre plusieurs fois le même lien dans la liste. On ne veut pas mettre à nouveau le lien de la page source ni plusieurs fois le même lien
                    if link not in Page1.url and link not in level2_links:
                        level2_links.append(link)
                Page2.wordcount() #de chaque page on compte les mots



            soup = self.grabpage(lien) #la fonction grabpage retourne une `soup`, donc on dit que `soup` prend le résultat de `grabpage` appliqué à la variable lien.
            comptage = self.comptagemots(soup)
        else:
            print("Il est nécessaire de soumettre une URL")
        return ("Crawling en cours")
    prendreURL.exposed = True

#recupérer le texte de la page

    def grabpage(self,lien):
        '''
        Prend l'URL passsée en paramètre et la récupère avec requests.
        On peut l'utiliser de cette manière: soup = grabpage(url)
        '''
        r = requests.get(lien)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup
    grabpage.exposed = True

#comptage des mots
    def comptagemots(self, soup):
        songs = (soup.get_text())
        lsongs = [song.replace('"', '').lower() for song in songs.split()]
        freqs = [(- lsongs.count(song), song) for song in set(lsongs)]
        soup = ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))
        #enrgistrer les 3 1er mots dans un fichier txt
        monFichier = open("resultatscrawling.txt", "w", encoding="utf-8")
        monFichier.write("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)[:3]))
        monFichier.close()
        return soup
    comptagemots.exposed = True

#récupérer les liens de la page




#demarrage du serveur cherrypy
cherrypy.quickstart(Crawler(), config='server.conf')

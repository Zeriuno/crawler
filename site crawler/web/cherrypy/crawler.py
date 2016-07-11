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
            print("Crawling en cours") #par exemple.

            #on prend lien, la variable qui nous est renvoyée par la page, et on la donne aux fonctions que nous avons définies par ailleurs.
            soup = self.grabpage(lien) #la fonction grabpage retourne une `soup`, donc on dit que `soup` prend le résultat de `grabpage` appliqué à la variable lien.
            comptage = self.comptagemots(soup)
        else:
            print("Il est nécessaire de soumettre une URL")
        return lien
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


    def comptagemots(self, soup):
        songs = (soup.get_text())
        lsongs = [song.replace('"', '').lower() for song in songs.split()]
        freqs = [(- lsongs.count(song), song) for song in set(lsongs)]
        soup = ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))
        return soup
    comptagemots.exposed = True

#demarrage du serveur cherrypy
cherrypy.quickstart(Crawler(), config='server.conf')

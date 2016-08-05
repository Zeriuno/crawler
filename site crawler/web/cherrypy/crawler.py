from crawl import analysis
import cherrypy
from jinja2 import Environment, FileSystemLoader

from urllib.parse import urlparse  # pour tester les URL passées par l'utilisateur et pour reconstituer les liens rélatifs

import requests
from bs4 import BeautifulSoup
from Page import *
from URLWords import *
from stopwords import *



env = Environment(loader=FileSystemLoader('templates'))

  # affichage de la page index.html

class Crawler(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    index.exposed = True

# récupérer le lien soumis
    def prendreURL(self, lien=None):
        if lien:
            largeur = 20  # variable pour, dans une évolution, pouvoir varier le niveau de récursion horizontale
            analysis(lien, largeur)  # fonction externalisée dans crawl.py
        else:
            print("Il est nécessaire de soumettre une URL")
        return ("Crawling en cours")
    prendreURL.exposed = True

  # # recupérer le texte de la page
  #
  #   def grabpage(self,lien):
  #       """
  #       Prend l'URL passsée en paramètre et la récupère avec requests.
  #       On peut l'utiliser de cette manière: soup = grabpage(url)
  #       """
  #       r = requests.get(lien)
  #       soup = BeautifulSoup(r.content, "html.parser")
  #       return soup
  #   grabpage.exposed = True
  #
  # # comptage des mots
  #   def comptagemots(self, soup):
  #       songs = (soup.get_text())
  #       lsongs = [song.replace('"', '').lower() for song in songs.split()]
  #       freqs = [(- lsongs.count(song), song) for song in set(lsongs)]
  #       soup = ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))
  #       #enrgistrer les 3 1er mots dans un fichier txt
  #       monFichier = open("resultatscrawling.txt", "w", encoding="utf-8")
  #       monFichier.write("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)[:3]))
  #       monFichier.close()
  #       return soup
  #   comptagemots.exposed = True
  #
  # # récupérer les liens de la page




  # demarrage du serveur cherrypy
cherrypy.quickstart(Crawler(), config='server.conf')

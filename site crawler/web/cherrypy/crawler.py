from crawl import *
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
    def crawlurl(self, lien=None):
        if lien:
            largeur = 20  # variable pour, dans une évolution, laisser déterminer à l'utilisateur le niveau de récursion horizontale
            pourcentage = 1 # variable pour, dans une évolution, laisser déterminer à l'utilisateur le pourcentage de cohérence requis entre la première page et celles associées
            crawling = analysis(lien, largeur, pourcentage)  # fonction externalisée dans crawl.py, elle retourne une liste avec les résultats
            show(crawling)  # affichage des résultats, fonction externalisée dans crawl.py
        else:
            print("Il est nécessaire de soumettre une URL")
        tmpl = env.get_template('results.html')
        return tmpl.render(first = crawling[0][0], follow = crawling[1:len(crawling)])
    crawlurl.exposed = True

cherrypy.quickstart(Crawler(), config='server.conf')

from crawl import *
import cherrypy
from jinja2 import Environment, FileSystemLoader

from urllib.parse import urlparse  # pour tester les URL passées par l'utilisateur et pour reconstituer les liens rélatifs

import requests
from bs4 import BeautifulSoup
from Page import *
from URLWords import *
import os.path  # pour getxml
from cherrypy.lib.static import serve_file  # pour getxml

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
            width = 20  # variable pour, dans une évolution, laisser déterminer à l'utilisateur le niveau de récursion horizontale
            coherence = 1  # variable pour, dans une évolution, laisser déterminer à l'utilisateur le pourcentage de cohérence requis entre la première page et celles associées
            recursions = 3  # variable pour, dans une évolution, laisser déterminer à l'utilisateur combien de niveaux de récursion sont effectués
            top_mots = 5  # variable pour, dans une évolution, laisser déterminer à l'utilisateur combien de mots de la première page sont retenus pour la confrontation avec les pages suivantes.
            links_list = []
            list = []
            list.append(lien)
            links_list.append(list)
            crawling = []
            crawling = analysis(links_list, top_mots, crawling, width, coherence, recursions)  # fonction externalisée dans crawl.py, elle retourne une liste avec les résultats
            xprtxml(crawling)  # le résultat est sauvegardé dans un fichier XML
            summary = sumup(crawling)  # sommaire des pages avec résultats
            empties = sumdown(crawling)  # sommaire des pages sans résultats
        else:
            print("Il est nécessaire de soumettre une URL")
        tmpl = env.get_template('results.html')
        return tmpl.render(first = crawling[0][0], follow = crawling[1:len(crawling)], got = summary, gotnot = empties)
    crawlurl.exposed = True

    def getxml(self):
        filename = "crawling-results.xml"  # le fichier est créé par xprtxml
        filepath = os.path.abspath(filename)
        return serve_file(filepath, "application/x-download", "attachment")
    getxml.exposed = True

cherrypy.quickstart(Crawler(), config='server.conf')

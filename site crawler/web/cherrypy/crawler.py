import cherrypy
import pymysql
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

#affichage de la page index.html

class Crawler(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    index.exposed = True

    def prendreURL (self, lien=None):
        return lien
    prendreURL.exposed = True

#demarrage du serveur cherrypy
cherrypy.quickstart(Crawler(), config='server.conf')

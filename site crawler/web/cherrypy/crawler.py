import cherrypy
import pymysql
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

class Crawler(object):
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    index.exposed = True

cherrypy.quickstart(Crawler(), config='server.conf')

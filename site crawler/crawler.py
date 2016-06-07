import cherrypy
import pymysql
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

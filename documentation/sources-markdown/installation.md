# Installation

## Dépendances

Le programme nécessite de:

* python3.4 ou supérieur
  * jinja2
  * beautifulsoup4
  * CherryPy
  * lxml
  * pysql
  * requests
  * urllib.parse
* mysql serveur ou similaire

## Configuration

### Base de données

Le programme utilise une base de données (non indispensable). Deux scripts pour celle-ci sont donnés:

* `creation-usr.sql`: pour créer la base, l'utilisateur, et lui allouer les droits sur la base
* `creation-bdd.sql`: pour créer les tables de la base de données

Les informations sur la base de données doivent être transcrites dans `web/db.conf` (actuellement pré-rempli avec les données proposées dans les deux scripts).

### Serveur

Dans `web/server.conf` modifier opportunément ce parcours:
```
tools.staticdir.dir.root = "/Users/$username/$path/$to/crawler/web/templates/css"
```

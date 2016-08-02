# Installer BeautifulSoup

## Via `pip`

Dans le terminal: `pip3 install beautifulsoup4` (ça peut être `pip3` ou `pip` selon les machines).

## Via téléchargement

1. site: http://pypi.python.org/pypi/beautifulsoup4
2. télécharger "beautifulsoup4-4.1.3.tar.gz"
3. Sur le terminal
```
python setup.py build 
python setup.py install
```

### Via téléchargement plus rapide

1. `curl -O https://pypi.python.org/packages/26/79/ef9a8bcbec5abc4c618a80737b44b56f1cb393b40238574078c5002b97ce/beautifulsoup4-4.4.1.tar.gz`
2. `tar xvzf beautifulsoup4-4.4.1.tar.gz`
3. `cd beautifulsoup4-4.4.1`
4. `python setup.py build && python setup.py install`


###Installer un parser BS

Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers. One is the lxml parser. Depending on your setup, you might install lxml with one of these commands:

$ apt-get install python-lxml

$ easy_install lxml

$ pip install lxml

Another alternative is the pure-Python html5lib parser, which parses HTML the way a web browser does. Depending on your setup, you might install html5lib with one of these commands:

$ apt-get install python-html5lib

$ easy_install html5lib

$ pip install html5lib


###Entête du fichier.py

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup("<html>data</html>")
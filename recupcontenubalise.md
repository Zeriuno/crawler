Récupérer le contenu d'une balise spécifiée
BeautifulSoup vous propose par exemple de récupérer toutes les balises p d'une page HTML

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """

//
<html>
    <head>
    <title>Titre de votre site</title>
    </head>
    <body>
        <p>Texte à lire 1</p>
        <p>Texte à lire 2</p>
    </body>
</html>

//
"""
soup = BeautifulSoup(html_doc)
    
for p in soup.find_all('p'):
    print p
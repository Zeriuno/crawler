import requests
from bs4 import BeautifulSoup
url =  "http://www.charo-shop.com/fr/"
r = ("http://www.charo-shop.com/fr/")
soup = BeautifulSoup(r.content, "html.parser")

soup.find_all("a") # récupérer tous les liens de la page

for link in links: // récupérer tous les liens de la page
    if "http" in link:
        print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

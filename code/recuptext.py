import requests
from bs4 import BeautifulSoup

r =  requests.get("http://www.charo-shop.com/fr/")
soup = BeautifulSoup(r.content, "html.parser")
soup.get_text
print (soup.prettify())
soup.find_all("a") # récupérer tous les liens de la page
for link in soup.find_all("a"): # récupérer tous les liens de la page
    print ("<a href='%s'>%s</a>" %(link.get("href"), link.text)) #récupérer tous les liens de la page


import requests
from bs4 import BeautifulSoup

#CRAWLING

r =  requests.get("http://www.charo-shop.com/fr/")
soup = BeautifulSoup(r.content, "html.parser")
soup.get_text
print (soup.get_text())
soup.find_all("p") # récupérer tous le texte de la page
for link in soup.find_all("p"): # récupérer tous les liens de la page
     print ("'%s'%s" %(link.get("p"), link.text)) #récupérer tous les liens de la page


#COMPTAGE MOTS

songs = (soup.get_text())
lsongs = [song.replace('"', '').lower() for song in songs.split()]
freqs = [(- lsongs.count(song), song) for song in set(lsongs)]
print ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))


#ECRITURE DES RESULTATS DANS FICHIER

# création et ecriture

monFichier = open("resultatscrawling.txt", "w", encoding="utf-8")
monFichier.write ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))
monFichier.close()


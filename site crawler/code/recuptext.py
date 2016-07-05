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

def  wordcount(self):
    '''
    '''
    text = 
songs = (soup.get_text())
lsongs = [song.replace('"', '').lower() for song in songs.split()]
freqs = [(- lsongs.count(song), song) for song in set(lsongs)]
print ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))


#ECRITURE DES 3 1er RESULTATS DANS LE FICHIER

#Création et ecriture

monFichier = open("resultatscrawling.txt", "w", encoding="utf-8")
monFichier.write ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)[:3]))
monFichier.close()


#RECUPERER LES LIENS DE LA PAGE

for link in soup.find_all("a"):
     print(link.get("href"))



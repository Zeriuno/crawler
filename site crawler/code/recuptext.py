

import requests
from bs4 import BeautifulSoup

#CRAWLING
# On n'a pas besoin de cette fonction: on récupère les liens dans la création de l'objet Page (cf `Page.py`). Par ailleurs on n'irait pas chercher les 'p', mais plutôt les 'a'.

# def recupliens(liens):
#     r = requests.get("http://www.charo-shop.com/fr/")
#     soup = BeautifulSoup(r.content, "html.parser")
#     soup.get_text
#     soup.find_all("p") # récupérer tous le texte de la page
#     for link in soup.find_all("p"): # récupérer tous les liens de la page
#         liens = ("'%s'%s" %(link.get("p"), link.text)) #récupérer tous les liens de la page
#     return liens

#COMPTAGE MOTS

#Fonction reprise dans Page.py, wordcount().

# def comptagemots(compte):
#     songs = (soup.get_text())
#     lsongs = [song.replace('"', '').lower() for song in songs.split()]
#     freqs = [(- lsongs.count(song), song) for song in set(lsongs)]
#     compte = ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)))
#     return compte

#ECRITURE DES 3 1er RESULTATS DANS LE FICHIER

#Création et ecriture

 def ecrituredansfichier():
     monFichier = open("resultatscrawling.txt", "w", encoding="utf-8")
     monFichier.write ("\n".join("%-10s : %s" % (n, -f) for f, n in sorted(freqs)[:3]))
     monFichier.close()


#RECUPERER LES LIENS DE LA PAGE

for link in soup.find_all("a"):
     print(link.get("href"))

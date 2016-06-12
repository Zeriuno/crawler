from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("Contact.html"))

final_link = soup.p.a
final_link.decompose()

f = csv.writer(open("Contact.csv", "w"))
f.writerow(["Nom", "Lien"])    # Write column headers as the first line

liens = soup.find_all('a')
for lien in liens:
    noms = lien.contenu[0]
    liencomplet = lien.get('href')

    f.writerow([noms,liencomplet])
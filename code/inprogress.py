#Traiter l'url donnée avec urllib.parse: https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse

#Il faut récupérer la page demandée

import requests
from bs4 import BeautifulSoup

url = "http://brucespringsteen.net/songs/blood-brothers"

def grabpage(url):
    '''
    Prend l'URL passsée en paramètre et la récupère avec requests.
    On peut l'utiliser de cette manière: soup = grabpage(url)
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    return soup

for link in links:
   print(link)

#en extraire les mots avec BeautifulSoup

Récupérer tout le texte: soup.get_text()

#sauvegarder cela dans un XML
#hypothèse
<page>
  <mots>
    <entree>
        <mot>
        </mot>
        <pourcentage>
        </pourcentage>
    <entree>
  </mots>
  <liens>
    <adresse>
    </adresse>
  </liens>
<page>

#on stocke dans la BDD


#ensuite on boucle. D'abord en horizontal, donc niveau par niveau, plutôt que de descendre en profondeur dans l'arborescence des liens. Non, peut-être mieux en profondeur d'abord. Tout ce qui suit est à revoir

pour adresse in liens[]
    recuppage,
    recupmots,
    BDD
    IDpagestartniveau1
    IDpageendniveau1
    pour IDpagestartniveau1 <= X <= IDpageendniveau1
        pour adresse in liens[]
            recuppage,
            recupmots,
            BDD
            IDpagestartniveau2
            IDpageendniveau2
        finpour
    finpour
finpour

Comment boucler les niveaux successifs? Par le biais de l'ID page: quand on crée

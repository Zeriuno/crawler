#Il faut récupérer la page demandée
recuppage
wget $cible ou, mieux, cf la vidéo proposée par MBA
#Il faut en extraire les liens, attention aux chemins relatifs
recupliens
from bs4 import BeautifulSoup
import csv

#en extraire les mots avec BeautifulSoup
recupmots
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

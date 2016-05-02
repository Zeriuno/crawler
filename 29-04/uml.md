#UML

## Classes

* Pages
* Mots
* Resultats

## Définitions

On assimile, pour commodité une URL à une page.

Résultat est le résultat synthétique produit par l'analyse d'une page et affiché à l'utilisateur.

## Schéma

page 0, * ---traite--- 0, * ---> thème [cela doit être la flèche d'association forte]

page 0, * ---renvoie vers--- 0, * ---> page [association faible]

page 1, * ---produit --- 1, 1 ---> Résultat

Résultat 1, * --- inclut --- 0, * ---> thème [association forte]

## Processus

* Chercher les mots clefs dans la page
* Stocker le résultat
* Afficher les résultats

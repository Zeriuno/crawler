#UML

## Classes

* Pages
* Mots
* Resultats

## Définitions

On assimile, pour commodité une URL à une page.

Résultat est le résultat synthétique produit par l'analyse d'une page et affiché à l'utilisateur.

## Schéma

page 0, * ---contient--- 0, * ---> mots [cela doit être la flèche d'association forte]

page 0, * ---renvoie vers--- 0, * ---> page

page 1, * ---produit --- 1, 1 ---> Résultat

## Processus

* Afficher les résultats
* Chercher les mots clefs dans la page
* Chercher les mêmes mots clefs dans les pages associées

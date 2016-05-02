# Crawler thématique

Objet principal: le projet est consiste en la réalisation d'une application web.
Celle-ci demande à l'utilisateur de fournir une URL. Une fois lancée, l'application analyse la page associée à l'URL et elle en identifie les mots clefs.
L'application itère l'opération de manière récursive sur les pages dont l'URL est contenue dans la page analysée et effectue ainsi plusieurs niveaux d'analyse.
L'application présente enfin les résultats obtenus à l'utilisateur: les pages des niveaux ultérieurs d'analyse ne sont incluses parmi les résultats que s'ils présentent une continuité thématique suffisante avec la première page (le niveau sera déterminé en cours de développement par le biais de tests).

### Objectifs

L'objectif principal est de proposer à l'utilisateur une web application permettant de déterminer les mots clefs d'une page web donnée par l'utilisateur et la continuité de présence de ces mots dans les pages associées.

L'application sera à la fois mise en ligne et son code source envoyé au client.

#### Problèmes

Il est également nécessaire de prendre en compte le problème que poserait au bon fonctionnement de l'application une grand nombre de liens présents dans une page et prévoir des modalités adaptées pour y pallier.

Pour ce qui est des résultats, seront à prendre en considération également plusieurs facteurs qui risquent d'en reduire la validité. Tels que la présence d'images et de vidéos, que l'application ne saurait pas prendre en compte, ainsi que des textes courts, ou bien à longueur inégale, où l'on toucherait aux limites de l'analyse textuelle avec une simple statistique gaussienne.


#### Objectifs complémentaires

Les objectifs complémentaires, classés par ordre de priorité decroissante sont :

* documentation client
* documentation utilisateur
* design
* mobile (facultatif)
* export des résultats (facultatif)

### Limites

Les parties suivantes de l'application ne seront pas développées dans le cadre du projet, qui réutilisera des éléments déjà existants :

* serveur web
* bibliothèque de crawling
* base de données et interaction avec celle-ci

L'application livrée ne sera pas :

* disponible hors-ligne
* évaluée pour la montée en charge
* conçue pour de la haute disponibilité
* garantie compatible avec IE

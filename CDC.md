# Crawler thématique

CRA1.a - Le système doit permettre à l'utilisateur de saisir une URL.
CRA2.a - Le système doit consulter la page présente à l'URL donnée et y identifier les mots les plus fréquents.
CRA3.a - Le système doit identifier les URL présentes à l'intérieur de la page fournie présente à l'URL fournie.
CRA4.a - Le système doit itérer la recherche du point CRA2.a sur les URL du point CRA3.a.
CRA5.a - Le système doit itérer la recherche du point CRA3.a sur les URL du point CRA3.a.
CRA5.b - Le système doit limiter la récursion du point CRA4.a à trois niveaux: URL fournie par l'utilisateur + deux niveaux de recherche.
CRA5.c - Le système doit limiter la recherche du point CRA4.a à n éléments (à déterminer via des tests).
CRA5.d - Le système doit permettre à l'utilisateur de désactiver les limitations des points CRA5.b et CRA5.c.


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

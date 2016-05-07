# Crawler thématique


Numéro de l’exigence : CRA1.a
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit permettre à l'utilisateur de saisir une URL.
Justification : rendre la recherche possible sur la page souhaitée par le client
Origine : Julien Roussel
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes : 
Exigences conflictuelles :
Documents relatifs : 
Historique :


Numéro de l’exigence : CRA2.a
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit consulter la page présente à l'URL donnée et y identifier les mots les plus fréquents.
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :


Numéro de l’exigence : CRA3.a
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit identifier les URL présentes à l'intérieur de la page fournie présente à l'URL fournie.
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :



Numéro de l’exigence : CRA4.a
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit itérer la recherche du point CRA2.a sur les URL du point CRA3.a.
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :


Numéro de l’exigence : CRA5.a
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit itérer la recherche du point CRA3.a sur les URL du point CRA3.a.
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :


Numéro de l’exigence : CRA5.b
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit limiter la récursion du point CRA4.a à trois niveaux: URL fournie par l'utilisateur + deux niveaux de recherche.
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :


Numéro de l’exigence : CRA5.c
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit limiter la recherche du point CRA4.a à n éléments (à déterminer via des tests).
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :


Numéro de l’exigence : CRA5.d
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit permettre à l'utilisateur de désactiver les limitations des points CRA5.b et CRA5.c.
Justification :
Origine :
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :

Numéro de l’exigence : CRA5.e
Type d’exigence :
Evénements / Cas d’utilisation :
Description : Le système doit permettre à l'utilisateur de visualiser les résulats de l'analyse de l'URL fournie et de ses pages associées.
Justification :
Origine : Julien Roussel
Critère de satisfaction :
Contentement du maître d’ouvrage:
Mécontentement du maître d’ouvrage:
Exigences dépendantes :
Exigences conflictuelles :
Documents relatifs :
Historique :

Nb : les pages des niveaux ultérieurs d'analyse ne sont incluses parmi les résultats que s'ils présentent une continuité thématique suffisante avec la première page (le niveau sera déterminé en cours de développement par le biais de tests).

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
* export des résultats, fichier format JSON ou XML(facultatif)

## Aspects techniques

Le programme est une application web et est compatible tous les navigateurs, seule la compatibilité avec Internet Explorer ne sera pas testée. Cette application est conçue pour offrir une disponibilité continue 24h/7j.

### Stockage des données

* Stockage des données en cache web (utilisation de cookies). 
* Stockage en base de données (utilisation des tables temporaires qui pourront soit rester en base soit devenir des fichier de logs)
* Vérification de l'adhérence entre la base de données et le cache





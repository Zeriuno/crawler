# Crawler thématique

## Parties prenantes

* Client : Julien ROUSSEL
* Membres de l'équipe projet (Gestion de projet, MOA, MOE, DEV) : Meriyama BANE, Salah DAHAMNI, Daniele PITROLO
* Validation de la gestion du projet: Georges GROSZ, Stéphane LAMASSÉ

##Identification du projet

Nom du projet : Crawler thématique

Nature du projet : nouvelle application

## Contexte de la demande

Date de la demande : 26 mars 2016
Motivation du besoin : évaluation, cours de Python, Master 2 MIMO

Objet principal: le projet est consiste en la réalisation d'une application web.
Celle-ci demande à l'utilisateur de fournir une URL. Une fois lancée, l'application analyse la page associée à l'URL et elle en identifie les mots clefs.
L'application itère l'opération de manière récursive sur les pages dont l'URL est contenue dans la page analysée et effectue ainsi plusieurs niveaux d'analyse.
L'application présente enfin les résultats obtenus à l'utilisateur: les pages des niveaux ultérieurs d'analyse ne sont incluses parmi les résultats que s'ils présentent une continuité thématique suffisante avec la première page (le niveau sera déterminé en cours de développement par le biais de tests).

### Objectifs

L'objectif principal est de proposer à l'utilisateur une page web permettant de déterminer les thèmes évoqués dans une page web donnée et la continuité thématique au travers des liens présentés.

* documentation client
* documentation utilisateur
* design
* mobile (facultatif)


### Limites

Les parties suivantes de l'application ne seront pas développées dans le cadre du projet, qui réutilisera des éléments déjà existants :

* serveur web
* bibliothèque de crawling
* base de données et interaction avec celle-ci

L'application livrée ne sera pas :

* disponible hors-ligne
* soumise à des tests de charge
* haute disponibilité non requise

## Phasage

Le projet est décomposé sur les 4 jalons suivants:


######################################################################################
				Remarques
Pas d'accord: je suis pour un échelonnement différent. Première étape la rédaction du cahier des charges, du cahier de recette.
Ensuite compte tenu du fait que l'équipe gestion projet, MOA, MOE et DEV sont les mêmes persones, rédaction des spécifications fonctionnelles au four et à mésure du développement. Le développement doit être abordé tôt avec une approche agile d'itération et amélioration continue.
On parle de jalons si on a des livraisons: le client accepte-t-il le principe de plusieurs livraisons?


o Jalon n.1 > Conception de la  solution
consistant à rédiger les livrables suivants : Rédaction du cahier des charges, des spécifications fonctionnelles générales et détaillées, des spécifications techniques générales et détaillées, du diagramme des classes et de la modélisation des use cases.
Ce jalon doit être idéalement terminé pour le 22/05/2016, avec une tolérance de 7 jours pour commencer la phase de développement de la solution au plus tard début juin.

o Jalon n.2 > Développement de la solution : développement de l'interface web côté client, création de la base de données associée pour stocker l'historique de recherche des URL fournis par les utilisateurs, développement des script de crawling des URL fournis et des pages associées, développement du script de génération des résultats du crawling.
Ce jalon doit être idéalement terminé pour le 27/06/2016, avec une tolérance de 4 jours pour commencer la phase de recette avant le rendu fin juillet.

o Jalon n.3 > Recette : rédaction du cahier de recette et tests utilisateurs.
Ce jalon doit être idéalement terminé pour le 10/07/2016, avec une tolérance de 2 jours pour déployer la solution au plus tard 13/07/2016.

Il sera diffusé toutes les 15 jours un état du tableau de bord et une réunion avec les membres de l'équipe projet.


## les contraintes liés au projet sont :

* Choix des langages de programmation à intégrer au projet (en dehors du python).
* Les contraintes professionnelles de chaque membre de l’équipe projet.
* La tenue des délais pour les différentes étapes du projet.
* Le langage de programmation Python est encore peu maitrisée par l'équipe.


## Risques

* Le manque de cohésion dans le groupe projet.
* Le manque de cadrage dans le déroulement du projet.
* Une mauvaise répartition des tâches entre les membres de l'équipe projet.
* Incompréhension du sujet de départ.

##Evolution du projet

* Fournir des statistiques inhérents au pages recherchées.
* Aller plus loin sur le principe récursif de recherche des pages associées à l'URL de départ.

## Moyens disponibles

* Une plateforme de travail collaboratif : Github.
* Un cahier des charges.
* Un gantt avec suivi de l'avancement en temps réel.
* Un IDE : PyCharm.

## Mots clefs du projet

* Recherche
* Exploration
* Web
* Crawler
* Statistiques
* Mots
* Sujet

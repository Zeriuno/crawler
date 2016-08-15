* Affichage
* XML
* Traitement BDD:
  * enregistrer les résultats de la première page
    ```
    INSERT INTO url(url, DATETIME) VALUES (crawling[0][0].address, CURDATE()); --> améliorer CURDATE qui ne retourne que le jour, pas l'heure
    INSERT INTO words(item, occurrences, percentage, idurl)
      SELECT crawling[0][0].results[0][2], crawling[0][0].results[0][0], crawling[0][0].results[0][1], MAX(idurl)
      FROM url;
    ```
  * récupérer idurl et le passer au phases suivantes -> pas nécessaire, ce sera toujours `MAX(idurl) FROM url`
  * pour chaque lien:
    * si il y a des mots, pour chaque mot enregistrer url, mot, pourcentage, niveau de récursion
    * si il n'y a pas de mots, idsuite, urlsuite, idword = null, pourcentage = null, niveau
* Stopwords

~~* Pour l'instant on code en dur utilisateur et mot de passe de la BDD.~~

~~* Faire sauter les limites horizontales de récursion: on ne va pas le faire, mais on va passer les limites horizontales à des variables (non plus un chiffre, en dur, mais une variable)~~

~~* Création du résultat~~

  ~~* Quand on a une URL on contrôle si elle est présente dans la BDD~~

  ~~* Si oui on récupère un la liste de mots depuis celle-ci~~

  ~~* Effacer les vieux trucs~~

* Affichage → extends http://jinja.pocoo.org/docs/dev/templates/#template-inheritance

* XML

* Réparer requête avec MAX(...) FROM ...WHERE...

* Stopwords

~~* Pour l'instant on code en dur utilisateur et mot de passe de la BDD.~~

~~* Faire sauter les limites horizontales de récursion: on ne va pas le faire, mais on va passer les limites horizontales à des variables (non plus un chiffre, en dur, mais une variable)~~

~~* Création du résultat~~

~~* Traitement BDD:~~

  ~~* Quand on a une URL on contrôle si elle est présente dans la BDD~~

  ~~* Si oui on récupère un la liste de mots depuis celle-ci~~

  ~~* Effacer les vieux trucs~~

  ~~* enregistrer les résultats de la première page~~

  ~~* pour chaque lien:~~

      ~~* si il y a des mots, pour chaque mot enregistrer url, mot, pourcentage, niveau de récursion~~

      ```
      INSERT INTO suite(urlsuite, idword, percentagesuite, occurrencessuite, niveausuite)
      SELECT $url, idword FROM words WHERE item = $item AND idurl = MAX(idurl)
      ```
      ~~* si il n'y a pas de mots, idsuite, urlsuite, idword = null, pourcentage = null, niveau~~

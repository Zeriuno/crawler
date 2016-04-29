* Utilisateur anonyme
* Ouvre le site internet
* L'utilisateur fournit une URL
* le crawler analyse la page et en ressort les mots-cléfs
    * On teste si l'URL est valide
    * Le crawler récupère la page
    * Chercher si la page contient des pages associées (recherche de liens sur la page)
    * Le crawler recherche les mots (analyse la page)
    * 'beautifulsoup glop' prendre la page : pomper la page et faire un dico de fréquence, nb de fois que le mot est compté et faire le calcul des proportions.
    * On présente les resultats de la page
    * On demande si le crawler doit chercher les mots clefs dans les pages associées  
* Si pages associées, le crawler analyse les pages en cherchant les mots-cléfs trouvés dans la page initiale.
* Le résultat est présenté uniquement si le pourcentage de présence est supérieur à x%

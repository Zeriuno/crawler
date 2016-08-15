import pymysql

class URLWords(object):
    """
    Objet pour traiter les résultats des analyses des pages en vue de les afficher.


    Attributs:
        address: l'url de la page analysée
        results: une liste avec mots, leur occurrence, leur pourcentage ([3, 42.86, 'salut'], [2, 28.57, 'bonjour'], [2, 28.57, 'adieu'])
    """

    def __init__(self, Page: object) -> object:
        """
        Pour créer un objet URLWords en passant la classe Page.
        Exemple d'utilisation:
        analysePage = URLWords(Page1)
        """
        self.address = Page.url
        self.results = []

    def save1(self, connectdb):
        """
        Enregistre les données du premier niveau de recherche dans la base.
        """
        curs = connectdb.conn.cursor()
        curs.execute("INSERT INTO url (url, date) VALUES ('"+self.address+"', NOW())")
        for item in self.results:
            curs.execute("INSERT INTO words(item, occurrences, percentage, idurl) SELECT '"+item[2]+"', '"+item[0]+"', '"+item[1]+"', MAX(idurl) FROM url")


    def showcrawling(self):
        print("Résultats de la page " + self.address)
        if self.results:  # si la liste est vide, ce test donne FALSE
            cpt = 0
            while cpt < len(self.results):
                print("Mot : " + self.results[cpt][2])
                print("Occurences : " + str(self.results[cpt][0]))
                print("Pourcentage : " + str(self.results[cpt][1]))
                cpt += 1
        else:
            print("Aucun.")

import pymysql

class db:
    """
    Classe pour gérer la base de données.

    Tables:
        * url (id, url, date)
        * words (id, item, occurrences, percentage, *id*)

    * insertPage(Page) insère url et date dans url et les éléments de wordset dans words
    * readPage(Page) à partir de Page.url, récupère le wordset (retourné comme liste)

    À faire: tester si la date est présente pour ajourd'hui.
    Supprimer les contenus plus vieux de x jours.
    """

    def __init__(self):
        """
        """
        file = open("db.conf", "r")
        conf = file.read()
        host = conf.split("\n")[0]
        port = conf.split("\n")[1]
        user = conf.split("\n")[2]
        password = conf.split("\n")[3]
        database = conf.split("\n")[4]
        charset = conf.split("\n")[5]
        self.conn = pymysql.connect(host, int(port), user, password, database, charset)

    def insertPage(self, Page):
        """
        Insère une page analysée dans la base.
        """
        curs = self.conn.cursor()
        curs.execute("INSERT INTO url (url, date) VALUES ('"+Page.url+"', CURDATE())")
        cpt = 0
        for setitem in Page.wordset:
            curs.execute("INSERT INTO words(url, item, occurrences, percentage) VALUES ('"+Page.url+"', '"+Page.wordset[cpt][3]+"','"+Page.wordset[cpt][0]+"','"+Page.wordset[cpt][2]+"')")
            cpt += 1
        self.conn.commit()

    def readPage(self, Page):
        """
        Pour extraire le wordset d'une page, à partir d'une URL
        """
        curs = self.conn.cursor()
        curs.execute("SELECT occurrences, percentage, item FROM words WHERE (url = '"+Page.url+"')")
        request = curs.fetchall()
        wordset_temp=[]
        for row in request:
            wordsetitem_temp=[]
            wordsetitem_temp.append(row["occurrences"], row["percentage"], row["item"])
            wordset_temp.append(wordsetitem_temp)
        return wordset_temp

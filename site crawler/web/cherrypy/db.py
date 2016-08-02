import pymysql

class db:
    """
    Classe pour gérer la base de données.
    """

    def __init__(self, db:object):
        """
        """
        self.conn = pymysql.connect(host='localhost', port= 3306, user="mimocrawlerusr", password="yolo", database="mimocrawlerdb", charset='utf8')

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

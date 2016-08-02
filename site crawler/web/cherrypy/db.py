import pymysql

class db:
    """
    Classe pour gérer la base de données.
    """

    def __init__(self, db:object):
        """
        """
        self.conn = pymysql.connect(host='localhost', port= 3306, user="mimocrawlerusr", password="yolo", database="mimocrawlerdb", charset='utf8')

    def insertPage(Page):
        """
        Insère une page analysée dans la base.
        """
        curs = self.conn.cursor()
        curs.execute("INSERT INTO url (url, date) VALUES ('"+Page.url+"', CURDATE())")
        for setitem in Page.wordset:
            curs.execute("INSERT INTO words(url, item, occurrences, percentage) VALUES ('"+Page.url+"', item'""')")
        self.conn.commit()

    def readPage(Page):


# Pour la lecture:
#     ```
#     for row in result:
#           mooc.append([row["url"],row["titre"],row["descrip"],row["effort"],row["price"],row["level"],row["view"],row["rate"],score])
#     ```
#
# /*
# La requête pour obtenir les mots d'une page est
#
# SELECT item, occurrences, percentage
# FROM  words
# WHERE url = $item ;
# */

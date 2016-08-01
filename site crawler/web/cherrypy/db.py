import pymysql

class db:
    """
    Classe pour gérer la base de données.
    """

    def __init__(self, db:object) -> object:
        """
        """

        self.pymysql.connect(host='localhost', port= 3306, user="", password="", database="", charset='utf8')

    def insertPage(Page):
        """
        Insère une page analysée dans la base.
        """
        cur = self.cursor()
        # date = date() # obtenir la date du jour et la mettre dans une variable
        cur.execute("insert into url (url,titre,descrip,effort,price,level,view,rate) values ('"+url+"','"+titre+"','"+descrip+"','"+effort+"','"+price+"','"+level+"','"+view+"','"+rate+"')")

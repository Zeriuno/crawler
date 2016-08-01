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

    def readPage(Page):


Pour la lecture:
    ```
    for row in result:
          mooc.append([row["url"],row["titre"],row["descrip"],row["effort"],row["price"],row["level"],row["view"],row["rate"],score])
    ```

/*
INSERT INTO url(url, date)
+ Page.url +, CURDATE());

La requête pour obtenir les mots d'une page est

SELECT item, occurrences, percentage
FROM  words
WHERE url = $item ;
*/

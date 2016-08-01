import pymysql

class db:
    """
    Classe pour gérer la base de données.
    """

    def __init__(self, db:object) -> object:
        """
        """

        self.pymysql.connect(host='localhost', port= 3306, user="", password="", database="", charset='utf8')

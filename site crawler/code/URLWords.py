class URLWords(object):
    '''
    Objet pour traiter les résultats des analyses des pages en vue de les transférer dans le résultat et de les stocker.


    Attributs:
        address: l'url de la page analysée
        wordlist: une liste avec mots, leur occurrence, leur pourcentage (["salut", 3, 42.86], ["bonjour",  2, 28.57], ["adieu", 2, 28.57])
    '''

    def __init__(self, Page):
        '''
        Pour créer un objet URLWords en passant la classe Page.
        Exemple d'utilisation:
        analysePage = URLWords(Page1)
        '''
        self.address = Page.url
        self.wordlist = Page.wordlist

#fonction pour mettre dans le résultat
#fonction pour sauvegarder

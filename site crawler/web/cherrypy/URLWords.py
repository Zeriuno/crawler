class URLWords(object):
    '''
    Objet pour traiter les résultats des analyses des pages en vue de les afficher.


    Attributs:
        address: l'url de la page analysée
        results: une liste avec mots, leur occurrence, leur pourcentage ([3, 42.86, 'salut'], [2, 28.57, 'bonjour'], [2, 28.57, 'adieu'])
    '''

    def __init__(self, Page: object) -> object:
        '''
        Pour créer un objet URLWords en passant la classe Page.
        Exemple d'utilisation:
        analysePage = URLWords(Page1)
        '''
        self.address = Page.url


#fonction pour mettre dans le résultat


#fonction pour sauvegarder

class URLWords(object):
    '''
    Objet pour traiter les résultats des analyses des pages.


    Attributs:
        address: l'url de la page analysée
        wordcount: un entier pour le total des mots.
        wordsitems: une liste avec mots, leur occurrence, leur pourcentage (["salut", 3, 42.86], ["bonjour",  2, 28.57], ["adieu", 2, 28.57])
    '''

    def __init__(self, url):
        '''
        Pour créer un objet URLWords en passant l'URL en paramètre (la première valeur qu'on a, on la stocke donc directement).
        Exemple d'utilisation:
        analysePage = URLWords(url)
        '''
        self.address = url
class page(object):
    '''
    Objet pour traiter une page.

    Attributs:
        url : pour garder l'adresse de la page.
        soup: pour traiter la page via BeautifulSoup
    '''

    def __init__(self, url):
        '''
        '''
        self.url = url
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")

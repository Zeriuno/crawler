class Page:
    '''
    Objet pour traiter une page.

    Attributs:
        url : pour garder l'adresse de la page.
        soup: pour traiter la page via BeautifulSoup
        links: liste avec les liens présents dans la page, sans doublons.
    '''

    def __init__(self, url):
        '''
        '''
        self.url = url
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        # Récupère les liens de la page et les place dans un tableau.
        self.links = []
        for link in self.soup.find_all('a'):
            url = link.get('href')
            if(url not in self.links):
                self.links.append(url)

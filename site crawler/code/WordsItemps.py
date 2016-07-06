class WordsItems(object):
    '''
    Objet qui sera envoyé à URLWords.
    Il contient: ["salut", 3, 42.86]

    word: le mot retourné par l'analyse de la page.
    count: le nombre d'occurences du mot dans la page.
    percent: le pourcentage de présence du mot dans la page.
    '''

    def __init__(self):
        '''
        
        '''

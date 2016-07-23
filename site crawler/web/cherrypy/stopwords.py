import re
from nltk.tokenize.regexp import RegexpTokenizer

reg_words = r'''(?x)
      aujourd'hui    # exception 1
    | prud'hom\w+ # exception 2
    | \d+(,\d+)?\s*[%€$] # les valeurs
    | \d+                # les nombres
    | \w'                 # les contractions d', l', j', t', s'
    | \w+(-\w+)+    # les mots composés
    | (\d|\w)+         # les combinaisons alphanumériques
    | \w+               # les mots simples
    '''

tokenizer = RegexpTokenizer(reg_words, flags=re.UNICODE | re.IGNORECASE)

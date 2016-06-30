#import urllib2
from collections import Counter
from nltk import word_tokenize
from bs4 import BeautifulSoup
url = "http://www.lemonde.fr"
page = urllib2.urlopen(url).read()
for i in BeautifulSoup(page).find_all('p'):
...     print i.text.strip()#erreur de syntaxe
word_freq = Counter(word_tokenize(text))

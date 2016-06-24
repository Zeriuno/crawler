>>> import urllib2
>>> from collections import Counter
>>> from nltk import word_tokenize
>>> from bs4 import BeautifulSoup as bsoup
>>> url = "http://www.lemonde.fr"
>>> page = urllib2.urlopen(url).read()
>>> for i in bsoup(page).find_all('p'):
...     print i.text.strip()
>>> word_freq = Counter(word_tokenize(text))
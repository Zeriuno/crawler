# Tester python

Python est un langage qui offre le grand avantage d'avoir une modalité interactive: tu ouvres une console, tapes ton code et vois tout de suite s'il marche ou pas, si et où l'ajuster.

## Comment faire

1. Ouvrir un terminal et taper `python3`. L'environnement change et on a trois chevrons, comme ça:
```
>>>
```
Pour sortir de ça, deux alternatives: taper `ctrl d` ou bien `exit()`.
2. Taper le code (attention à l'indentation). Par exemple:
```
def grabpage(lien):
      r = requests.get(lien)
      soup = BeautifulSoup(r.content, "html.parser")
      return soup
url = "http://liberation.fr/"
soup_test = grabpage(url)
```
3. Attention aux messages de retour. Par exemple le code ci-dessus donne:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in grabpage
NameError: name 'requests' is not defined
```
Car la fonction `grabpage` utilise `requests` et on ne l'a jamais importé (dans le fichier non plus.)
On le note dans le fichier au bon endroit et dans la console on tape la même chose:
```
import requests
```
Encore une erreur:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in grabpage
NameError: name 'BeautifulSoup' is not defined
```
Car on n'a pas importé `BeautifulSoup`. Du coup:
```
from bs4 import BeautifulSoup
```
Et à ce moment là plus d'erreur. Ça a marché? Testons:
```
print(soup_test)
```
(chez moi ça marche).

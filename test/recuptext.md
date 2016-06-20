import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.lemonde.fr")
soup = BeautifulSoup(r.content, "html.parser")
print soup.prettify()
soup.get_text()

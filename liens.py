import sys, string, os
from bs4 import BeautifulSoup

adresse = sys.argv[1]

print(adresse)
soup = BeautifulSoup(open("test/liens.html"))

links = soup.find_all('a')

#for link in links:
#   if(link[0] == '.'):
#        if(link[1] == '.'):
#            link =
#        else:
#            link = adresse + link
#    elif(link[0] == '/'):
#        link =
#    print(link)

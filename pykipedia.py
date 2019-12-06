import requests as r
from bs4 import BeautifulSoup
import string
import sys,os

# Import all the things
assunto = input('Qual o assunto? ~>')
assunto = assunto.strip()
assunto = assunto.replace(" ", "_")
# String treatment
page = r.get('https://pt.wikipedia.org/wiki/{}'.format(assunto))
soup = BeautifulSoup(page.text, 'html.parser')
# Parser
p = soup.find_all('p')
i = soup.find_all('i')
li = soup.find_all('li')
span = soup.find_all('span')
# <> stuff
print('Consultando wikipedia...\n')
os.system('sleep 3')
# Begin loop
c = 0
while c < len(p):
  print(p[c].get_text())
  c += 1
#End loop



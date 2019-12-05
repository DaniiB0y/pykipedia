import requests as r
from bs4 import BeautifulSoup
import string

assunto = input('Qual o assunto? ~>')
assunto = assunto.strip()
assunto = assunto.replace(" ", "_")
print(assunto)
page = r.get('https://pt.wikipedia.org/wiki/{}'.format(assunto))
soup = BeautifulSoup(page.text, 'html.parser')
p = soup.find_all('p')
c = 0
while c < len(p):
  print(soup.find_all('p')[c].get_text())
  c += 1
  if c == len(p):
    print(soup.find_all('i')[c].get_text())
    print(soup.find_all('li')[c].get_text())
    print(soup.find_all('a')[c].get_text())




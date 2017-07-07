import requests
from bs4 import BeautifulSoup
import time
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')

soup = BeautifulSoup(response.text,"html.parser")

page = soup

article_chain = []

while(page.title != '<title>Philosophy - Wikipedia<title/>'):
    article_chain.append(page)
    test = soup.p
    test2 = test.a
    print(test2['href'])
    download = requests.get('https://pt.wikipedia.org'+test2['href'])
    soup = BeautifulSoup(download.text,"html.parser")
    page = soup
    time.sleep(2)

print('ACHOU')

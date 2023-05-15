from bs4 import BeautifulSoup

import requests
import pandas as pd

root="https://subslikescript.com"
url=f"{root}/movies"

page=requests.get(url)

page_text=page.text

soup=BeautifulSoup(page_text,'lxml')

body=soup.find('article', class_='main-article')

links=[]
for link in body.find_all('a',href=True):
    links.append(link['href'])

for link in links:
    url=f"{root}/{link}"
    page=requests.get(url)
    page_text=page.text
    soup=BeautifulSoup(page_text,"lxml")
    body=soup.find('article', class_='main-article')
    title=body.find('h1').get_text()
    article=body.find('div',class_="full-script").get_text(strip=True,separator=" ")

    with open(f'{title}.txt','w') as file:
        file.write(article)



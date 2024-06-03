import requests
from bs4 import BeautifulSoup

detik_html = requests.get('https://news.detik.com/indeks')
soup = BeautifulSoup(detik_html.text, 'html.parser')

news = soup.find(class_='grid-row list-content')
titles = news.findAll(class_='media__title')
images = news.findAll(class_='media__image')

for image in images:
    print(image.find('a').find('img')['title'])
# print(titles)

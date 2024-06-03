import requests
from bs4 import BeautifulSoup

# detik_html = requests.get('https://news.detik.com/indeks')
# soup = BeautifulSoup(detik_html.text, 'html.parser')
#
# news = soup.find(class_='grid-row list-content')
# titles = news.findAll(class_='media__title')
# images = news.findAll(class_='media__image')

# for image in images:
#     print(image.find('a').find('img')['title'])
# # print(titles)

jadwal = requests.get('https://jadwalsholat.org/adzan/monthly.php?id=232')
soup = BeautifulSoup(jadwal.text, 'html.parser')
data = soup.find_all('tr', 'table_highlight')
data = data[0]
shalat = {}

i = 0
for d in data:
    print('shalat : ', d.get_text())
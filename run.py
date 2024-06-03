import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-news')
def detik_news():
    detik_html = requests.get('https://news.detik.com/indeks')
    soup = BeautifulSoup(detik_html.text, 'html.parser')

    news = soup.find(class_='grid-row list-content')
    titles = news.findAll(class_='media__title')
    images = news.findAll(class_='media__image')

    return render_template('detik-news.html', images=images)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('https://www.floatrates.com/daily/idr.json')
    json_data = source.json()

    return render_template('idr-rates.html', datas=json_data.values())

@app.route('/sholat')
def jadwal_sholat():
    jadwal = requests.get('https://jadwalsholat.org/adzan/monthly.php?id=232')
    soup = BeautifulSoup(jadwal.text, 'html.parser')
    data = soup.find_all('tr', 'table_highlight')
    data = data[0]

    return render_template('sholat.html', datas=data)

if __name__ == '__main__':
    app.run(debug=True)
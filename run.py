import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-news')
def detik_news():
    detik_html = requests.get('https://news.detik.com/indeks')
    soup = BeautifulSoup(detik_html.text, 'html.parser')

    news = soup.find(class_='grid-row list-content')
    titles = news.findAll(class_='media__title')
    images = news.findAll(class_='media__image')

    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
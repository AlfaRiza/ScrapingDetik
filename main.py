import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

populers = soup.find('div', attrs={'class': 'grid-row list-content'})

# contens = populers.findAll('article', attrs={'class': 'list-content__item'})
titles = populers.findAll(attrs={'class': 'media__title'})
images = populers.findAll(attrs={'class': 'media__image'})
for image in images:
    print(image.find('a').find('img')['title'])

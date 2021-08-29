import json
import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests.api import request

URL = 'https://books.toscrape.com/?'
page = requests.get(URL)

def getBooks():
    soup = BeautifulSoup(page.text, 'lxml')
    bookList = []
    for heading in soup.select('a[href*="catalogue"]'):
        bookTitle = heading.get('title')
        if bookTitle != None:
            bookList.append(bookTitle)
    for price in soup.select('p[class*="price_color"]'):
        bookList.append(price.get_text())

    for img in soup.findAll('div', {'class': 'image_container'}):
        for image in img.findAll('img',src=True):
            bookList.append(image['src'])
    return bookList

print(getBooks())

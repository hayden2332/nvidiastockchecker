import requests
from bs4 import BeautifulSoup
import time


def check_stock():
    URL = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/'
    available = False
    while not available:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        btnClass = soup.find(class_="cta mobile-top").findNext('div').get("class")
        if not btnClass[2] == 'show-out-of-stock':
            available = True
            break
        else:
            time.sleep(1)

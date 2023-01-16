import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from pprint import pprint
import re

url = 'https://steamcommunity.com/market/itemordersactivity?country=GE&language=english&currency=1&item_nameid=176288467&two_factor=0'

def main(url):
    r = requests.get(url)
    data = dict(r.json())

def second(data):
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('div')
    for item in items:
        avatar = item.find('span', {'class': 'market_ticker_avatar'})
        name = item.find('span', {'class': 'market_ticker_name'})
        print(avatar, name)
    
    
    
    
#     # items = soup.find_all('div')
#     # for item in items:
#     #     avatar = item.find('span', {'class': 'market_ticker_avatar'})
#     #     name = item.find('span', {'class': 'market_ticker_name'})
#     # print(avatar,name)

x = main(url)
second(x)



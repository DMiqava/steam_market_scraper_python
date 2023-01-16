import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = 'https://steamcommunity.com/market/search/render/?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=tag_WearCategory1&category_730_Exterior%5B%5D=tag_WearCategory4&category_730_Exterior%5B%5D=tag_WearCategory3&category_730_Exterior%5B%5D=tag_WearCategory0&category_730_Type%5B%5D=tag_CSGO_Type_Pistol&category_730_Type%5B%5D=tag_CSGO_Type_Rifle&category_730_Type%5B%5D=tag_CSGO_Type_SniperRifle&category_730_Type%5B%5D=tag_CSGO_Type_Knife&category_730_Type%5B%5D=tag_Type_Hands&appid=730#p1_popular_desc'

def totalresults():
    r = requests.get(url)
    data = dict(r.json())
    total = data['total_count']
    return int(total)

def get_data(url):
    r = requests.get(url)
    data = dict(r.json())
    return data['results_html']

def parse(data):
    itemslist = []
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('a')
    for item in items:
        listing = item['href']
        itemimg = item.find('img', {'class': 'market_listing_item_img'})['src']
        title = item.find('span', {'class': 'market_listing_item_name'}).text
        price = item.find('span', {'class': 'normal_price'}).text

        myitems = {
            'itemimg': itemimg,
            'listing': listing,
            'title': title,
            'price': price,
        }
        specific_item = requests.get(listing)
        specific_item_data = dict(specific_item.json())
        a = specific_item_data['results_html']
        

        itemslist.append(myitems)
    return itemslist


def output(itemslist):
    itemsdf = pd.concat([pd.DataFrame(g) for g in results])
    itemsdf.to_csv('itemslistings.csv', index=False)
    return

# data = get_data(url)
# gameslist = parse(data)
# output(gameslist)

results = []
for x in range(0, 30, 10):
    data = get_data(f'https://steamcommunity.com/market/search/render/?query&start={x}&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=tag_WearCategory1&category_730_Exterior%5B%5D=tag_WearCategory4&category_730_Exterior%5B%5D=tag_WearCategory3&category_730_Exterior%5B%5D=tag_WearCategory0&category_730_Type%5B%5D=tag_CSGO_Type_Pistol&category_730_Type%5B%5D=tag_CSGO_Type_Rifle&category_730_Type%5B%5D=tag_CSGO_Type_SniperRifle&category_730_Type%5B%5D=tag_CSGO_Type_Knife&category_730_Type%5B%5D=tag_Type_Hands&appid=730#p1_popular_desc')
    results.append(parse(data))
print("Scraping is Done!")

output(results)
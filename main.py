from bs4 import BeautifulSoup as BS
import requests
from time import sleep

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

r = requests.get(f'https://www.binance.com/ru/markets', headers=HEADERS)
soup = BS(r.content, 'html.parser')

all_crypto = soup.find('div', style='min-height:800px').find_all('div', class_='css-vlibs4')
for crypto in all_crypto:
    not_full_name = crypto.find('a').find('div').find_next('div').find_next('div')
    full_name = not_full_name.find_next('div').find('div')
    price = crypto.find('div', style='direction:ltr')
    proc = price.find_next('div', style='direction:ltr')

    print(f'{full_name.text} ({not_full_name.text}):')
    print(f' Цена: {price.text}')
    print(f' Цена за день: {proc.text}')
    print()

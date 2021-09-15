import bs4 
from bs4 import BeautifulSoup
import pandas as pd
import requests
url = 'https://liannewriting.github.io/scraping_example.html'
response = requests.get(url)
print(f'Visited: {response.url}')
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
data_containers = soup.find_all('div', class_= 'data-container')
print(data_containers)
dat = []
for dc in data_containers:
    fruit = dc.text
    dat.append(fruit)
print(dat)
data_table = soup.find('table', id='data-table')
print(data_table)
data_table_tds = data_table.find_all('td')
print(data_table_tds)
addresses = []
prices = []
for i, td in enumerate(data_table_tds):
    if i % 2:
        prices.append(td.text)
    else:
        addresses.append(td.text)
df_fruit = pd.DataFrame(data=dat, columns=['fruit_name'])
print(df_fruit)
df_prices = pd.DataFrame(data={'addresses': addresses, 'prices': prices})
print(df_prices)
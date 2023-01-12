import csv

import requests
import re
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf-8').decode('ascii','ignore')
soup = BeautifulSoup(text,'lxml')
table = soup.find('table', class_ = 'wikitable')
rows = table.find_all('tr')[1:]

iPhone_price = {}

for row in rows:
    data = row.find_all(['th','td'])
    try:
        version_text = data[0].a.text.split(' ')[1]
        version = re.sub(r"\D", "", version_text)
        version = int(version)
        # print(version)

        price_text = data[-1].text.split('/')[1]
        price = re.sub(r"\D", "", price_text)
        price = int(price)

        if version and price > 100 and price < 99999:
            # print(version, price)
            iPhone_price[version] = price
    except:
        pass

print(iPhone_price)

csv_fields = ['version','price']

with open('iphone_price.csv', 'w', newline='') as csvFile:
    csvwriter = csv.writer(csvFile)
    csvwriter.writerow(csv_fields)
    for key, value in iPhone_price.items():
        csvwriter.writerow([key, value])
    csvFile.close()
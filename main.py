import requests
import csv
from bs4 import BeautifulSoup

result = requests.get('http://quotes.toscrape.com/')
page = result.text


soup = BeautifulSoup(page, 'html.parser')

quotes = soup.find_all('div', class_='quote')

scraped = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    scraped.append([text, author])


with open('quotes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for quote in scraped:
        writer.writerow(quote)
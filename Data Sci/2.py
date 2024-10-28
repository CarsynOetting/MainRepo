# basic webscraper

from bs4 import BeautifulSoup
import requests

URL = 'https://www.youtube.com/watch?v=CJXtTWN4NQE'

data = requests.get(URL).text

soup = BeautifulSoup(data, 'html.parser')

print(soup.prettify())


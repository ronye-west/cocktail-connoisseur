import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = 'https://iba-world.com/category/iba-cocktails/the-unforgettables/'
html_text = requests.get(url).text

print(html_text)
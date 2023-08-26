import requests
from bs4 import BeautifulSoup
import pandas as pd

org = 1084205013155
url = 'https://checko.ru/company/resurs-' + str(org)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find("section", id="competitors")
headers = []
for i in table1.find_all("td"):
    title = i.text
    headers.append(title)
print(headers)

List_table = []

Champion = input("챔피온을 입력하시오")

import requests
from bs4 import BeautifulSoup

url = 'https://lol.fandom.com/wiki/Special:RunQuery/PickBanHistory?PBH%5Bpage%5D=LCK+2021+Spring+Playoffs&PBH%5Btextonly%5D=Yes&pfRunQueryFormName=PickBanHistory'

response = requests.get(url)


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('tbody')
    titles = ul.select('tbody > tr > td')
    for title in titles:
        List_table.append(title.get_text())

    print(List_table.count(Champion))


else :
    print(response.status_code)



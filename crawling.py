List_table = []

Champion = input("챔피온을 입력하시오")

import requests
from bs4 import BeautifulSoup

url = 'https://lol.fandom.com/wiki/Special:RunQuery/PickBanHistory?PBH%5Bpage%5D=LCK+2021+Spring+Playoffs&PBH%5Btextonly%5D=Yes&pfRunQueryFormName=PickBanHistory'

response = requests.get(url)


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

#------------------------------------------------------------

    ul = soup.select_one('tbody')
    titles = ul.select('tbody > tr > td')
    for title in titles:
        print(title.get_text())
        List_table.append(title.get_text())

    print(List_table)
    print(List_table.count(Champion))


else :
    print(response.status_code)






    # copyselector 분석 (밴)
    # pbh-table > tbody > tr:nth-child(3) > td:nth-child(7)
    # pbh-table > tbody > tr:nth-child(4) > td:nth-child(7)
    # pbh-table > tbody > tr:nth-child(7) > td:nth-child(7)
    # pbh-table > tbody > tr:nth-child(5) > td:nth-child(8)

    # pbh-table > tbody > tr:nth-child(3) > td:nth-child(17)
    # pbh-table > tbody > tr:nth-child(3) > td:nth-child(18)
    # pbh-table > tbody > tr:nth-child(3) > td:nth-child(19)
    # pbh-table > tbody > tr:nth-child(3) > td.pbh-ban.pbh-blue.pbh-divider

    # pbh-table > tbody > tr:nth-child(3) > td.pbh-ban.pbh-blue.pbh-divider
    # pbh-table > tbody > tr:nth-child(4) > td:nth-child(13)
    # pbh-table > tbody > tr:nth-child(5) > td:nth-child(13)
    # pbh-table > tbody > tr:nth-child(6) > td:nth-child(13)

    # pbh-table > tbody > tr:nth-child(20) > td:nth-child(7) 3~20
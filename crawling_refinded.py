#불러오기

import requests, bs4

resp = requests.get("https://lol.fandom.com/wiki/Special:RunQuery/PickBanHistory?PBH%5Bpage%5D=LCK+2021+Spring+Playoffs&PBH%5Btextonly%5D=Yes&pfRunQueryFormName=PickBanHistory")
resp.encoding = 'utf-8'
html = resp.text
bs = bs4.BeautifulSoup(html, "html.parser")

#챔피언 설정

search = input("챔피온 입력")

#밴픽 추출 (클래스 pbh-ban인 것 추출)

divs = bs.find_all(class_="pbh-ban")

Matchlist = []
for word in divs:
    if search in word :
        Matchlist.append(word)

print("{}는 {}번 밴 당했습니다.".format(search, len(Matchlist)))

#픽 추출 (클래스 pbh-blue, pbh-red 인 것 추출)

#레드팀 픽(밴 포함)

divs_red = bs.find_all(class_="pbh-red")

Matchlist_red = []

for word in divs_red:
    if search in word :
        Matchlist_red.append(word)

#블루팀 픽(밴 포함)

divs_blue = bs.find_all(class_="pbh-blue")

Matchlist_blue = []

for word in divs_blue:
    if search in word :
        Matchlist_blue.append(word)

#블루팀 픽, 레드팀 픽리스트 합치기(밴 제외)

Matchlist_all = Matchlist_red + Matchlist_blue

for word in Matchlist :
    if word in Matchlist_all:
        Matchlist_all.remove(word)

print("{}는 {}번 픽됐습니다.".format(search, len(Matchlist_all)))


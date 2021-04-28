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
print(divs)
Matchlist = []
for word in divs:
    if search in word.text :
        Matchlist.append(word)

print(Matchlist)
print("{}는 {}번 밴 당했습니다.".format(search, len(Matchlist)))

#픽 추출 (클래스 pbh-blue, pbh-red 인 것 추출)

#레드팀 픽(밴 포함)

divs_red = bs.find_all(class_="pbh-red")
print(divs_red)
Matchlist_red = []

for word in divs_red:
    if search in str(word) :
        Matchlist_red.append(word)

print("red 픽은 {}".format(Matchlist_red))
print(len(Matchlist_red))

#블루팀 픽(밴 포함)

divs_blue = bs.find_all(class_="pbh-blue")
print(divs_blue)
Matchlist_blue = []

for word in divs_blue:
    if search in word.text :
        Matchlist_blue.append(word)

print(Matchlist_blue)
print(len(Matchlist_blue))

#블루팀 픽, 레드팀 픽리스트 합치기(밴 제외)

Matchlist_all = Matchlist_red + Matchlist_blue

print("그냥 합지면 {}".format(Matchlist_all))
print(len(Matchlist_all))

for word in Matchlist :
    if word in Matchlist:
        Matchlist_all.remove(word)

print(Matchlist_all)
print(len(Matchlist_all))
print("{}는 {}번 픽됐습니다.".format(search, len(Matchlist_all)))


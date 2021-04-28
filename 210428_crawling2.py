import requests, bs4

# 웹페이지 html 소스 가져오기
resp = requests.get("https://lol.fandom.com/wiki/Special:RunQuery/PickBanHistory?PBH%5Bpage%5D=LCK+2021+Spring+Playoffs&PBH%5Btextonly%5D=Yes&pfRunQueryFormName=PickBanHistory")
resp.encoding = 'utf-8'
html = resp.text

bs = bs4.BeautifulSoup(html, "html.parser")
# div에서 id가 id_py_quiz인것만 추출
divs = bs.select("#pbh-table")
print(divs)

a = list(map(str, divs))

Matchlist = []
search = "Gnar"

for word in a:
    if search in word :
        Matchlist.append(word)


print(Matchlist)


#pbh-table > tbody > tr:nth-child(3) > td:nth-child(7)
# pbh-table
# #pbh-outer

#pbh-table > tbody > tr:nth-child(3) > td:nth-child(7)   3~20
#pbh-table > tbody > tr:nth-child(3) > td:nth-child(13)   7~12, 17~20

#<td class="pbh-blue">Hecarim</td>

#< td class ="pbh-ban pbh-blue" > Gnar < / td >
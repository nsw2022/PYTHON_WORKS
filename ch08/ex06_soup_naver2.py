# naver 메뉴 가져오기
import requests
from bs4 import BeautifulSoup

class_name = "list_nav type_fix"
response = requests.get("https://www.naver.com/")
# print(response.text)
html = BeautifulSoup(response.text,'html.parser')
# print(html)

# 메뉴 - 메일, 카페, 블로그
menu_ul = html.find('ul',attrs={'class' : 'list_nav type_fix'})
first_li = menu_ul.find('li')
# print(first_li.text)
first_a = first_li.find('a').text
# print(first_a)

# 다른 메뉴 찾기 - findAll
all_li = html.findAll('li')

all_a = menu_ul.findAll('a') # 직접 a 태그 찾기
# print(all_a)
print(all_a[1].text) # 카페 찾음

for a in all_a:
    print(a)
    print(a.text)

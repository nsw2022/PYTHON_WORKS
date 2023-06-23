# naver 에서 필요한 정보 가져오기

import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')
# print(html)
print(html.title) # title태그
print(html.title.text) # title태그

# '네이버를 시작페이지로' 문자열 찾아오기
# print(html.find('div',"service_area").find('a').text) # 한번에 해보는 테스트 결과 성공
div = html.find('div',attrs={'class':'service_area'})
first_a = div.find('a')
print(first_a.text)

# 쥬니어 네이버 참고
print(html.find('div', "service_area").find('span').text)
all_a = div.findAll('a')
print(all_a[1])
print(all_a[1].text)

for a in all_a:
    print(a)
    print(a.text)
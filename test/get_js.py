# pycharm 무료버전에서는 자동완성 지원이안됨으로 js 키워드 w3s에서 가져오기
import requests
from bs4 import BeautifulSoup

url_for_html_DOM = "https://www.w3schools.com/jsref/dom_obj_document.asp"
url_for_html_DOM_class = "ref_overview"

url_for_array = "https://www.w3schools.com/jsref/jsref_obj_array.asp"

response = requests.get(url_for_html_DOM)
html = BeautifulSoup(response.text,"html.parser")
dom_div = html.find('table',attrs={'class':'ws-table-all notranslate'})
dom_a = dom_div.select_one('td.a')
print(dom_a)

# 왜 array가 튀어나오냐 세상 슬프고 아마 첫 클래스만 출력해준거같음 지금보니 이름이 겹침


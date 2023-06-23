import urllib.request
import json
import requests

url = 'http://openapi.seoul.go.kr:8088/4d6e42445a746d6437354e65737162/json/tbLnOpendataRentV/1/1000/'

response = urllib.request.urlopen(url)
response_message = response.read().decode('utf8')

data = json.loads(response_message)
total_count = data['tbLnOpendataRentV']['list_total_count']

result_list = []  # 결과를 저장할 빈 리스트
count = 0
for item in data['tbLnOpendataRentV']['row']:
    if item['BUBN'] != "" or item['BLDG_NM'] != "" or item['BUBN'] != "":
        if item['BUBN'] != "0000":
            result = item['SGG_NM'] + ' ' + item['BJDONG_NM'] + ' ' + item['BOBN'] + ' ' + item['BUBN']
            result_list.append(result)
            count += 1
        elif item['BUBN'] == "0000":
            result = item['SGG_NM'] + ' ' + item['BJDONG_NM'] + ' ' + item['BOBN']
            result_list.append(result)
            count += 1

# 결과 출력
for result in result_list:
    print(result)

    url_front = "http://api.vworld.kr/req/address?"
    url_params = "service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type=road"
    url_address = "&address="
    url_key = "&key=7F333705-8E22-391D-A774-644985B13EDD"  # 인증키 입력

    address = str(result).replace(" ","")
    auth_key = "7F333705-8E22-391D-A774-644985B13EDD"

    # url 완성
    url = url_front + url_params + url_address + address + url_key

    print(url)

    result = requests.get(url)
    json_data = result.json()

    print(json_data)

    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        print("\n경도:", x, "\n위도:", y)
print("총 갯수:", count)

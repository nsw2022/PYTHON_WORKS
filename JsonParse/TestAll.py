import urllib.request
import json

'''
25개
강남구
강동구
강북구
강서구
관악구
광진구
구로구
금천구 
노원구
도봉구
동대문구
동작구
마포구
서대문구
서초구
성동구
성북구
송파구
양천구
영등포구
용산구
은평구
종로구
중구
중랑구
'''

'''
데이터 형식
{"tbLnOpendataRentV":
	{"list_total_count":5387856,"RESULT":
		{"CODE":"INFO-000","MESSAGE":"정상 처리되었습니다"},
			"row" :[
				{"ACC_YEAR":"2023",
				"SGG_CD":"11590"
 				,"SGG_NM":"동작구",
				"BJDONG_CD":"10200",
				"BJDONG_NM":"상도동",
				"LAND_GBN":"1",
				"LAND_GBN_NM":"대지",
				"BOBN":"0430",
				"BUBN":"0000",
				"FLR_NO":5.0,
				"CNTRCT_DE":"20230617",
				"RENT_GBN":"전세",
				"RENT_AREA":32.43,
				"RENT_GTN":"4871",
				"RENT_FEE":"0",
				"BLDG_NM":"상도에스에이치빌",
				"BUILD_YEAR":"2006","
				HOUSE_GBN_NM":"아파트",
				"CNTRCT_PRD":"","
				NEW_RON_SECD":"",
				"CNTRCT_UPDT_RQEST_AT":"",
				"BEFORE_GRNTY_AMOUNT":"",
				"BEFORE_MT_RENT_CHRGE":""
				}
'''

'''
json 기준 표
1	ACC_YEAR	접수연도
2	SGG_CD	자치구코드
3	SGG_NM	자치구명
4	BJDONG_CD	법정동코드
5	BJDONG_NM	법정동명
6	LAND_GBN	지번구분
7	LAND_GBN_NM	지번구분명
8	BOBN	본번
9	BUBN	부번
10	FLR_NO	층
11	CNTRCT_DE	계약일
12	RENT_GBN	전월세 구분
13	RENT_AREA	임대면적(㎡)
14	RENT_GTN	보증금(만원)
15	RENT_FEE	임대료(만원)
16	BLDG_NM	건물명
17	BUILD_YEAR	건축년도
18	HOUSE_GBN_NM	건물용도
19	CNTRCT_PRD	계약기간
20	NEW_RON_SECD	신규갱신여부
21	CNTRCT_UPDT_RQEST_AT	계약갱신권사용여부
22	BEFORE_GRNTY_AMOUNT	종전 보증금
23	BEFORE_MT_RENT_CHRGE	종전 임대료

'''

# 마커찍기 방안 모색중
# 일단 지금까지 중간 파악
# 데이터 구조 파악완료, 아파트/단독다가구/연립다세대/오피스텔 중 하나로 데이터가 있음

# 마커 테스트 방안 ( 위도와 경도 없이 마커를 찍을수있는지 파악을 해야함.. 위도와 경도가 필요하다는 전제로 생각하겠음 )

# 1안(json 데이터 csv던 sql이던 저장후 거기서 발췌)
# 어차피 서버에서 그때마다 url타고 가서 파싱해서 하면 시간이 걸릴꺼같다는 판단이 들음..
# 그렇다면 csv던 sql던 데이터를 저장한후 거기서 추출해야 서버 처리 시간이 금방 처리할거 같다는 결론에 도달함
# 저장이 되어있다면 sql이던 if 조건문이던(구와 동 추출) 으로검색후 위도와 경도값을 추출후 각데이터에 넣어서 마커 추출
#
# 2안(json 에서 바로 조건으로 파싱)
# 이게 아니라면? -> 어차피 서버에서 그때마다 url타고 가서 파싱해서 하면 시간이 걸릴꺼같다는 판단이 들음..
# 서버에서 json 추출하면서 값을 전달하면 될꺼같다는 생각이 들음


# 쓰다보니 흠 아직 네이버API를 안해봐서 뭔가 헛도는 느낌이라 잠정 중단

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
# 실제로 데이터를 넣을때는 뒤에 강남구 조건빼고 건물이름도 빼야함

# 결과 출력
for result in result_list:
    print(result)

    import requests

    url_front = "http://api.vworld.kr/req/address?"
    url_params = "service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type=road"
    url_address = "&address="
    url_key = "&key="

    address = requests  # 청와대 도로명 주소
    auth_key = "7F333705-8E22-391D-A774-644985B13EDD"

    # url 완성
    url = url_front + url_params + url_address + address + url_key + auth_key

    print(url)

    result = requests.get(url)
    json_data = result.json()

    print(json_data)

    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        print("\n경도: ", x, "\n위도: ", y)
print("총갯수", count)


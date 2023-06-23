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

sgg_names = []  # 서울시 구단위를 저장할 빈배열

for item in data['tbLnOpendataRentV']['row']:
    # 리스트 중에 구단위 전부 저장(중복도 되게)
    sgg_nm = item['SGG_NM']

    '''
    # 없으면 넣어라 조건문
    if sgg_nm not in sgg_names:
        # 없으면 넣기때문에 중복을 걸러줌
        sgg_names.append(sgg_nm)
    '''

    # SGG_NM 가 강남구인거만 추출
count = 0
building_names = []  # 강남구의 건물명을 저장할 빈 리스트

for item in data['tbLnOpendataRentV']['row']:
    if item['BLDG_NM']:
        building_names.append(item['BLDG_NM'])
        count += 1

print("전체 건물 개수:", count)
print("전체 건물명:", building_names)



# 구단위 출력
# for sgg_name in sgg_names:
#     print(sgg_name)



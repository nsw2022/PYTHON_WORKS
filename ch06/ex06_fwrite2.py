# 파일 쓰기 - 리스트

try:
    season = ['봄', '여름', '가을', '겨울']
    f = open("E:/NSW/pyfile/season.txt", 'w')

    for i in season:
        f.write(i + ' ')

    # 파일 닫기
    f.close()
except FileNotFoundError:
    print("파일 쓰기를 실패 하였습니다!")
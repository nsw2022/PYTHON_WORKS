# season 파일 읽기
try:
    f = open("E:/NSW/pyfile/season.txt", 'r')

    data = f.read()
    print(data)

    f.close()

except:
    print("파일 못 찾겠다 히히")

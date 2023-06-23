# 파일 쓰기
try:
    # 파일 열기(경로, 쓰기 모드)
    f = open("E:/NSW/pyfile/file1.txt", 'w')
    # 파일 쓰기
    f.write('Hello\n') # 줄바꿈
    f.write("100 \n") # 숫자는 입력할수 없음 -> 문자형으로 변환
    n = 10 * 2
    f.write(str(n) + '\n')

    for i in range(1, 11):
        text = f'{i}번째 줄입니다.\n'
        f.write(text)
    print("쓰기완료")
    # 파일 종료
    f.close()
except:
    print("파일을 쓰기를 실패 했습니다.!")
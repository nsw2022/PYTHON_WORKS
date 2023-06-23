'''
암호가 틀리면 암호다시 출력하고 다시물어봄 -> 반복문을 쓰겟단소리~
5번틀리면 로그인 실패 횟수추가 메세지 출력
올바르다면 로그인 오나료 출력하고 종료
암호는 프로그래밍

암호가 틀리면 특정 변수를 더하는데 5회가 되면 횟수초과! 출력하면 될듯?
특정변수를 세간에선 상태변수라함


암호 입력받는거 -> pw

암호 실패하면 더해지는 횟수(상태변수) -> checkPw

정답 압호 -> goodPw = programming

'''
goodPw = "programming"
checkPw = 0

while checkPw < 5:
    pw = input("관리자 암호 입력: ")
    if pw == goodPw:
        print("로그인 완료")
        break
    else:
        checkPw += 1
        print("암호 다시 확인")

if checkPw == 5:
    print("로그인 실패, 횟수 초과!!")






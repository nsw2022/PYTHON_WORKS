'''
 사용자가 숫자 2개를 입력하고 연산자를 선택하면
 연산결과가 출력되는 프로그램을 함수를 이용해서 만드시오
'''

# function(함수)
'''
승하쿤 너가 얼마나 아는지 몰라서 간략하게 적어줄게
파이썬에서는 함수를 데피니션! 정의하다라는 쪽에서 영감을 얻었나봐
def 함수명(사용할 변수):
    함수내용....
    
이렇게 사용해 참고로 함수명 옆에 괄호는 파라미터라고 불러
함수를 사용하는 법은 간단해 그냥

함수명(사용할 변수) 이런식으로 쓰면됨
'''
def num():
    # 숫자 입력 받기
    n1 = int(input("숫자를 입력하세요: "))
    s1 = input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈: ")
    n2 = int(input("숫자를 입력하세요: "))

    # 연산 결과 계산
    if s1 == '1':
        print("덧셈 결과: {}".format(n1 + n2))
    elif s1 == '2':
        print("뺄셈 결과: {}".format(n1 - n2))
    elif s1 == '3':
        print("곱셈 결과: {}".format(n1 * n2))
    elif s1 == '4':
        print("나눗셈 결과: {}".format(n1 / n2))

def main():
    # num 함수 호출
    num()

# main 함수 실행 학교에서 말한 main함수가 저런느낌인지
#if __name__ == "__main__": <-진짜찐 메인인데 요정도까지 쓸지모르겠어
main()
# 만약 둘다아니라면 걍 num()만써도되 위에 def main 지우고 이해안감 말혀
#num()


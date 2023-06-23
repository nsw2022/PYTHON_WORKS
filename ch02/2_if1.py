# 조건문
# 삼항연산자 확인 - 조건 연산자 사용안함
# if문의(:) 코드 블럭을 의미하고
# 다음줄에서 4칸 들여쓰기(indent-인덴트) 되어야 함
'''
result = (10 > -10)? 'T': 'F'
print(result)
'''
'''
x = 10
y = -10

if x > y:
    print('T')
else:
    print('F')
'''

# 자동차 주행 제한속도가 50Km 이상이면 "안전속도 위반!"
'''
limit_speed = int(input('속도입력'))
if limit_speed >= 50:
    print("안전속도 위반 !! 과태료 10만원 부과대상")
print("현재 속도는 "+str(limit_speed))
'''
# 자동차 주행 제한속도가 50km 이상이면 "안전속도 위반!! 과태료 10만원 부가대상"
# 50km 미만이면 "안전 속도 준수"를 출력하는 프로그램
limit_speed = int(input('속도입력'))
if limit_speed < 50:
    print("안전 속도 준수")
else:
    print("안전속도 위반 !! 과태료 10만원 부과대상")
print("현재 속도는 "+str(limit_speed))

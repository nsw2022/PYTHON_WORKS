# 다중 조건문 - if ~ elif ~ else
# 놀이공원 입장료 계산
# 미취학 8세미만 초등학색 14세 미만 중고등 20세 미만 나머지 일반인

print('♣ 놀이공원 입장을 환영합니다♣')
age=int(input('나이입력 : '))
charge = 0

print('♣ 놀이공원 입장을 환영합니다♣')
age=int(input('나이입력 : '))
charge = 0

if age < 0:
    print('사람이 아니시군요')
elif age >= 1 and age<8:
    print('미취학 아동입니다.')
    charge = 1000
elif age >= 8 and age < 14:
    print('초등학생입니다.')
    charge = 2000
elif age<20:
    print('중,고등학생입니다.')
    charge = 3000
else:
    print('일반인입니다.')
    charge = 4000

# 메인 영역
if age >= 0:
    print('입장료는 '+str(charge) +"원 입니다.")



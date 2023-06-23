# bmi.py
# 체질량 지수 = 몸무게 / 키(m)의 제곱
# 키 = 키 / 100 -> cm 으로 환산
# 거듭제곱 5 ** 3 = 5x5x5
name = input("이름을 입력하세요 : ")
weight = float(input("몸무게를 입력하세요 : "))
heigth = float(input("키(cm)를 입력하세요 : "))
heigth = heigth / 100


bmi = weight / (heigth ** 2)

print(f'{name}님의 bmi는 {bmi:.2f}입니다') # f 스트링 방식
# % 포맷 방식 : %s - 문자, %f - 실수, %d - 정수
print("%s님의 bmi는 %.2f입니다" %(name, bmi) ) 

if bmi < 20:
    print('저체중입니다.')
elif bmi >= 20 and bmi < 24:
    print('정상입니다.')
elif bmi >= 24 and bmi < 30:
    print('과체중입니다.')
else:
    print('비만')



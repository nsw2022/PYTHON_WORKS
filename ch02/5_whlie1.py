# while 반복문
# 'hello'를 열번 출력
# i++는 사용할 수 없음
'''
i = 0
while i < 10:
    print('hello~')
    i += 1
'''

'''
# 1부터 10까지 더하기
i = 0
sum_V=0
while i < 10:
    i += 1
    sum_V = sum_V + i
    print("i=",i,"sum_V =",sum_V)
print(f' 합계 : {sum_V}')
'''

'''
# 반복조건문 (break)
i = 0
sum_V=0
while True:
    i += 1
    if i > 10:
        break
    sum_V += i
    print(f'합계 : {sum_V} i:{i}')
print(f'여기는 while문 밖 {sum_V,i}')
''' 
# 무한반복 제어
key = input('반복을 계속 할까요?(y/n)\n')
while True:
    if key == 'y':
        print('반복을 계속합니다')
        key = input('반복을 계속 할까요?(y/n)\n')
    elif key=='n':
        print('반복을 중단합니다')
        break
    else:
        print('정상답변이 아닙니다')
        key = input('반복을 계속 할까요?(y/n)\n')


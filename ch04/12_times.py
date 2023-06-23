# 1~ 100 까지 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의하시오.

def t_basu(x):
    count = 0
    print('{}의 배수'.format(x), end=' ')
    for x in range(1, 101):
        if x % 3 == 0:
            print(x, end=' ')
            count += 1
    print()
    print("배수의 개수:", count)

t_basu(3)


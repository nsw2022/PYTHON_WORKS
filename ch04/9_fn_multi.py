# 두 수를 매개 변수 전달
# 1. 서로 같으면 곱하고
# 2. 두수가 서로 다르면 더하는 함수

def fn_multi(x, y):
    if x == y:
        return x * y
    elif x != y:
        return x + y


result = fn_multi(5, 5)
result2 = fn_multi(5, 10)

print(result)
print(result2)


# 구구단 4단 출력
# dan = 4
# for i in range(1, 10):
#     print(f'{dan} X {i} = {i*dan}')

# 함수를 정의해서 구구단 출력
def gugu_dan(x):
    dan = x
    for i in range(1, 10):
        print(f'{dan} X {i} = {i * dan}')

gugu_dan(9)


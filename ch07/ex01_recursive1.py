# 재귀 함수
# 종료 조건을 항상 명시(if ~ else)
# 1부터 5까지 곱하기

import time

start = time.time()
def getgob(n):
    gob = 1
    for i in range(1, n+1):
        gob *= i

    return gob
end = time.time()
print(getgob(1000))
print(f'{end-start}')
# 재귀 함수
# 5 * 4(5-1) * 3(4-1) * 2(3-1) * 1(2-1) = 5! (팩토리얄, 계승)
# 패턴을 코드화
start = time.time()
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)

# n = 5 조건식 만남 1아니면 - 1 n=4
# n = 4 조건식 만남 1아니면 - 1 n=3
# n = 3 조건식 만남 1아니면 - 1 n=2
# n = 2 조건식 만남 1아니면 - 1 n=1
# n = 1 조건식 만남 1아니면 - 1 n=1 임으로 return은 1

#  end = time.time()

print(facto(100))
print(f'{end-start:2f}')
# getgob() 호출
# print(getgob(5))

def sos(n):
    print("Help me")
    # 종료 조건
    if n == 1:
        return ""
    else:
        return sos(n-1)

# sos(3)




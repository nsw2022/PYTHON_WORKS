# 함수 - function, method(메서드)
import time


# 1 ~ 10 까지의 출력
# for i in range(1, 11):
#     print(i)

# 1부터 n까지 출력하는 함수
def get_num(n):

    for i in range(1, n+1):
        print(i, end=' ')

get_num(20)

# 계산 복잡도 - 곱셈, 덧셈, 나눗셈 - 3번 O(n)
# 1부터 n까지 합계
start = time.time()
def get_sum(n):
    sum_v=0
    for i in range(1, n+1):
        sum_v += i
    return sum_v


# 계산 복잡도 - 곱셈, 덧셈, 나눗셈 - 3번 0(1)
start = time.time()
def get_sum2(n):
    sum_v = (n*(n+1))//2
    return sum_v

if __name__ == "__main__":
    print(f'합계 : {get_sum(10)}')  # error 너무걸림
    end = time.time()
    print(f'소요시간 : {end - start}')

    print(f'합계 : {get_sum2(10)}') # 위랑 달리 바로 연산됨
    end = time.time()
    print(f'소요시간 : {end-start}')







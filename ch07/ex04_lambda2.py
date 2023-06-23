# map(), filter()
# 리스트를 매개변수로 전달
v = [1, 2, 3, 4]
# lambda 함수와 map() 사용
# times = lambda x : 3 * x
def times(x):
    return 3 * x
result = map(times, v)
# map(함수, 리스트)
print(list(result))
# result = map(times2, v)

# filter()와 lambda 사용
# 음의 정수를 출력
def negative(n):
    return n < 0

li = [-5, 1, 2, -11, 76]

# negative = lambda x : x<0
value = filter(negative, li)
print(list(value))
# 리스트 합계, 최대값, 최솟값
#print(sum(v))
#print(max(v))
#print(min(v))

# 리스트의 합계 연산하는 함수 정의 - get_sum()
# 매개변수가 리스트

v = [3, 2, 5, 1, 4]
def get_sum(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v

# 리스트의 평군을 구하는 함수 정의 - get_avg()
def get_avg(a):
    sum_v=0
    for i in a:
        sum_v += i
    return sum_v/len(a)
def get_max(a):
    max_v = a[0]
    for i in a:
        if max_v < i:
            max_v = i
    return max_v
def get_min(a):
    min_v = a[0]
    for i in v:
        if min_v > i:
            min_v = i
    return min_v
"""
min_v = 3 i=3,  3 > 3  False
          i=2,  3 > 2  True    
min_v = 2 i=5,  2 > 5  False
          i=1,  2 > 1  True
min_v = 1 i=4,  1 > 4  False
"""
print("합계 :", get_sum(v))
print("평균 :", get_avg(v))
print("최댓값 :", get_max(v))
print("최솟값 :", get_min(v))


'''
# 입력
v = [1, 2, 3, 4]
# 합계
sum_v = 0
for i in v:
    sum_v += i
# 출력
print(sum_v)
'''
# # 최대값
# v = [1,2,9,7,5]
# max_v = v[0]
#
# # 연산
# for i in v:
#     if max_v < i:
#         max_v = i
#
# # 출력
# print(max_v)

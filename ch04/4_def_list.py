# 매개변수가 리스트인 함수
# 리스트 복사를 함수로 이용
def get_list(a): # v라는 변수 a와 같다
    a2 = []
    for i in a:
        a2.append(2*i)
    return a2
    

v = [1,2,3,4]
print(get_list(v)) #[1,2,3,4]


# 리스트 a
a=[1,2,3,4,5]

# 5를 삭제
a.pop()

print(a)

# a 리스트의 합계와 평균
sum_v = 0

for i in a:
    sum_v += i

avg_v = sum_v / len(a) # 평균
print(f'[a]의 합계 : {sum_v}')
print(f'[a]의 평균 : {avg_v}')

# 내장함수
print(f'sum = {sum(a)}')

b = (1, 2, 3, 4) #튜플
print(sum(b))

# 성적 처리
# 학생 5명의 국어 점수 - 합계, 평균, 최고점수, 최저점수
A = [70, 80, 50, 60, 90]
# for ~ in
for i in A:
    print(i, end=' ')
print()
'''
for i in range(1,6):
    print(i)
'''

# 개수
count = len(A)

# for ~ in range() - 인덱스 방식
'''
for i in range(0,len(A)):
    print(A[i], end=' ')
'''
# print(count)

# 합계
sum_v=0

for i in A:
    sum_v = sum_v + i
print(f'합계:{sum_v}')

# 평균 / 개수
avg = sum_v / count
print(f'평균 : {avg:.1f}')

# 최고점수
# 내장 함수 - sum(), max()
print(sum(A))
print(max(A))
print()
for i in range(0,len(A)):
    if(A[0] < A[i]):
        A[0]=A[i]
print(A[0])

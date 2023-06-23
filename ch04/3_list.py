# 리스트
a=[1,2,3,4]


# 리스트에 5를 추가
a.append(5)

# 5를삭제
a.pop()

print(a)

# 리스트 복사
a2 = [] # a2는 빈리스트
'''
a2 = a # 직접복사
print(a2)
'''

# for ~ in 로 복사
'''
for i in a:
    a2.append(i)
print(a2)
'''

# 3의 배수로 복사
for i in a:
    a2.append(i*3)
print(a2)

# a 리스트에서 홀수만 저장
a3=[]
for i in a:
    #if i%2 != 0:
    if i%2 == 1:
        a3.append(i)
print(a3)


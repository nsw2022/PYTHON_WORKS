# 정렬 - 1. 내장함수 2. 반복조건문
# 리스트의 매서드 sort(), reverse()

'''
a = [1, 5, 4, 15, 6]
a.reverse() # 거꾸로
print(a)

a.sort()
print(a)

a.sort(reverse=True) # 내림차순
print(a)
'''
# 2. 반복 조건문(중첩 for)
# 정렬 알고리즘 - 버블정렬
a = [60, 5, 33, 12, 97, 24]
n = len(a)
for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a[j], a[j+1])

'''
i=0(1행) a[0] a[1] True  5 60 33 12 97 24  
   (2행) a[1] a[2] True  5 33 60 12 97 24   
   (3행) a[2] a[3] Ture  5 33 12 60 97 24
   (4행) a[3] a[4] False 5 33 12 60 97 24
   (5행) a[4] a[5] True  5 33 12 60 24 97   
   
i=1(1행) a[0] a[1] False 5 33 12 60 24 97
   (2행) a[1] a[2] True  5 12 33 60 24 97 
   (3행) a[2] a[3] False 5 12 33 60 24 97
   (4행) a[3] a[4] True  5 12 33 24 60 97
   (5행) a[4] a[5] False 5 12 33 24 60 97
          
i=2(3행) a[2] a[3] True  5 12 24 33 60 97 
      
'''
print(a)



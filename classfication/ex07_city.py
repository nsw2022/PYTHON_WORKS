class City:
    # 클래스 리스트
    a = ['Seoul', 'Incheon', 'Deajon', 'Jeju']

str1 = ""
for i in City.a: # 클래스 이름으로 직접 접근
    str1 += i[0]
print(str1)

# for ~ in
laguages = ['python', 'C', 'Java','JavaScript']
'''
for lang in laguages:
    if lang in ['python', 'JavaScript']:
        print(f'{lang} need interpreter') # 인터프리터
    else:
        print(f'{lang} need complier') # 컴파일러
'''
'''
# 구구단 출력

for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print()
'''
'''
dan = input("단을 입력해주세요")
result = ""

for i in range(1,10):
    current_val= f'{dan} x {i} = {dan*i}\n'
    result= result+current_val
'''


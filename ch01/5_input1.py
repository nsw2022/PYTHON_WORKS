# 입력처리 - input()함수
#방법1
"""
print("이름을 입력해주세요")
name=input() # 문자를 입력할 수 있음
print(name + "님 환영합니다")
"""

#방법2
'''
name = input("이름을 입력해주세요\n")
print(name + "님 환영합니다")
'''

# 입력받은 수는 문자열임 - > 정수로 변환 int()함수 사용
"""
number = int(input("숫자를 입력하세요(1~10)\n"))
print(number * 2)
"""

# 두 수를 입력받아서 합을 계산하기
'''
x = int(input("첫째 수 입력"))
y = int(input("둘째 수 입력"))
sum_v = x + y
print(sum_v)
'''

# 나이 계산 프로그램
# 나이 = 현재년도 - 출생년도 + 1
'''
current_year = 2023
birth_year = int(input("태어난 연도를 입력하세요\n"))
age = current_year - birth_year + 1
print(str(birth_year)+"에 태어나신분의 현재나이는",age)
'''

# 사각형의 넓이를 계산하는 프로그램을 작성
# 사각형의 넓이 = 가로 x 세로
width=int(input('가로의 길이: '))
hegint=int(input('세로의 길이: '))
print('가로 길이 : '+str(width)+'cm')
print('세로 길이 : '+str(hegint)+'cm')
print('면적 : '+str(width*hegint)+'cm\n')

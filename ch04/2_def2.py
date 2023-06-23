# 사각형 넓이 계산 함수
# 함수이름 - rec_area()
# 사각형 넓이 공식 가로 X 세로
# 삼각형 넓이 공식 (밑변 X 높이)/2 = 넓이
# 함수이름 - calc_area(), tri_area()
'''
def calc_area(w,h):
    area = w * h
    return area

result = calc_area(4,3)
print(f'사각형의 면적: {result}')
'''


'''
def calc_area(x,y):
    return x*y
'''


def calc_area(x, y):
    area = x * y
    return area

x = int(input('가로의 길이 입력: '))
y = int(input('세로의 길이 입력: '))
print('사각형의 면적: {}'.format(calc_area(x, y)))



# 삼각형. 밑변 - 4, 높이 - 5
def tri_area(x,y):
    return (x*y)/2
print('삼각형의 넓이 :',tri_area(4,5))

# 정사각형의 면적
size = int(input("숫자를 입력"))
area = size * size
print(area)

def calc_size(n):
    area = n * n
    return area
print(calc_size(100))


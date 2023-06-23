# 파라미터 정리
# =, *, **kargs
# 번외 테스트에는 print(*p)를 다뤘다 한개붙히면 리스트형태의 값만 보여주는거 같다

# =키워드
# 함수 호출시 매개변수를 생략하면 기본값 출력
def print_string(text, count=1):
    for i in range(count):
        print(text)

print_string("ㅎㅇ")
print_string("ㅎㅇㅎㅇ",2)

# *키워드
# 가변 매개 변수 - 변수 앞에 '*'를 붙임
def calc_avg(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg
print(f'평균을 구해 드립니다 : {calc_avg(10, 20, 30)}')

def saveDic(**kargs):
    print(kargs)

saveDic(a=1, b=2, c=3)

# ※ 번외 테스트
p = ['a','b','c']
print(*p)



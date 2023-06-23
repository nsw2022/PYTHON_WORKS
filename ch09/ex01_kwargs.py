# 키워드 매개변수
# 딕셔너리 형의 자료로 만들어짐
def print_kw(**kwargs):
    print(kwargs)



# 호출
print_kw(name='진') # {name='진'}
print_kw(age = 30, gender='여자')


# 가변 매개 변수 - 변수 앞에 '*'를 붙임
def calc_avg(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg
print(f'평균을 구해 드립니다 : {calc_avg(10, 20, 30)}')
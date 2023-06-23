import ex01_method as met
from ex01_method import get_sum2

# 모듈 이용법
# import ex01_method as met 인 경우
# get_sum()호출
val = met.get_sum2(10)
print(val)

# from ex01_method import get_sum2 인경우

val2 = get_sum2(10)
print(val2)

met.get_num(10)
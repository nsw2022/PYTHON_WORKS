import datetime
import calendar as cal

cal.prcal(2023) # 2023년 달력
cal.prmonth(2023,4) # 2023 4월 달력

# 나이가 100세 되는 해의 연도 계산하기
# 현재년도 + (100 - age)

# age = int(input('나이입력 : '))
now = datetime.date.today()

# result = now.year + (100 - age + 1 )
# print(f'100세 되는 해는 {result}년 입니다.')

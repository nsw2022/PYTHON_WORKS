# 로또 복권 추첨 프로그램
# 1 ~ 45 까지 수를 6개 랜덤수로 저장
import random

lotto = []
while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
lotto.sort(reverse=True)
print(lotto)
'''
# for에서 안됨
for i in range(0, 6):
    num = random.randint(1, 6)
    if num not in lotto:
        lotto.append(num)
    else:
        num = random.randint(1, 6)
'''


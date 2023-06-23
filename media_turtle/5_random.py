# random 모듈
# 숫자(정수)를 랜덤 추출 - 1 ~ 10 random.randint(1, 10)
# 리스트에서 요소 추출 - random.choice()
import random

# 1 ~ 10 중 무작위로 추출
num = random.randint(1, 10)
print(num)

# 주사위 만들기
dice = random.randint(1, 6)
print(dice)

# 주사위 10번 던지기
for i in range(10):
    dice = random.randint(1, 6)
    print(dice)

# 리스트에서 랜덤하게 값을 추출하기
과일 = ['딸기','수박','참외','사과']
# print(과일[0])
print(random.choice(과일))

# 주사위 2개를 10번 던지기
# 두눈의 합이 7이면 "Seven Thrown!!",
# 11 이면 "Eleven Thrown!!"
# 같으면 "Double Thrown
print()

count = 0
s_count = 0
e_count = 0

for i in range(10):

    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1==d2:
        count+=1
        print("Double Thrown\nd1: {} d2: {}\n".format(d1,d2))

    elif d1+d2 == 7:
        s_count += 1
        print("Seven Thrown!!\nd1: {} d2: {}\n".format(d1,d2))

    elif d2+d2 == 11:
        e_count += 1
        print("Eleven Thrown!! \nd1: {} d2: {}\n".format(d1,d2))

    else:
        print(f'd1:값 {d1} d2:값{d2}\n')

print(f'Eleven: {e_count}')
print(f'Seven: {s_count}')
print(f'Double: {count}')
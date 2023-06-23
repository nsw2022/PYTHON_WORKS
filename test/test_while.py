'''
아래의 출력을 보이는 프로그램을 작성해보자.
 *
 o *
 o o *
 o o o *
 o o o o *
'''
'''
i = 1
while i <= 5:
    j = 1
    while j <= i - 1:
        print("o", end=' ')
        j += 1
    print("*")
    i += 1
'''

'''
문제 6.
입력값들의 분포를 시각적으로 볼 수 있는 히스토그램을 만드는 프로그램을 작성하시오.
이 프로그램은 1부터 100이하의 정수 10개를 읽어야 하고, 1-10,11-20 등의 범위에 드는
값들의 횟수를 아래와 같이 출력하여야 한다.

  1 - 10 : ****
 11 - 20 : **
 21 - 30 : *
 31 - 40 : **
 ..........
 ..........
 
 10 1
 20 2
 22 2
 
 
'''
print("정수 10개 입력")
print("문자열 입력하면 3대가 대머리")
intput1 = int(input("정수1: "))
intput2 = int(input("정수2: "))
intput3 = int(input("정수3: "))
intput4 = int(input("정수4: "))
intput5 = int(input("정수5: "))
intput6 = int(input("정수6: "))
intput7 = int(input("정수7: "))
intput8 = int(input("정수8: "))
intput9 = int(input("정수9: "))
intput10 = int(input("정수10: "))

arr=[]
test_10 = []
test_20 = []
test_30 = []
test_40 = []
test_50 = []
test_60 = []
test_70 = []
test_80 = []
test_90 = []
test_100 = []

arr.append(intput1)
arr.append(intput2)
arr.append(intput3)
arr.append(intput4)
arr.append(intput5)
arr.append(intput6)
arr.append(intput7)
arr.append(intput8)
arr.append(intput9)
arr.append(intput10)

for i in arr:
    if i  <11: # 1~10
        test_10.append("*")

    elif i  <21: # 11~20
        test_20.append("*")

    elif i  <31: # ~30
        test_30.append("*")

    elif i  <41: # ~40
        test_40.append("*")

    elif i  <51: # ~50
        test_50.append("*")

    elif i  <61: # ~60
        test_60.append("*")

    elif i <71: # ~70
        test_70.append("*")

    elif i < 81: # ~80
        test_80.append("*")

    elif i < 91: # ~90
        test_90.append("*")

    elif i < 101: # ~100
        test_100.append("*")

    else:
        print("뭔가 잘못 입력하셨군요")
print(" 1 - 10  : ", *test_10)
print("11 - 20  : ", *test_20)
print("21 - 30  : ", *test_30)
print("31 - 40  : ", *test_40)
print("41 - 50  : ", *test_50)
print("51 - 60  : ", *test_60)
print("61 - 70  : ", *test_70)
print("71 - 80  : ", *test_80)
print("81 - 90  : ", *test_90)
print("91 - 100 : ", *test_100)

len(test_10)
len(test_20)
len(test_30)
len(test_40)
len(test_50)
len(test_60)
len(test_70)
len(test_80)
len(test_100)

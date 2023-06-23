# 다중 예외 처리
try:
    data = [15,20,99,8,0]
    x = input("정수 입력(0~4까지 입력) ")
    num = int(x)
    print(data[num])
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
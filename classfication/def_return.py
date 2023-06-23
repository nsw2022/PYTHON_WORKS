def one_up():
    x = 0
    x = x + 1
    return x

def square(x): # 제곱수를 계산
    val = x * x
    return val
def add(x,y): # 두수를 더하는 함수
    val = x + y
    return val
if __name__ == "__main__":
    print(square(2))#4
    result = square(3)
    print(result)#9
    #add함수호출
    print(add(3,4))#7

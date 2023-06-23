# try ~ except~ finally

def devide(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("여기는 반드시 수행되는 구간")
# devide(2,4)
devide(4,2)

# Calculator 클래스

class Calculator:
    def __init__(self):
        self.x = 0 # 멤버 변수 X를 0을 할당

    # 매개 변수 y값 더하기
    def add(self, y):
        self.x = self.x + y
        return self.x

    # 매개 변수 y값 뺴기
    def sub(self, y):
        self.x = self.x - y
        return self.x

if __name__ == "__main__":
    cal1 = Calculator()
    print(cal1.add(10))  # 10
    print(cal1.sub(4))  # 10-4=6

    cal2 = Calculator()
    print(cal2.add(10.1))
    print(cal2.sub(2.5))

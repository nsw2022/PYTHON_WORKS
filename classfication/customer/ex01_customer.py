# Customer 클래스 생성
# 멤버변수 - 고객아이디, 이름, 등급, 보너스포인트, 보너스 적립율
# 멤버 함수 - get() set() 함수로 작성
# 보너스 포인트 = 가격 * 보너스 적립률
class Customer:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname
        self.cgrade = "SILVER"
        self.bonus_point = 0
        self.bonus_ratio = 0.01 # 1%

    def __str__(self):
        return f'{self.cname}님의 등급은 {self.cgrade}이고, ' \
               f'보너스 포인트는 {self.bonus_point}점 입니다.'

    def calc_price(self, price):

    # self.bonus_point = price * self.bonus_ratio
    # 보너스 포인트 += 보너스 포인트 ( 가격 X 보너스 할인율 )
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def getname(self):
        return self.cname

if __name__ == "__main__":
    c1 = Customer(1001, "정국")
    # print(c1.cname, c1.cid)
    price1 = 10000
    cost1 = c1.calc_price(price1)
    print(f'{c1.getname()}님의 구매 비용은 {cost1}입니다.')
    print(c1)

    c2 = Customer(1002, "슈가")
    price2 = 20000
    cost2 = c2.calc_price(price2)
    print(f'{c2.getname()}님의 구매 비용은 {cost2}입니다.')
    print(c2)



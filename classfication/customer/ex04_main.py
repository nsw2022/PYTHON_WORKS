from classfication.customer.ex01_customer import Customer
from classfication.customer.ex02_goldcustomer import GoldCustomer
from classfication.customer.ex03_vipcustomer import VIPCustomer

# 객체 리스트
# Customer - 2명, GoldCustomer -2명, Vip - 1명
customer = [
    Customer(101,'놀부'),
    Customer(102,'팥쥐'),
    GoldCustomer(201,'흥부'),
    GoldCustomer(202, '콩쥐'),
    VIPCustomer(301, "심청", 777)
]
print("*** 구매 가격과 보너스 포인트 계산 ***")
for cus in customer:
    price = 10000
    cost = cus.calc_price(price)
    # print(f'{cus.getname()}님의 지불 금액은 {cost}입니다')
    print(cus.getname() + "님의 지불 금액은 "+format(cost, ',d') + "원입니다.")
print("********** 고객 정보 출력 **********")
for i in customer:
    print(i)

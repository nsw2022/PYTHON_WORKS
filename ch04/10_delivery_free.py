# 배송비 계산
# 주문 상품 가격이 2만원 미만이면 배송비 포함하고,
# 아니면 배송비를 포함하지 않는 프로그램
"""
price = 15000
delivery_free = 2500

if price < 20000:
    price = price + delivery_free
else:
    price

print(price)
"""


def get_price(unit_price, num):  # 매개변수 - 가격, 수량
    delivery_free = 2500
    price = unit_price * num
    if price < 20000:
        price = price + delivery_free
        return price
    else:
        return price


orders1 = get_price(15000, 2)
orders2 = get_price(5000, 3)
print(f'주문가격은 {orders1}원 입니다')
print(f'주문가격은 {orders2}원 입니다')

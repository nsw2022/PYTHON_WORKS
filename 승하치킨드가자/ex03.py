'''
건덕이가 두개의 주사위를 동시에 던지는 실험한다
1~6까지의 수가있고 3번던지는 실험
각각 랜덤
각각 값구하기
그리고 둘의 합 구하기

3번 반복 각각랜덤 으로 파.훼.
보면 누적합계있음
sum_a=0 하고 각각값
sum_a+=a
sum_b+=b 해달라하셈

모르는거있음 연락혀
'''
import random
sum_a=0
sum_b=0
for i in range(3):
    a=random.randint(1,6)
    b=random.randint(1,6)
    sum_a += a
    sum_b += b
    print("{}번째 A의 주사위 숫자는 {}입니다".format(i+1,a))# 반목문이 0부터 시작이라 i+1해줌
    print("{}번째 B의 주사위 숫자는 {}입니다".format(i+1,b))

#print(sum_a) a총값
#print(sum_b) b총값
print("모든 눈의 수의 합은 {}입니다".format(sum_a+sum_b))
# 가위 바위 보 게임 만들기
"""
게임 방법
1. 당신은(you) 가위, 바위, 보 중 하나를 입력한다.
2. 컴퓨터(com)는 가위 바위 보 중 하나를 랜덤 생성한다
3. 결과 출력은 무승부, 패, 승 이다
4. 잘못 입력한 경우 "잘못된 입렵입니다"

무한반복돌리고
com 이 각각의 경우일때를 다중if로 구현

"""

import random

com = ['가위', '바위', '보']
win_list = random.choice(com)
print(win_list)
count = 0
while True:
    you = input("가위바위보 중 입력해주세요: ")

    if you not in com:
        print("잘못된 입력입니다. 다시 입력해주세요")
        continue

    if you == win_list:
        print("결과: 무승부")
        count += 1
    elif (you == '가위' and win_list == '보') or (you == '바위' and win_list == '가위') or (you == '보' and win_list == '바위'):
        print("결과: 승리")
        print(f'{count}번만에 승리하셨습니다!!')
        break
    else:
        print("결과: 패")
        print("이길때 까지 한다 크킄")
        count += 1


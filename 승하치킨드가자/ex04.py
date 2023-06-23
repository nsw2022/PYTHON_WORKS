import random

rps_dic = {1: "가위", 2: "바위", 3: "보"}
match_table = {"가위": "보", "바위": "가위", "보": "바위"}#key:value 형태
score = [0, 0, 0] # 승 무 패로 각각 index에 넣어줬음

win_count = 0 # 이긴거 카운트
lose_count = 0  # 진거 카운트

userName = input("도전자 이름: ")

for i in range(3):
    you = input("가위, 바위, 보 중 하나 입력: ")

    computer = random.choice(list(match_table.keys()))
    #print("컴퓨터 선택:", computer)

    if match_table[you] == computer:
        print("이겼습니다.")
        score[0] += 1
        win_count += 1
    elif match_table[computer] == you:
        print("졌습니다.")
        score[1] += 1
        lose_count += 1
    else:
        print("비겼습니다.")
        score[2] += 1

print("{}: {}승 {}무 {}패".format(userName, win_count, score[2], lose_count))





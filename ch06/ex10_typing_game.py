# 영어 타자 게임
import random
import time

try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split()
    n = 1 # 문제번호
    input("[타자게임] 준비되면 엔터\n")
    start = time.time()
    while n <= 10:
        question = random.choice(data)
        print(f'-문제 {n}')
        print(question)
        user = input()
        if user == question:
            print("통과!")
            n+=1
        elif user != question:
            print("오타! 다시 도전!")
    end = time.time()
    print(f'게임 소요 시간 : {end-start:.2f}')

except:
    print("못읽어옴 ㅋ")
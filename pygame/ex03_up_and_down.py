# 숫자 추측게임
'''
게임 방법
게임이 시작되면 컴퓨터가 난수(정답)을 생성한다
- 사용자의 추측값이 정답과 같으면 정답
  추측값이 정답보다크면 "너무 커요"
  추측값이 정답보다작으면 "너무작아요" 출력
'''
import random
min = 1
max = 100
com = random.randint(min, max)
print(com)
count=1
user_count=10
while True:
    try:
        print("남은목숨", user_count)
        print()
        guess = int( input(f"맞혀보세요[{count}회]({min}~{max})>"))

        if guess > 100 or guess < 1:
            print("입력범위 초과 제한수를 다시봐주세요")

        elif com == guess:
            print("정답")
            user_count=user_count * 10
            print(f"점수 : {user_count}")
            break

        elif com >= guess:
            print("너무작아요")
            count += 1
            if guess >= min:  # 목숨 감소 조건 추가
                user_count -= 1
            min = guess

        elif com <= guess:
            print("너무 커요")
            count += 1
            if guess <= max:  # 목숨 감소 조건 추가
                user_count -= 1
            max = guess


        if user_count == 0:
            print()
            print("이걸못맞히네 까비이 GG")
            break
    except:
        print("문자입력노노")

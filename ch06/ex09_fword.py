# 영어 단어장 만들기
import random

word = ['ant', 'bear', 'chicken', 'deer', 'fox', 'elephant',
        'horse', 'lion', 'monkey', 'penguin']
try:
    with open("./output/word.txt", 'w') as f:
        for i in word:
            if i == word[-1]:
                f.write(i)
            else:
                f.write(i + ' ')

except:
    print("파일 쓸수 없었다")

# 파일 읽기
try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split() # 공백문자로 구분 - 리스트로 변환
        word = random.choice(data) # 단어 1개 랜덤 추출
        print(word)
except:
    print("파일 읽을수없다")

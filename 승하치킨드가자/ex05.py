# questions = [
#     {"question": "3+2", "answer": 5, "score": 3},
#     {"question": "5÷2 (5나누기2)의 몫", "answer": 2, "score": 5},
#     # ㄷ 한자키 ÷
#     {"question": "10-2", "answer": 8, "score": 3},
#     {"question": "10²(10의 제곱)+2", "answer": 200, "score": 5},
#     # ㅊ 한자키 제곱
#     {"question": "1-(10÷4의 나머지)", "answer": -1, "score": 5},
#     {"question": "2⁴ (2의4승)", "answer": 16, "score": 3},
#     {"question": "4÷2", "answer": 2, "score": 3},
# ]
questions = [
    {"question": "3+2", "answer": 5, "score": 3},
    {"question": "5÷2 (5나누기2)의 몫", "answer": 2, "score": 5},
]
correct_count = 0
incorrect_count = 0
total_score = 0


for i, question in enumerate(questions):
    q_text = question["question"]
    answer = question["answer"]
    score = question["score"]

    print("문제 {}:".format(i + 1))
    print(q_text)
    user_answer = input("정답을 입력하세요: ")
    if user_answer == str(answer):
        correct_count += 1
        total_score += score
    else:
        incorrect_count += 1

print("\n정답 개수: {}".format(correct_count))
print("오답 개수: {}".format(incorrect_count))
print("Total Score: {}".format(total_score))
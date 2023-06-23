# 주인공 거북이, 전체 stage(무대)
import turtle as t
import random
import time

# 주인공 거북이
t.setup(500, 500)
t.bgcolor('skyblue')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')
# 점수와 게임 스위치 변수
score = 0               # 게임 실행 점수 변수
playing = False         # 게임 실행 상태 변수

# 적 거북이
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 100)
# 두번째 거북이
te2 = t.Turtle()
te2.shape('turtle')
te2.color('black')
te2.up()
te2.goto(0, 200)
te2.shapesize(5, 5, 8)

# 먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)


def turn_right():
    t.setheading(0)


def turn_up():
    t.setheading(90)


def turn_left():
    t.setheading(180)


def turn_down():
    t.setheading(270)


def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()


def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home() # 주인공 거북이 위치


# 키조종
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")


def play():
    global score
    global playing
    # 적 거북이가 주인공 거북이쪽 보며 쫓아가기
    t.forward(18)
    if random.randint(1, 5) == 3:  # 3을 뽑을 확률은 20%
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)

    # 두번째 악당 거북이 설정
    te2.forward(100)
    te2.setheading(random.randint(-200, 200))

    # 주인공 거북이가 적 거북이에 닿으면 게임 종료
    if t.distance(te) < 12:
        text = "Score " + str(score)
        message("Game over", text)
        playing = False
        score = 0

    if t.distance(te2) < 90:
        text = "Score " + str(score)
        message("Game over", text)
        playing = False
        score = 0



    # 주인공 거북이가 먹이에 닿으면 점수가 올라감
    if t.distance(tf) < 16:
        score += 1
        t.clear()  # 이전 점수 지우기
        t.write(score, False, align="center", font=("", 20))  # 새로운 점수 출력
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        tf.goto(start_x, start_y)

    # 게임 실행 (0.1초 콜백)
    if playing:
        t.ontimer(play, -100)


t.mainloop()

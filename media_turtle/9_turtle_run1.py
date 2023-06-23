# turtle run 게임
import random
import turtle as t

# 적 거북이 생성
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)


# 먹이 생성
tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)

def trun_right():
    t.setheading(0)


def trun_up():
    t.setheading(90)


def trun_left():
    t.setheading(180)


def trun_down():
    t.setheading(270)

def play():
    score = 0
    # 적 거북이와 닿지 않으면 게임 유지
    # 적 거북이와 닿으면 게임 멈춤
    if t.distance(te) > 12:
        t.ontimer(play, 100)  # 0.1 초 간격 으로 계속 play 호출

    t.forward(10)
    te.forward(9)


    # 적 거북이가 주인공을 쫓아옴 t.pos() <= 거북이의 현재좌표
    # 적 거북이가 주인방향을 알아채는데 20% 확률로 적용
    if random.randint(1, 5) == 4:
        ang = te.towards(t.pos())
        te.setheading(ang)

    # 주인공 거북이가 먹이에 닿으면 새 위치에서 랜덤하게 나타냄
    if t.distance(tf) < 12:
        x = random.randint(-230,250)
        y = random.randint(-230,250)
        tf.goto(x,y)
        score += 1



# 주인공 거북이
t.shape("turtle")
t.setup(500,500)
t.bgcolor('orange')
t.color("white")
t.speed(0)
t.up()

t.onkeypress(trun_right, "Right")
t.onkeypress(trun_up, "Up")
t.onkeypress(trun_down, "Down")
t.onkeypress(trun_left, "Left")
t.listen()


play()

t.mainloop()
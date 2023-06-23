# 키보드로 거북이 조종하기
import turtle
import turtle as t

t.shape("turtle")
t.speed(0)

def trun_right():
    t.setheading(0)
    t.forward(10)

def trun_up():
    t.setheading(90)
    t.forward(10)

def trun_down():
    t.setheading(270)
    t.forward(10)

def trun_left():
    t.setheading(180)
    t.forward(10)

def clear():
    t.clear() # 화면지우기

t.onkeypress(trun_right, "Right")
t.onkeypress(trun_up, "Up")
t.onkeypress(trun_down, "Down")
t.onkeypress(trun_left, "Left")
t.onkeypress(clear,"Escape")
# t.onclick(turtle.goto,1)
t.listen() # 키가 작동하는걸 대기중


t.mainloop()
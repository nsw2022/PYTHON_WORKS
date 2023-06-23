# turtle 모듈
import turtle as t
from builtins import range

t.shape("turtle")
t.bgcolor("black")
t.color("green")
t.speed(0)

n = 4    # 변의 개수
d = 100  # 거리(크기)
# 각도 = 360 / 변의 개수

for i in range(4):
    t.forward(100)
    t.right(90)

t.color('blue')
t.shapesize(2)
for i in range(3):
    t.forward(100)
    t.left(120)

t.color('red')
t.pensize(3)
t.shapesize(3)
t.circle(50)  # 반지름이 50px인 원





t.mainloop()



# 다각형 그리기
import turtle as t

t.shape('turtle')
t.speed(0)
def polygon(n): # 매개변수 - 도형의 변의 개수
    for i in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d):
    for i in range(n):
        t.forward(50)
        t.left(360 / n)

polygon(3)
polygon(5)
for i in range(2):
    t.up()
    t.forward(100)
    t.down()

polygon2(3, 100)
polygon2(5, 100)

'''
for i in range(3):
    t.forward(100)
    t.left(120)

t.up() # 펜 올리기
t.left(90)
t.forward(150)
t.down() # 펜 내리기

for i in range(3):
    t.forward(100)
    t.left(120)
t.up()
t.left(90)
t.forward(250)
t.left(90)
t.forward(100)
t.down()

for i in range(4):
    t.forward(100)
    t.left(90)
'''

t.mainloop()
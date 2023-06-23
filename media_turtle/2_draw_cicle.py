# 원 그리기
import turtle as t

# t.shape("turtle")
# t.bgcolor("black")
# t.color("green")
# t.speed(00) # 1~10 숫자가 클수록 빠른데, 0이 가장 빠름
#
# n = 50
#
# for x in range(50):
#     t.left(10)
#     t.circle(80)


# 이쁜 모양

t.shape('turtle')
#t.speed('fastest')
t.speed(0)
for i in range(500):
	t.forward(i)
	t.right(91)


t.mainloop()

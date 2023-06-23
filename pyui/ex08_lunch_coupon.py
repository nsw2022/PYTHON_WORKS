# 쿠폰 추첨기 만들기
import random
from tkinter import *


namelist = [
    '이진성','노승우','박성호','권지혜','김은효',
    '이경철','성의석','이유진','유성길','한주훈',
    '강정형','김현우','이영준','안재훈','김민정',
    '유세현','유기은','오화룡','조은별','이가은'
]

def click():
    win_list = []
    '''
    구현 1
    while len(win_list) < 5:
        compare = random.choice(namelist)
        if compare not in win_list: # 중복제거
            win_list.append(compare) # win_list에 추가
    output.delete(0.0, END)
    # output.insert(END, win_list) # str로 출력요망
    for i in win_list:
        output.insert(END, i + ' ')
    print(win_list)
    # win_list.clear() <- 저는 구현당시 win_list를 함수 밖에 빼놓음
    '''

    # 구현2
    while len(win_list) < 5:
        idx = random.randint(0, 19)
        if idx not in win_list:
            win_list.append(idx)
    output.delete(0.0,END)
    for i in win_list:
        output.insert(END, namelist[i] + ' ')


window = Tk()
window.title("쿠폰 추첨기")
window.option_add('*font', '맑은고딕 14')

# 이미지 넣기 - PhotoImage
img = PhotoImage(file='./image/bronx.png')
lbl_img = Label(window)
lbl_img.config(image=img)
lbl_img.grid(row=0, column=0, sticky=W)

# 추첨 버튼
Button(window, text='추첨',command=click).grid(row=1, column=0, sticky=E)

# 이름 출력
output = Text(window, width=33, height=4, bg='yellow')
output.grid(row=2, column=0,sticky=W)

window.mainloop()
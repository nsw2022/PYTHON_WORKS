from tkinter import *

def select():
    try:
        word = entry.get()
        definition = dic[word]  # dic[key] = value
        output.delete(0.0, END)
        output.insert(END, definition)
    except KeyError:
        output.insert(END, "단어를 정의할 수 없습니다.")

def enter(event):
    word = entry.get()
    definition = dic[word]  # dic[key] = value
    output.delete(0.0, END)
    output.insert(END, definition)

root = Tk()
root.title("키이벤트 테스트")

lbl = Label(root)
lbl.config(text='단어를 입력 하고 엔터 키를 누르세요')
lbl.grid(row=0,column=0,sticky=W)

entry=Entry(root, width=20,bg='yellowgreen')
entry.grid(row=1,column=0,sticky=W)

btn = Button(root, command=select,text="제출")
btn.grid(row=2,column=0,sticky=W)

output = Text(root, width=80, height=10, bg='yellowgreen')
output.grid(row=3,column=0,sticky=W)


dic = {
    "html" : "하이퍼 텍스트 마크업 언어로 웹 페이지를 구상하는 언어이다.",
    "HTML" : "하이퍼 텍스트 마크업 언어로 웹 페이지를 구상하는 언어이다.",
    "css" : "웹 페이지를 구성하는 요소로 디자인을 담당하는 웹 기술이다.",
    "CSS" : "웹 페이지를 구성하는 요소로 디자인을 담당하는 웹 기술이다.",
    "함수" : "명령이나 기능을 수행하는 재사용 가능한 코드 조각이다."
}

root.bind('<Return>',enter)
root.mainloop()
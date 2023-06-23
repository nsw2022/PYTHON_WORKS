#!/usr/bin/env python
# coding: utf-8

# ## 로또 당첨 번호 가져오기

# In[19]:


import requests
from bs4 import BeautifulSoup

def loto_win():
    num = 1063
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(num)
    reponse = requests.get(url)
    # print(reponse.text)

    soup = BeautifulSoup(reponse.text,"html.parser")
    win_result=soup.select_one("div.win_result") # 태그이름.클래스이름

    # \n이 많은걸확인하여 리스트형태로 리턴
    win_list = win_result.text.split('\n')

    win_list = win_result.text.split('\n')[7:13]

    print('당첨번호')
    print(win_list)
    bonus_num = win_result.text.split("\n")[-4]
    print('보너스 번호')
    print(bonus_num)



# # 로또 당첨 앱 제작
# 

# In[5]:


import requests
from bs4 import BeautifulSoup
from tkinter import *

def loto_win():
    num = entry.get() # 입력박스에 입력된 값
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(num)
    reponse = requests.get(url)
    # print(reponse.text)

    soup = BeautifulSoup(reponse.text,"html.parser")
    win_result=soup.select_one("div.win_result") # 태그이름.클래스이름
    win_result.text
    # \n이 많은걸확인하여 리스트형태로 리턴
    win_list = win_result.text.split('\n')
    win_list
    win_list = win_result.text.split('\n')[7:13]
    win_list
    bonus_num = win_result.text.split("\n")[-4]
    
    
    # 풀력상자에 번호 출력
    output.delete(0.0, END)
    output.insert(END,f'당첨번호 : {win_list}\n보너스 번호 : {bonus_num}')

def enter(event):
    loto_win()

window = Tk()
window.title("로또 당첨 확인")

Label(window, text="당첨 회차 입력 : ").grid(row=0,column=0,sticky=W)
# 입력상자
entry=Entry(window, bg='yellow')
entry.grid(row=1, column=0,sticky=W)

btn=Button(window, text="당첨 번호 확인", command=loto_win)
btn.grid(row=2, column=0,sticky=W)

#출력상자
output = Text(window, bg='skyblue', width=50, height=5)
output.grid(row=3,column=0,sticky=W)

window.bind('<Return>',enter)
window.mainloop()


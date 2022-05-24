import tkinter
from tkinter import *

window = Tk()

window.title("word chain game")
window.geometry("1001x700+100+100")
window.resizable(False, False)
bg = PhotoImage(file='../img/full-background.png')
bg_label = Label(window, image = bg)
bg_label.place(x=0, y=0)

lock = PhotoImage(file='../img/lock.png')

b1 = Button(window, text= 'Room1', width=45, height=5, bg='white')
b1.place(x=140, y=100)

def btn_click1(event):
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
b1.bind('<Button-1>', btn_click1)

# def b1event():   입장 인원수에 맞게 숫자를 바꿔주는 함수
#     if(입장이 완료되면):
#         b1['text'] = "1/4"

b2 = Button(window, text='Room2', anchor='c', width=45, height=5, bg='white')
b2.place(x=540, y=100)

def btn_click2(event):
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
b2.bind('<Button-1>', btn_click2)

# def b2event():   입장 인원수에 맞게 숫자를 바꿔주는 함수
#     if(입장이 완료되면):
#         b2['text'] = "1/4"

b3 = Button(window, text= 'Room3', width=45, height=5, bg='white')
b3.place(x=140, y=250)

def btn_click3(event):
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
b3.bind('<Button-1>', btn_click3)

# def b3event():   입장 인원수에 맞게 숫자를 바꿔주는 함수
#     if(입장이 완료되면):
#         b3['text'] = "1/4"

b4 = Button(window, text= 'Room4', width=45, height=5, bg='white')
b4.place(x=540, y=250)

def btn_click4(event):
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
b4.bind('<Button-1>', btn_click4)

# def b4event():   입장 인원수에 맞게 숫자를 바꿔주는 함수
#     if(입장이 완료되면):
#         b4['text'] = "1/4"

window.mainloop()
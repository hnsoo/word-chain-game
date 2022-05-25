import tkinter
from tkinter import *
import tkinter.messagebox as msgbox

current_person1 = 0
current_person2 = 0
current_person3 = 0
current_person4 = 0

room1 = "Room1"
room2 = "Room2"
room3 = "Room3"
room4 = "Room4"

window = Tk()
window.title("word chain game")
window.geometry("1001x700+100+100")
window.resizable(False, False)
bg = PhotoImage(file='../img/full-background.png')
bg_label = Label(window, image = bg)
bg_label.place(x=0, y=0)

def error():
    msgbox.showerror("Denied", "방이 꽉 찼습니다.")
def btn_click1():
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
    global current_person1
    current_person1 += 1
    b1.config(text=room1+'\t\t{}/4\t  ' .format((current_person1)))
    if(current_person1 == 4):
         b1["bg"]="grey"
         error()

def btn_click2():
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
    global current_person2
    current_person2 += 1
    b2.config(text=room2+'\t\t{}/4\t  ' .format((current_person2)))
    if(current_person2 == 4):
         b2["bg"] = "grey"
         error()

def btn_click3():
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
    global current_person3
    current_person3 += 1
    b3.config(text=room3+'\t\t{}/4\t  ' .format((current_person3)))
    if(current_person3 == 4):
         b3["bg"] = "grey"
         error()

def btn_click4():
    print("방에 입장하겠습니다") #방의 입장 화면으로 넘길 것
    global current_person4
    current_person4 += 1
    b4.config(text=room4+'\t\t{}/4\t  ' .format((current_person4)))
    if(current_person4 == 4):
         b4["bg"] = "grey"
         error()

b1 = tkinter.Button(window, text=room1+'\t\t{}/4\t  ' .format(current_person1), anchor='e', width=45, height=5, bg='white', command=btn_click1)
b1.place(x=140, y=100)

b2 = Button(window, text=room2+'\t\t{}/4\t  '.format(current_person2), anchor='e', width=45, height=5, bg='white', command=btn_click2)
b2.place(x=540, y=100)

b3 = Button(window, text=room3+'\t\t{}/4\t  '.format(current_person3), anchor='e', width=45, height=5, bg='white', command=btn_click3)
b3.place(x=140, y=250)

b4 = Button(window, text=room4+'\t\t{}/4\t  '.format(current_person4), anchor='e', width=45, height=5, bg='white', command=btn_click4)
b4.place(x=540, y=250)

window.mainloop()
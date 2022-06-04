import socket
from tkinter import *
import tkinter.messagebox as msgbox


class Room():
    def __init__(self, master, client_socket):
        self.client_socket = client_socket
        self.window = master
        self.current_person = [0, 0, 0, 0]
        self.bg = None
        self.bg_label = None
        self.refresh = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.init_gui()

    def init_gui(self):
        # 윈도우 창
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)
        # 배경 화면
        self.bg = PhotoImage(file='../img/full-background.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)

        def refresh_click():
            print('click')

        def btn_click1():
            self.current_person[0] += 1
            self.b1.config(text='room1' + '\t\t{}/4\t  '.format(self.current_person[0]))
            if self.current_person[0] == 4:
                self.b1["bg"] = "grey"
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
            self.client_socket.send('/room/1'.encode('utf-8'))

        def btn_click2():
            print("방에 입장하겠습니다")  # 방의 입장 화면으로 넘길 것
            self.current_person[1] += 1
            self.b2.config(text='room2' + '\t\t{}/4\t  '.format(self.current_person[1]))
            if self.current_person[1] == 4:
                self.b2["bg"] = "grey"
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
            self.client_socket.send('/room/2'.encode('utf-8'))

        def btn_click3():
            print("방에 입장하겠습니다")  # 방의 입장 화면으로 넘길 것
            self.current_person[2] += 1
            self.b3.config(text='room3' + '\t\t{}/4\t  '.format(self.current_person[2]))
            if self.current_person[2] == 4:
                self.b3["bg"] = "grey"
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
            self.client_socket.send('/room/3'.encode('utf-8'))

        def btn_click4():
            print("방에 입장하겠습니다")  # 방의 입장 화면으로 넘길 것
            self.current_person[3] += 1
            self.b4.config(text='room4' + '\t\t{}/4\t  '.format(self.current_person[3]))
            if self.current_person[3] == 4:
                self.b4["bg"] = "grey"
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
            self.client_socket.send('/room/4'.encode('utf-8'))

        self.refresh = Button(self.window, text='refresh', width=10, height=2, bg='white', command=refresh_click)
        self.refresh.place(x=785, y=360)

        self.b1 = Button(self.window, text='room1' + '\t\t{}/4\t  '.format(self.current_person[0]), anchor='e',
                         width=45, height=5,
                         bg='white', command=btn_click1)
        self.b1.place(x=140, y=100)

        self.b2 = Button(self.window, text='room2' + '\t\t{}/4\t  '.format(self.current_person[1]), anchor='e',
                         width=45, height=5,
                         bg='white', command=btn_click2)
        self.b2.place(x=540, y=100)

        self.b3 = Button(self.window, text='room3' + '\t\t{}/4\t  '.format(self.current_person[2]), anchor='e',
                         width=45, height=5,
                         bg='white', command=btn_click3)
        self.b3.place(x=140, y=250)

        self.b4 = Button(self.window, text='room4' + '\t\t{}/4\t  '.format(self.current_person[3]), anchor='e',
                         width=45, height=5,
                         bg='white', command=btn_click4)
        self.b4.place(x=540, y=250)

import pickle
import time
from tkinter import *
import tkinter.messagebox as msgbox


class Room():
    def __init__(self, master, client_socket, user_name):
        self.client_socket = client_socket
        self.user_name = user_name
        self.window = master
        self.current_room_count = []
        self.select_room = 0
        self.bg = None
        self.bg_label = None
        self.refresh = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.init_gui()

    def ret_select_room(self):
        return self.select_room

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
            self.client_socket.send('/refresh'.encode('utf-8'))
            time.sleep(0.5)
            buffer = self.client_socket.recv(256)
            self.current_room_count = pickle.loads(buffer)
            self.b1.config(text='room1' + '\t\t{}/4\t  '.format(self.current_room_count[0]))
            self.b2.config(text='room2' + '\t\t{}/4\t  '.format(self.current_room_count[1]))
            self.b3.config(text='room3' + '\t\t{}/4\t  '.format(self.current_room_count[2]))
            self.b4.config(text='room4' + '\t\t{}/4\t  '.format(self.current_room_count[3]))

        def refresh_room(room_number=0):
            self.client_socket.send(('/room/1'+self.user_name).encode('utf-8'))
            time.sleep(0.5)
            msg = (self.client_socket.recv(256)).decode('utf-8')
            if msg == 'no':
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
            else:
                self.select_room = 1
                self.window.destroy()

        self.refresh = Button(self.window, text='refresh', width=10, height=2, bg='white', command=refresh_click)
        self.refresh.place(x=785, y=360)

        self.b1 = Button(self.window, text='room1' + '\t\t0/4\t  ', anchor='e',
                         width=45, height=5,
                         bg='white', command=lambda: refresh_room(1))
        self.b1.place(x=140, y=100)

        self.b2 = Button(self.window, text='room2' + '\t\t0/4\t  ', anchor='e',
                         width=45, height=5,
                         bg='white', command=lambda: refresh_room(2))
        self.b2.place(x=540, y=100)

        self.b3 = Button(self.window, text='room3' + '\t\t0/4\t  ', anchor='e',
                         width=45, height=5,
                         bg='white', command=lambda: refresh_room(3))
        self.b3.place(x=140, y=250)

        self.b4 = Button(self.window, text='room4' + '\t\t0/4\t  ', anchor='e',
                         width=45, height=5,
                         bg='white', command=lambda: refresh_room(4))
        self.b4.place(x=540, y=250)

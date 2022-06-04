from tkinter import *


class Ingame:
    def __init__(self, master, client_socket):
        self.window = master
        self.bg = None
        self.bg_label = None
        self.user1 = None
        self.user2 = None
        self.user3 = None
        self.user4 = None
        self.exit = None
        self.init_gui()

    def init_gui(self):
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)
        # 배경 화면
        self.bg = PhotoImage(file='../img/ingame-page.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)

        self.user1 = Label(self.window, text='user1')
        self.user2 = Label(self.window, text='user2')
        self.user3 = Label(self.window, text='user3')
        self.user4 = Label(self.window, text='user4')

        # 나가기
        self.exit = Button(self.window, text='나가기', anchor='center', width=20, height=3, bg='grey', fg='white')
        self.exit.place(x=0, y=0)

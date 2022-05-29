from tkinter import *


class Ingame:
    def __init__(self, master):
        self.window = master
        self.init_gui()

    def init_gui(self):
        # 윈도우 창
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)

        # 배경 화면
        self.bg = PhotoImage(file='../img/ingame-page.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)

        # 나가기
        self.exit = None
        self.exit = Button(self.window, text='나가기', anchor='center', width=20, height=3, bg='grey', fg='white')
        self.exit.place(x=0, y=0)
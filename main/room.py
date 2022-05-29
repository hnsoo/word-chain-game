from tkinter import *
import tkinter.messagebox as msgbox

class Room():
    def __init__(self, master):
        self.window = master
        self.current_person = [0, 0, 0, 0]
        self.bg = None
        self.bg_label = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.init_gui()

    def personCheck(self):
        self.current_person[0] += 1
        print("{}" .format(self.current_person[0]))
        if self.current_person[0] >= 4:
            msgbox.showerror("Denied", "방이 꽉 찼습니다.")
            if self.current_person[0] == 4:
                self.b1["bg"] = "grey"
        self.window.destroy()

    def init_gui(self):
        # 윈도우 창
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)
        # 배경 화면
        self.bg = PhotoImage(file='../img/full-background.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)

        def btn_click1():
            self.current_person[0] += 1
            if self.current_person[0] > 4:
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
                # 꽉차면 못들어가게 막아야 됌
            elif self.current_person[0] == 4:
                self.b1["bg"] = "grey"
                # 꽉차면 못들어가게 막아야 됌
            self.b1.config(text='room1' + '\t\t{}/4\t  '.format(self.current_person[0]))
            self.window.destroy()

        def btn_click2():
            self.current_person[1] += 1
            if self.current_person[1] > 4:
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
                # 꽉차면 못들어가게 막아야 됌
            elif self.current_person[1] == 4:
                self.b2["bg"] = "grey"
                # 꽉차면 못들어가게 막아야 됌
            self.b2.config(text='room2' + '\t\t{}/4\t  '.format(self.current_person[1]))
            self.window.destroy()

        def btn_click3():
            self.current_person[2] += 1
            if self.current_person[2] > 4:
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
                # 꽉차면 못들어가게 막아야 됌
            elif self.current_person[2] == 4:
                self.b3["bg"] = "grey"
                # 꽉차면 못들어가게 막아야 됌
            self.b3.config(text='room3' + '\t\t{}/4\t  '.format(self.current_person[2]))
            self.window.destroy()

        def btn_click4():
            self.current_person[3] += 1
            if self.current_person[3] > 4:
                msgbox.showerror("Denied", "방이 꽉 찼습니다.")
                # 꽉차면 못들어가게 막아야 됌
            elif self.current_person[3] == 4:
                self.b4["bg"] = "grey"
                # 꽉차면 못들어가게 막아야 됌
            self.b4.config(text='room4' + '\t\t{}/4\t  '.format(self.current_person[3]))
            self.window.destroy()

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
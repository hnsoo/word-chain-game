from tkinter import *

class Rank():
    def __init__(self):
        self.window = Tk()
        self.window.title("Ranking")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)

        self.bg = PhotoImage(file="../img/ranking-page.png")
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)

        self.btn_start = Button(self.window, text='계속하기', font=("Homenaje", 20, "bold"), anchor='center', width=18, height=3, bg='#72F987') #command="~~~" 시켜서 재시작 화면으로 넘겨야함
        self.btn_start.place(x=170, y=330)
        self.btn_exit = Button(self.window, text='종료하기', font=("Homenaje", 20, "bold"), anchor='center', width=18, height=3, bg='#A63641') #command="~~~"  재시작 화면으로 넘겨야함
        self.btn_exit.place(x=550, y=330)

        mainloop()






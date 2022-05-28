from tkinter import *

window = Tk()

window.title("Ranking")
window.geometry("1001x700+100+100")
window.resizable(False, False)

bg = PhotoImage(file="../img/ranking-page.png")
bg_label = Label(window, image=bg)
bg_label.place(x=0, y=0)


btn_start = Button(window, text='계속하기', font=("Homenaje", 20, "bold"), anchor='center', width=18, height=3, bg='#72F987') #command="~~~" 시켜서 재시작 화면으로 넘겨야함
btn_start.place(x=170, y=330)

btn_exit = Button(window, text='종료하기', font=("Homenaje", 20, "bold"), anchor='center', width=18, height=3, bg='#A63641') #command="~~~" 시켜서 재시작 화면으로 넘겨야함
btn_exit.place(x=550, y=330)





mainloop()






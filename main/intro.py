from tkinter import *


class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.config(width=43, bd=2)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


if __name__ == "__main__":
    window = Tk()

    # 윈도우
    window.title("word chain game")
    window.geometry("1001x700+100+100")
    window.resizable(False, False)

    # 배경 화면
    bg = PhotoImage(file='../img/intro-page.png')
    bg_label = Label(window, image=bg)
    bg_label.place(x=0, y=0)

    # 닉네임 입력 박스
    textbox = EntryWithPlaceholder(window, "영문, 숫자 최대 10자리")
    textbox.place(x=350, y=300)

    # 시작 버튼
    button = Button(window, text="Go", bg="#ebddcc", fg="black", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100)
    button.place(x= 460,y=350)

    window.mainloop()

from tkinter import *
from tkinter import messagebox


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


class Intro():
    def __init__(self):
        self.userName = ""
        self.window = Tk()
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)
        # 배경 화면
        self.bg = PhotoImage(file='../img/intro-page.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)

        # 닉네임 입력 박스
        self.textbox = textbox = EntryWithPlaceholder(self.window, "영문, 숫자 최대 10자리")
        self.textbox.place(x=350, y=300)

        # 시작 버튼
        self.button = Button(self.window, text="Go", bg="#ebddcc", fg="black", overrelief="solid", width=10,
                             repeatdelay=1000, repeatinterval=100, command=self.nameCheck)
        self.button.place(x=460, y=350)

        mainloop()

    def nameCheck(self):
        count = 0
        if len(self.textbox.get()) <= 10:
            for t in self.textbox.get():
                if 48 <= ord(t) <= 57 or 65 <= ord(t) <= 90 or 97 <= ord(t) <= 122:
                    count += 1

            if count != len(self.textbox.get()):
                messagebox.showwarning("닉네임 양식 오류", "영문, 숫자 최대 10자리로 닉네임을 생성해주세요.")
            else:
                self.userName = self.textbox.get()
                self.window.destroy()
        else:
            messagebox.showwarning("닉네임 양식 오류", "영문, 숫자 최대 10자리로 닉네임을 생성해주세요.")

    def retName(self):
        return self.userName


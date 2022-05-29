from tkinter import *
from tkinter import messagebox
import socket
import placeholder

class Intro:
    client_socket = None

    def __init__(self, master):
        self.userName = ""

        # 클래스 속성
        self.window = master
        self.bg = None
        self.bg_label = None
        self.textbox = None
        self.button = None
        # 클래스 메소드
        self.init_gui()

    def init_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_ip = '127.0.0.1'
        remote_port = 55555
        self.client_socket.connect((remote_ip, remote_port))

    def init_gui(self):
        # 윈도우 창
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)
        # 배경 화면
        self.bg = PhotoImage(file='../img/intro-page.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)
        # 닉네임 입력 박스
        self.textbox = placeholder.EntryWithPlaceholder(self.window, "영문, 숫자 최대 10자리")
        self.textbox.place(x=350, y=300)
        # 시작 버튼
        self.button = Button(self.window, text="Go", bg="#ebddcc", fg="black", overrelief="solid", width=10,
                             repeatdelay=1000, repeatinterval=100, command=self.nameCheck)
        self.button.place(x=460, y=350)

    def nameCheck(self):
        count = 0
        if len(self.textbox.get()) <= 10:
            for t in self.textbox.get():
                if 48 <= ord(t) <= 57 or 65 <= ord(t) <= 90 or 97 <= ord(t) <= 122:
                    count += 1

            if count != len(self.textbox.get()):
                messagebox.showwarning("닉네임 양식 오류", "영문, 숫자 최대 10자리로 닉네임을 생성해주세요.")
            else:
                self.init_socket()
                self.client_socket.send(self.textbox.get().encode('utf-8'))
                if self.receive_response():
                    self.userName = self.textbox.get()
                    self.client_socket.close()
                    self.window.destroy()
                else:
                    messagebox.showwarning("닉네임 중복 오류", "서버 상에 해당 닉네임이 존재합니다. ")
                    self.client_socket.close()
        else:
            messagebox.showwarning("닉네임 양식 오류", "영문, 숫자 최대 10자리로 닉네임을 생성해주세요.")

    def receive_response(self):
        while True:
            buffer = self.client_socket.recv(256).decode('utf-8')
            if not buffer or "no" in buffer:
                return False
            else:
                return True

    def retName(self):
        return self.userName

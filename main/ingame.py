import threading
import tkinter.font
from tkinter import *
from datetime import datetime


class Ingame:
    def __init__(self, master, client_socket, room_num, name):
        self.name = name
        self.room_num = room_num
        self.client_socket = client_socket
        self.users_name = []
        self.window = master
        self.bg = None
        self.bg_label = None
        self.frame = None
        self.user_box = []
        self.exit = None
        self.enter_text_widget = None
        self.chat_transcript_area = None
        self.word_label = None
        self.time_box = None
        self.init_gui()
        self.timer = None
        self.listen_for_incoming_messages_in_a_thread()

    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.receive_message_from_server,
                                  args=(self.client_socket,))
        thread.start()

    def receive_message_from_server(self, so):
        while True:
            buffer = so.recv(256)
            message = buffer.decode('utf-8')
            print(message)
            if "join" in message:
                user = message.split(":")[1]
                message = '[알림] ' + user + " 님이 입장하였습니다."
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)
            elif "start" in message:  # Message at game Started

                # start:{start_word}:{who_is_first_player}
                start_word = message.split(":")[1]
                who_is_first_player = message.split(":")[2]
                self.users_name = (message.split(":")[3]).split(",")
                str_timer = message.split(":")[4]
                self.timer = datetime.strptime(str_timer, '%d/%m/%Y/%H/%M/%S')

                self.set_interval(self.count_timer(), 1)

                print(self.users_name)
                # 유저 목록 UI 출력
                self.display_user_box()
                self.word_label.configure(text=start_word)
                message = "게임이 시작했습니다. 시작단어는 {}입니다. {}님부터 시작하겠습니다.".format(start_word, who_is_first_player)
                # 유저 박스 색상 변경
                self.change_user_box_color(who_is_first_player, "answer")
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)

                if who_is_first_player == self.name:
                    senders = self.name + ":"
                    data = "제 순서입니다."
                    msg = (senders + data).encode('utf-8')
                    self.client_socket.send(msg)

            elif "attempt" in message:  #
                # attempt:{who : String} : {word : string} : {is_Correct? : bool}
                attempt_user = message.split(":")[1]
                attempt_word = message.split(":")[2]
                result = message.split(":")[3]
                result_message = "{}님이 {}를 입력 했습니다. {}!".format(attempt_user, attempt_word,
                                                                "정답" if result == 'True' else "실패")
                if result == 'True':
                    self.change_user_box_color(attempt_user, "default")
                self.chat_transcript_area.insert('end', result_message + '\n')
                self.chat_transcript_area.yview(END)

            elif "change_turn" in message:
                # change_turn:{player}:{last_word}
                now_turn = message.split(":")[1]
                last_word = message.split(":")[2]
                self.word_label.configure(text=last_word)
                message = "{}님 차례로 바뀌었습니다! - '{}' 이어해주세요~".format(now_turn, last_word)
                # 유저 박스 색상 변경
                self.change_user_box_color(now_turn, "answer")
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)

                if now_turn == self.name:
                    senders = self.name + ":"
                    data = '제 순서입니다.'
                    msg = (senders + data).encode('utf-8')
                    self.client_socket.send(msg)

            elif "finish" in message:
                result = message.split(":")[1]
                self.chat_transcript_area.insert('end', result + '\n')
                self.chat_transcript_area.yview(END)
                print(result)

            else:
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)

    def change_user_box_color(self, name, user_type):
        for box in self.user_box:
            if box.cget("text") == name:
                if user_type == "answer":
                    box.configure(bg='#1fb177')
                else:
                    box.configure(bg='#b6f2da')

    def init_gui(self):
        self.window.title("word chain game")
        self.window.geometry("1001x700+100+100")
        self.window.resizable(False, False)
        # 배경 화면
        self.bg = PhotoImage(file='../img/ingame-page.png')
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0)
        # 채팅창
        self.display_chat_entry_box()
        self.display_chat_box()
        # 단어
        word_frame = Frame()
        word_frame.pack(side='top', pady=110)
        self.word_label = Label(word_frame, relief='flat', font=tkinter.font.Font(size=25, family='맑은 고딕'),
                                text='게임 시작 전', bg='white')
        self.word_label.pack()
        # 시간
        self.display_time_box(seconds=0)
        # 나가기
        self.exit = Button(self.window, text=self.name, anchor='center', width=10, height=2, bg='grey', fg='white')
        self.exit.place(x=0, y=0)

    def display_chat_entry_box(self):
        self.enter_text_widget = Text(self.window, width=121, height=1, font=("Serif", 12))
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        self.enter_text_widget.pack(side='bottom', pady=10)

    def display_chat_box(self):
        frame = Frame()
        self.chat_transcript_area = Text(frame, width=119, height=9, font=("Serif", 12))
        scrollbar = Scrollbar(frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.pack(side='left')
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='bottom')

    def on_enter_key_pressed(self, event):
        senders = self.name + ":"
        data = self.enter_text_widget.get(1.0, 'end').strip()
        msg = (senders + data).encode('utf-8')
        self.client_socket.send(msg)
        print('success client to server')
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def display_user_box(self):
        frame = Frame()
        frame.pack(side='top', pady='96')
        font = tkinter.font.Font(size=13)
        print(self.users_name, type(self.users_name))
        for user in self.users_name:
            print(user)
            self.user_box.append(Label(frame, width=10, height=2, bg='#b6f2da', relief='groove', font=font,
                                       text=user))
            self.user_box[-1].pack(side='left')

    def display_time_box(self, seconds):
        if seconds != 0:
            self.time_box = Label(self.window, relief='flat', text="{}s".format(seconds),
                                  font=tkinter.font.Font(size=14, weight='bold'),
                                  bg='white')
            self.time_box.place(x=130, y=340)

    def change_time_box(self, seconds):
        if self.time_box is None:
            self.display_time_box(seconds)
        else:
            self.time_box.configure(text="{}s".format(seconds))

    def count_timer(self):
        now = datetime.now()
        if self.timer < now:
            self.change_time_box(0)
        else:
            diff = self.timer - now
            self.change_time_box(diff.seconds)

    def set_interval(self, func, sec):
        def func_wrapper():
            self.set_interval(self.count_timer(), sec)
            self.count_timer()

        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

# if __name__ == "__main__":
#     Ingame(Tk(), None, 1, 'a')
#     mainloop()

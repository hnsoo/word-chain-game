import threading
import tkinter.font
from tkinter import *


class Ingame:
    def __init__(self, master, client_socket, room_num):
        self.room_num = room_num
        self.client_socket = client_socket
        self.users_name = []
        self.window = master
        self.bg = None
        self.bg_label = None
        self.frame = None
        self.users = []
        self.exit = None
        self.enter_text_widget = None
        self.chat_transcript_area = None
        self.init_gui()
        self.user_box()
        self.listen_for_incoming_messages_in_a_thread()

    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.receive_message_from_server,
                                  args=(self.client_socket,))
        thread.start()

    def receive_message_from_server(self, so):
        while True:
            buffer = so.recv(256)
            message = buffer.decode('utf-8')

            if "join" in message:
                user = message.split(":")[1]
                message = '[알림] ' + user + " 님이 입장하였습니다."
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)
            else:
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)

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
        # 나가기
        self.exit = Button(self.window, text='나가기', anchor='center', width=20, height=3, bg='grey', fg='white')
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

    def on_enter_key_pressed(self):
        pass

    def user_box(self):
        frame = Frame(self.window)
        font = tkinter.font.Font(size=13)
        for user in self.users_name:
            self.users.append(Label(frame, width=10, height=2, bg='#b6f2da', relief='groove', font=font, text='{}'.format(user)))
            self.users[-1].pack(side='left')

        frame.place(x=310, y=367)


# if __name__ == "__main__":
#     Ingame(Tk(), None, 1)
#     mainloop()

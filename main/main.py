import socket
from tkinter import Tk

import intro
import room

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 10319))

    # 게임 처음 화면
    window = Tk()
    p = intro.Intro(window, client_socket)
    window.mainloop()

    print(p.retName())
    window = Tk()
    p = room.Room(window, client_socket)
    window.mainloop()

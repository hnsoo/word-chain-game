import socket
from tkinter import Tk

import intro
import room

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 55555))
    client_socket.send('/init'.encode('utf-8'))
    res = False
    buffer = client_socket.recv(256).decode('utf-8')
    if buffer == 'yes':
        res = True

    # 게임 처음 화면
    window = Tk()
    p = intro.Intro(window)
    window.mainloop()

    print(p.retName())
    window = Tk()
    p = room.Room(window)
    window.mainloop()

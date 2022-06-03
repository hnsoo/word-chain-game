from tkinter import Tk, mainloop

import socket
import intro, room
import ingame


if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 55555))

    # 게임 처음 화면
    window = Tk()
    p = intro.Intro(window)
    window.mainloop()

    print(p.retName())
    window = Tk()
    p = room.Room(window)
    window.mainloop()

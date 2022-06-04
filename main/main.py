import socket
from tkinter import Tk

import intro
import room
import ingame

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 10319))

    # 게임 처음 화면
    window = Tk()
    i = intro.Intro(window, client_socket)
    window.mainloop()

    window = Tk()
    r = room.Room(window, client_socket, i.retName())
    room_num = r.ret_select_room()
    window.mainloop()

    window = Tk()
    ing = ingame.Ingame(window, client_socket, room_num)
    window.mainloop()
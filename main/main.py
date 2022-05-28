from tkinter import Tk, mainloop

import intro, room
import ingame

if __name__ == "__main__":
    # 게임 처음 화면
    window = Tk()
    p = intro.Intro(window)
    window.mainloop()

    print(p.retName())
    p = room.Room()




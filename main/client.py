import socket
import threading
from tkinter import *

window=Tk()
user_box = []
frame = Frame()
frame.pack(side='top', pady=50)
for user in ['a', 'b']:
    user_box.append(Label(frame, width=10, height=2, bg='#b6f2da', relief='groove', text='{}'.format(user)))
    user_box[-1].pack(side='left')
window.mainloop()
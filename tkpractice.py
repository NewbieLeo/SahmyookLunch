from msvcrt import LK_LOCK
from tkinter import *

root = Tk()
root.title('hello')
root.geometry('320x300')
l = ['abc', 'def', 'ghi']
label = Label(root, text='4월 20일', font=('나눔스퀘어', 25))
label.pack()
listbox = Listbox(root, height=0, selectmode='extended', font='나눔스퀘어')
for i in l:
    listbox.insert(END, i)
listbox.pack()
root.mainloop()

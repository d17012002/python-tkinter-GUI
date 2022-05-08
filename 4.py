from tkinter import *
from tkinter.ttk import *
from functools import partial
from tkinter import messagebox
window = Tk()
window.title("Raise Application Errors")
window.geometry("400x300")

key = StringVar()

combo = Combobox(window, textvariable=key)
combo["values"]=("YesNo","RetryCancel","YesNoCancel","OkCancel","Select")
combo.current(4)
combo.grid(column=3, row=0)

def clicked(key):
    action = key.get()
    if(action=="YesNo"):
        res = messagebox.askyesno('Message title','Message content')
    elif(action=="RetryCancel"):
        res = messagebox.askretrycancel('Message title','message Content')
    elif(action=="YesNoCancel"):
        res = messagebox.askyesnocancel('Message Title','Message Content')
    elif(action=="OkCancel"):
        res = messagebox.askokcancel('Message Title','Message content')


clicked = partial(clicked,key)

btn = Button(window, text="Submit", command=clicked)
btn.grid(column=4, row=0)

window.mainloop()
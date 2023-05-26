import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg = "red")
#Button Function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)
#ladel for entering user url
Label(win,text="Enter your url link ",font = "impack 17 bold",bg="black",fg="white").pack(fill="x")
#Entry Box
entry1 = Entry(win , font = "10" , bd = 3 , width = 40)
entry1.pack(pady = 30)
#Button
Button(win,text="Click me",font="impack 12 bold",bg="white",fg="black",width="13",command=short).pack()
#Shortend url
entry2 = Entry(win,font="impack 16 bold",bd=3,width=25)
entry2.pack(pady=30)
mainloop()


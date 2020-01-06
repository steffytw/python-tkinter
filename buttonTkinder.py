from tkinter import *

def display():
    label1.config(text="button clicked")


window = Tk()
window.title("GUI Button")

label1 = Label(window, text=" ")
but=Button(window, text = "click me", command =display)
but.pack()
label1.pack()
window.geometry("300x300")
window.mainloop()
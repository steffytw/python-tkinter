from tkinter import *

window =Tk()
window.title("GUI")

def display():
    m1.config(text="file clicked")

menubar = Menu(window)
m1 = menubar.add_command(Label="file", command=display())
window.geometry("300x300")
window.mainloop()
from tkinter import *

root = Tk()


def display():
    print("hello!")


# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="New", command=display)
menubar.add_command(label="Quit", command=root.quit)

# display the menu
root.config(menu=menubar)
root.mainloop()

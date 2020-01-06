from tkinter import *

data = Tk()

label1 = Label(data,text="Username:")
label2 = Label(data,text="Password:")

e1 = Entry(data)
e2 = Entry(data)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
button1= Button(data, text = "login")
button1.grid(row = 2, column = 0)
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
data.geometry("300x300")
data.mainloop()
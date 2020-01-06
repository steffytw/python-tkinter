from tkinter import *
import mysql.connector

db1 = mysql.connector.connect(
    host="192.168.1.250",
    user="scopeinternship",
    password="scopeinternship",
    database="scopeinternship"
)
cursor_data = db1.cursor()
data = Tk()


def display():
    flag = 0
    data1 = e1.get()
    data2 = e2.get()
    cursor_data.execute("SELECT * FROM  PYTHON_DATA_STEFFY")
    cur = cursor_data.fetchall()
    for i in cur:
        print(i)
        if i[1] == data1 or i[2] == data2:
            flag = 1
        else:
            flag = 0
    print(flag)
    if flag == 1:
        label12.config(text="Successfully logged in")
    else:
        label12.config(text="invalid username or password")


label1 = Label(data, text="Username:")
label2 = Label(data, text="Password:")
label12 = Label(data, text="")

e1 = Entry(data)
e2 = Entry(data)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
button1= Button(data, text = "login",command = display)
button1.grid(row=2, column=0)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label12.grid(row=3, column=0)
data.geometry("300x300")
data.mainloop()
# cursor_data.execute("SELECT * FROM  PYTHON_DATA_STEFFY")
# cur = cursor_data.fetchall()
# for i in cur:
#      print(i)

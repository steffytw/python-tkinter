# Python tkinter

* Tkinter is the inbuilt python module that is used to create GUI applications. 
* It is one of the most commonly used modules for creating GUI applications in Python as it is simple and easy to work with. 
* It gives an object-oriented interface to the Tk GUI toolkit.

Some other Python Libraries available for creating GUI applications are

- Kivy
- Python Qt
- wxPython ,
Among all Tkinter is most widely used

## Fundamental structure of tkinter program :

![image](https://user-images.githubusercontent.com/33021781/129498549-c43118f2-6c9f-4cb6-ac95-e9eab65b940d.png)

## Basic tkinter Widgets:

```
widget = Widget(window, **options)
```

| Widget | Description |
| ------ | ------ |
| Label | It is used to display text or image on the screen |
| Button | It is used to add buttons to your application |
| Canvas | It is used to draw pictures and others layouts like texts, graphics etc. |
| ComboBox | It contains a down arrow to select from list of available options |
| CheckButton | It displays a number of options to the user as toggle buttons from which user can select any number of options. |
| RadiButton | It is used to implement one-of-many selection as it allows only one option to be selected |
| Entry | It is used to input single line text entry from user |
| Frame | It is used as container to hold and organize the widgets |
| Message | It works same as that of label and refers to multi-line and non-editable text |
| Scale | It is used to provide a graphical slider which allows to select any value from that scale |
| Scrollbar | It is used to scroll down the contents. It provides a slide controller. |
| SpinBox | It is allows user to select from given set of values |
| Text | It allows user to edit multiline text and format the way it has to be displayed |
| Menu | It is used to create all kinds of menu used by an application |


## Geometric configuration of the widgets

tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager class.
* pack() method :  It organizes the widgets in blocks before placing in the parent widget.
* grid() method :  It organizes the widgets in grid (table-like structure) before placing in the parent widget.
* place() method : It organizes the widgets by placing them on specific positions directed by the programmer.

## Example
```
from tkinter import *

window = Tk()
window.title("GUI tkinter")

label_text = "Hello World!"

label1 = Label(window, text=label_text)

label1.pack()
window.geometry("100x100")
window.mainloop()
```





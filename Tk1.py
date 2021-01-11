from tkinter import *
# To create the main window, tkinter offers a method ‘Tk’.
x = Tk()

x.geometry('300x300')           # WidthxHeight
x.maxsize(500,500)              # Width, Height
x.minsize(200,200)

Var = Label(text='This is our first GUI Application.')
Var.pack()

# This is an infinite loop used to run the application.
x.mainloop()
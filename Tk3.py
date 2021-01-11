from tkinter import *

app = Tk()

app.geometry('300x300')
app.title('Application')

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

app_label = Label(text='''Basic Programs:  
Python program to add two numbers
Maximum of two numbers in Python
Python Program for factorial of a number
Python Program for simple interest
Python Program for compound interest
Python Program to check Armstrong Number
''', bg='yellow', fg='red', padx=40, pady=40, font='Arial 15 bold', borderwidth=2, relief=GROOVE)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady
app_label.pack(side=LEFT, fill=Y, padx=25, pady=25)

app.mainloop()
from tkinter import *
root = Tk()
root.geometry('400x300')

def a():
    print("9")

def b():
    print("8")

def c():
    print("7")

frame = Frame(root, borderwidth= 1, bg='black', relief=FLAT,)
frame.pack(side=LEFT, anchor='nw')

b1 = Button(frame, fg='red', text="7",padx=20, command=c)
b1.pack(side=LEFT,padx=1)

b2 = Button(frame, fg='red', text="8",padx=20, command=b)
b2.pack(side=LEFT,padx=1)

b3 = Button(frame,fg='red', text="9",padx=20, command=a)
b3.pack(side=RIGHT,padx=1)

root.mainloop()

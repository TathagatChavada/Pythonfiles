from tkinter import*
root = Tk()
root.geometry('355x333')

f1 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2 = Frame(root, bg='grey', borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=135)
l = Label(f2, text="Welcome to Pycharm")
l.pack()

root.mainloop()
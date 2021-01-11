from tkinter import  *
stem = Tk()
stem.geometry('400x300')

user = Label(stem, text="Username")
password = Label(stem, text="Password")
user.grid(row = 0, column = 1)
password.grid(row = 2, column = 1)

stem.mainloop()
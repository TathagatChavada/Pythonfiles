from tkinter import *
x = Tk()

x.geometry('500x450')
photo = PhotoImage(file="1.png")                    # For displaying images
photo_label = Label(image = photo)

photo_label.pack()

x.mainloop()
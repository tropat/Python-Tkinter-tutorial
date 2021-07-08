from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkbox")
root.geometry("400x400")

var = StringVar()

def show():
    myLabel = Label(root, text=var.get()).pack()

c= Checkbutton(root, text="Check this box!", variable=var, offvalue="Hamburger", onvalue="Pizza")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
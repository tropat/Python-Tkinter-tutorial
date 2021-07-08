from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown Menus")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get())

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options) # for some reason it doesn't work and I don't know why
drop.pack()

myButton = Button(root, text="Show Selection", command=show)

root.mainloop()
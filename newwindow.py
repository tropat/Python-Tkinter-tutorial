from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Main Window")

def open():
    global my_img

    top = Toplevel()
    top.title("Second Window")

    #lbl = Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open("baran.png"))
    my_label = Label(top, image=my_img).pack()

    btn2 = Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()
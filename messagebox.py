from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('messagebox')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()
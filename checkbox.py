from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lear about Checkbox")
root.iconbitmap("C:/Users/sereyratha.chan/Documents/image3.webp")

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()
check_box = Checkbutton(root, text="Check this box", variable=var, onvalue="on", offvalue="off")
check_box.deselect()
check_box.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
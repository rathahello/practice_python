from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn Create New Window")
root.iconbitmap('C:/Users/sereyratha.chan/Documents/image3.webp')

def open():
    global my_img
    top = Toplevel()
    root.title("Learn Create New Window")
    root.iconbitmap('C:/Users/sereyratha.chan/Documents/image3.webp')
    my_img = ImageTk.PhotoImage(Image.open("images/img1.png"))
    Label(top, image=my_img).pack()
    Button(top, text="Close window", command=top.destroy).pack()

btn = Button(root, text="Open new window", command=open)
btn.pack()


root.mainloop()
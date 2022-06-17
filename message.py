from struct import pack
from tkinter import *
from urllib import response
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Learn about Message Box")
root.iconbitmap('C:/Users/sereyratha.chan/Documents/image3.webp')

# Message: showinfo,  showwarning,  showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askokcancel("This is my popup!", "Do you want to delete this one?")
    Label(root, text=response).pack()
    if response == 1: 
        Label(root, text="You clicked OK!!").pack()
    else:
        Label(root, text="You clicked CANCEL!!").pack()

Button(root, text="popup", command=popup).pack()


root.mainloop()
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn about Frame')
root.iconbitmap('C:/Users/sereyratha.chan/Documents/image3.webp')

frame = LabelFrame(root, text="This is my Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

btn = Button(frame, text="Click Me")
# btn.pack() 
btn.grid(row=0, column=0)



root.mainloop()
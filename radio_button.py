from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn about Radio Button")
root.iconbitmap('C:/Users/sereyratha.chan/Documents/image3.webp')

# radio_btn = IntVar()
# radio_btn.set("2")
# radio_btn = StringVar()

MODES = [
    ("Pepper", "Pepper"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

radio_btn = StringVar()
radio_btn.set("Pepper")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=radio_btn, value=mode).pack(anchor=W)

def clicked(value): 
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable=radio_btn, value=1, command=lambda: clicked(radio_btn.get())).pack()
# Radiobutton(root, text="Option 2", variable=radio_btn, value=2, command=lambda: clicked(radio_btn.get())).pack()

# myLabel = Label(root, text=radio_btn.get())
# myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(radio_btn.get()))
myButton.pack()

root.mainloop()
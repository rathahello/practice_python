from tkinter import *
root = Tk()

inputField = Entry(root, width=50)
inputField.pack()
inputField.insert(0, "Enter your name:")

def myClick():
    field = "Hello " + inputField.get()
    myLabel = Label(root, text=field)
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()


root.mainloop()
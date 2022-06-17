from tkinter import *

root = Tk()

# myLabel1 = Label(root, text="Hello Ratha!")
# myLabel2 = Label(root, text="My name is Sereyratha CHann")
# myLabel3 = Label(root, text=" ")
    #shoving it onto the screen
# myLabel1.pack()
    #Create grid 
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=0)

    #create function
def myClick():
    myLabel = Label(root, text="Look!", fg="blue")
    myLabel.pack()

    #create button
# myButton = Button(root, text="Click Me!", state=DISABLED)   #button disabled
# myButton = Button(root, text="Click Me!", pady=50)  #Y

myButton = Button(root, text="Click Me!", command=myClick, padx=50, pady=10, fg="yellow", bg="blue") 
myButton.pack()

root.mainloop()
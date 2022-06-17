import math
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)  #font=("default", 40 or 20)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "substract"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "substract":
        e.insert(0, f_num - int(second_number))
    
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    
    if math == "divide":
        e.insert(0, f_num / int(second_number))

button_0= Button(root, text="0", padx=40, pady=20, command=lambda: button_number(0))
button_1= Button(root, text="1", padx=40, pady=20, command=lambda: button_number(1))
button_2= Button(root, text="2", padx=40, pady=20, command=lambda: button_number(2))
button_3= Button(root, text="3", padx=40, pady=20, command=lambda: button_number(3))
button_4= Button(root, text="4", padx=40, pady=20, command=lambda: button_number(4))
button_5= Button(root, text="5", padx=40, pady=20, command=lambda: button_number(5))
button_6= Button(root, text="6", padx=40, pady=20, command=lambda: button_number(6))
button_7= Button(root, text="7", padx=40, pady=20, command=lambda: button_number(7))
button_8= Button(root, text="8", padx=40, pady=20, command=lambda: button_number(8))
button_9= Button(root, text="9", padx=40, pady=20, command=lambda: button_number(9))

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=30, pady=15, command=button_clear)

button_subtract = Button(root, text="-", padx=50, pady=15, command=button_subtract)
button_multiply = Button(root, text="*", padx=50, pady=15, command=button_multiply)
button_divide = Button(root, text="/", padx=50, pady=15, command=button_divide)

# put the button on the screen

button_add.grid(row=5, column=2)
button_clear.grid(row=1, column=2)
button_equal.grid(row=5, column=0)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=5, column=1)

root.mainloop()
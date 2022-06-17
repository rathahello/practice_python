from tkinter import *
from turtle import back
# cmd line to install:   
# 1: pip install pillow 
# 2: pip freeze
from PIL import ImageTk,Image

root = Tk()
root.title('Learn today!')
root.iconbitmap('C:/Users/sereyratha.chan/Documents/image3.webp')

my_img1 = ImageTk.PhotoImage(Image.open("images/img1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def  back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


btn_back = Button(root, text="<<", command=back)
btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2, pady=30)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)
# btn_forward.pack()

root.mainloop()
# importing tkinter and strftime
from tkinter import *
from time import strftime
# Assigning variable to tkinter
root = Tk()
# Title for Application
root.title('Digital clock')
# function for timer


def timer():
    # assigning time to a string variable
    string = strftime("%H:%M:%S %p")
    # configuring by adding time(string) to text
    label.configure(text=string)
    # creating a loop to call timer function after 1000ms
    label.after(1000, timer)


# label variable
label=Label(root,font=('Baskerville old face' , 80), bg = 'white',fg = 'blue')


# positioning of a label
label.pack()
# calling a function timer
timer()
# calling mainloop
root.mainloop()
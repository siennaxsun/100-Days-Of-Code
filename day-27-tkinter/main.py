from tkinter import *


# this line of code is to initialize a window object
# if you just run this line of code, nothing will happen, because you just created a window
# and the computer sees nothing follows, and just ends the program
# so we need a way to keep the window on screen, so you will need to call the mainloop()
window = Tk()

# change the title of the program
window.title("My First GUI Program")

# change the size of the window
window.minsize(width = 500, height = 300)

# add padding to all the widgets:
window.config(padx = 20, pady = 20)


def button_clicked():
    # hold the value from the entry's input: using get() which returns the entry's string
    user_input = input.get()
    my_label["text"] = user_input


# create components
# 1. creating a label: first initialize a label and then specify where the label is placed on screen
my_label = Label(text = "I am a label", font = ("Arial", 24, "bold"), )
# # how the label is gonna laid out on the screen
# my_label.pack(side = "top", expand = 0) # it's packed in the center of the program
my_label.grid(column= 0, row= 0)
my_label.config(padx = 30, pady = 30)

# create a button
button1 = Button(text = "click me", command = button_clicked)
# button.pack()
button1.grid(column = 1, row = 1)


# create a new button
button2 = Button(text = "click me", command = button_clicked)
# button.pack()
button2.grid(column = 2, row = 0)

# create an input
input = Entry(width = 10)
# input.pack()
input.grid(column = 3, row = 3)







# #access the property of the button
# button["fg"] = "grey"
# button["bg"] = "beige"
#
# # set multiple properties of the button
# button.config(fg = "red", bg = "blue")


# this line of code always stays at the very end of your code
# this line of code is baiscally equal to the while loop, in which keeps listening as long as it is true
# and the tikinter module has this function called mainloop() to do the same thing
window.mainloop()
# while True:
#     listening

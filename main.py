from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am A Label",  font=("Arial", 24, "bold"))
my_label.pack(side="top")

my_label['text'] =  "New Text"
my_label.config(text="New Texts")

# Button


def button_clicked():
    my_label['text'] = user_input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=30)
user_input.pack()
# my_label['text'] =

window.mainloop()

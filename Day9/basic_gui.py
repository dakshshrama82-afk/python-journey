
# Basic GUI
from tkinter import *

window = Tk()

window.geometry("600x420")

window.config(bg="white")  # Sets the background color

window.title("HI")  # Sets the window title

label = Label(
    window,
    text="Hello World",  # Sets the text
    fg="blue",  # Sets the text color
    font=("arial", 40, "bold"),  # Sets the font
    bg="black",  # Sets the background color of the label
    padx=10,  # Adds horizontal padding
    pady=10,  # Adds vertical padding
    relief=RAISED,  # Sets the border style
    bd=10  # Sets the border width
)

label.pack()  # Places the label in the window

icon = PhotoImage(file="hi.PNG")  # Initializes the icon image

window.iconphoto(True, icon)  # Sets the window icon

window.mainloop()  # Keeps the window open and running


# Basic GUI
from tkinter import *

window = Tk() # this code make the window

window.geometry("600x420") # provides the shape of window

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
count = 0

def button_1():
    global count
    count +=1
    

image_1 = PhotoImage(file="Screenshot 2026-10-16 231011.png")

button_1 = Button(window,
                  text="click",
                  command=button_1,
                  bg="blue",
                  font=("arial",40),
                  fg="black",
                  activebackground="blue",
                  activeforeground="black",
                  image=image_1,
                  compound=BOTTOM)

button_1.pack()
lable_2 = Label(window,
    text=str(count),                 # Sets the text
    fg="blue",                  # Sets the text color
    font=("arial", 40, "bold"), # Sets the font
    bg="black",                 # Sets the background color of the label
    padx=10,                    # Adds horizontal padding
    pady=10,                    # Adds vertical padding
    relief=RAISED,              # Sets the border style
    bd=10,)                     # Sets the border width,print(count))
lable_2.place(x=0,y=0)
lable_2.pack()

icon = PhotoImage(file="hi.PNG")  # Initializes the icon image

window.iconphoto(True, icon)  # Sets the window icon

window.mainloop()  # Keeps the window open and running

# python offers multiple options for developing GUI .out of all tkinter is the most commonly used method

import tkinter

# important method 1 : TK - it is used to create main window

# window_main = tkinter.Tk(className="my first tkinter window")

# important method 2 :  mainloop() used when your app is ready to run  , infinite loop ,
# wait for an event to occur and process teh event as long as the window is not closed

# ___________________________________________________

# pack() method organize the widgets in block before placing in parent widget
# grid() method organize the widget in tabular form before placing
# place() method organize the widget by specific pos defined by user

# _____________________________________________________

# widgets
# ________________
# buttons

# but = tkinter.Button(window_main, text="click", width=25)
# but.pack()

# ________________
# canvas it is used to draw a pic and other complex layout like graphics, text , widgets
#
# can = tkinter.Canvas(window_main, bd=10, bg="green", width=400, height=400)
# can.pack()

# can.create_line(1,20,30,10)

# _____________________________
# check buttons

# checkbut = tkinter.Checkbutton(window_main, text="mail").grid(row=0)

# ________________________________
# Entry is used to take the single line input from the user

# lab1 = tkinter.Label(window_main, text="First Name").grid(row=0)
# lab2 = tkinter.Label(window_main, text="Last Name").grid(row=2)
# ent = tkinter.Entry(window_main).grid(row=0, column=1)
# ent2 = tkinter.Entry(window_main).grid(row=2, column=1)

# ___________________________________________ important---------
# reading images with tkinter
#
# we require pillow pakage
from PIL import ImageTk , Image

root = tkinter.Tk(className="image reading window")

canvas = tkinter.Canvas(root, width=1000, height=1000 )
canvas.pack()

# loading image

img = ImageTk.PhotoImage(Image.open("ironman.JPG"))

# arrange image parameters in app

canvas.create_image(100,30, anchor="nw", image=img)

# running app
root.mainloop()
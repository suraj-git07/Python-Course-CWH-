# This is a DRS review system .
# library required

import tkinter
import cv2
from PIL import Image, ImageTk
import os
from functools import partial
from threading import *
import imutils
import time


# capturing video
stream = cv2.VideoCapture(r"E:\samrat\testing progs\drs\clip.mp4")

def play(speed):
    print(f"you clicked on play, and the speed is {speed}.")

    if (stream.isOpened())== False:
        print("Error In Opening The Image")
    else:

        frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)

        stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

        grabbed, frame = stream.read()

        if grabbed == False:
            exit()

        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor="nw")

        canvas.create_text(135, 25, fill="black", font="Times 27 bold", text="Decision Pending" )




def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor="nw")
    # 2. wait for 2.5 sec
    time.sleep(2.5)
    # 3. Display out/Not out
    if decision == "out" :
        decision = "out.png"
    else:
        decision= "not_out.png"

    frame = cv2.cvtColor(cv2.imread(decision), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor="nw")


def out():
    thread = Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("decision is out")


def notout():
    thread = Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("decision is not out")


# changing directory
os.chdir(r"E:\samrat\testing progs\drs")

# setting the constant of width and height

SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter gui starts here
window = tkinter.Tk()
window.title("Third Umpire Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(width=SET_WIDTH, height=SET_HEIGHT)
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.pack()

# buttons for control playing
bdn = tkinter.Button(window, text="<< previous (fast)", width=50, command=partial(play, -25))
bdn.pack()

bdn = tkinter.Button(window, text="<< previous (slow)", width=50, command=partial(play, -2))
bdn.pack()

bdn = tkinter.Button(window, text="forward (fast) >>", width=50, command=partial(play, 25))
bdn.pack()

bdn = tkinter.Button(window, text=" forward (slow) >>", width=50, command=partial(play, 1))
bdn.pack()

bdn = tkinter.Button(window, text=" Give Out", width=50, command=out)
bdn.pack()

bdn = tkinter.Button(window, text=" Give Not Out", width=50, command=notout)
bdn.pack()



window.mainloop()


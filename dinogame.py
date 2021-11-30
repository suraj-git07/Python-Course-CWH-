import pyautogui

from PIL import ImageGrab

import time


def hit(key):
    """
    this function is used to click any key as per the argument
    """
    pyautogui.keyDown(key)
    return


def is_collide(data):

    """
    It forms the rectangle on specific pixel of data.
    this func is used to check whether any black object collide with any type of rectangles and then do the commanded
    job

    """

    # forming a rectangle of pixel , upper range for x_axis and inner range for y_axis .
    # this is for checking  if a bird is colliding with the rectangle.
    # if bird collide then press the down key.

    for i in range(470, 485):
        for j in range(190, 225):
            if data[i, j] < 100:
                hit("down")

                return

    # forming a rectangle of pixel , upper range for x_axis and inner range for y_axis .
    # this is for checking if a cactus is colliding with the rectangle.
    # if cactus collide then press the up key.

    for i in range(485, 500):
        for j in range(235, 260):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":

    print("Hey dino game is about to start in 3 seconds")
    time.sleep(3)

    # while loop , so that dino keep playing
    while True:

        # taking the gray scale (black and white) screen_shot of the screen of dino game continuously
        image = ImageGrab.grab().convert('L')

        # Allocates storage for the image and loads the pixel data . in a form of an array
        data = image.load()

        # calling is collide function
        is_collide(data)


# ____________________this is used to forming the rectangles in processing time_____________________________

    # Draw the rectangle for cactus
    # for i in range(490,505):
    #      for j in range(227,260):
    #         data[i,j] = 0

    # Draw the rectangle for birds
    # for i in range(475, 490):
    #     for j in range(190,220):
    #         data[i,j] = 171

    # image.show()

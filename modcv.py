# video capturing

import cv2

cap = cv2.VideoCapture("clip.mp4")

if cap.isOpened() == False:
    print("Error Opening  Video Stream")

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        cv2.imshow("frame", frame)

        if cv2.waitKey(25)== ord("q"):
            break

        else:
            break

cap.release()
cv2.destroyAllWindows()
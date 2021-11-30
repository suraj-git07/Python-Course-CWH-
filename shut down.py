import speech_recognition as sr
import cv2
from ffpyplayer.player import  MediaPlayer

# listening shut down

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    print("Recognising..")
    task = r.recognize_google(audio, language="en-in")
    print(task)
except 101:
    print("Recognition error")

# playing the video

if task == 'shutdown':

    # setting video and audio objects

    vid = cv2.VideoCapture("E:\\samrat\\video\\i_am_iron_man.mp4")
    player = MediaPlayer("E:\\samrat\\video\\i_am_iron_man.mp4")

    # setting frame
    # vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # vid.set(cv2.CAP_PROP_FPS, 25)

    # playing video + audio
    while True:
        ret, frame = vid.read()
        frame = cv2.resize(frame, (1350, 680), 20)

        audio_frame, val = player.get_frame()

        cv2.imshow('output', frame)
        if (cv2.waitKey(1)) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

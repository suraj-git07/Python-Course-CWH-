import pygame as pyg
import time
import datetime


def playmus(file,stopper):
    pyg.mixer.init()
    pyg.mixer.music.load(file)
    pyg.mixer.music.play()
    while True:
        stop=input()
        if stop==stopper:
            pyg.mixer.music.stop()
        break

def log_req(string):
    with open("my_logs.txt","a") as f:
        f.write(f"{string} at {datetime.datetime.now()} \n " )



if __name__=="__main__":

    init_water=time.time()
    init_eyes = time.time()
    init_exercise = time.time()

    water_after_every=35*60
    eyes_after_every=30*60
    exercise_after_every=45*60


    print("I AM HEALTH MANEGER PROG , I HELP U BY MANAGING YOUR HEALTH")
    while True:

        if time.time()-init_water>water_after_every:
            print("this is the time to drink water , enter 'drank' after drinking")
            playmus("Guitar Sikhda-(SwagyJatt.CoM).mp3","drank")
            log_req("Drank water")
            init_water=time.time()

        if time.time() - init_eyes > eyes_after_every:
            print("this is the time for your eyes exercise , enter 'done' after doing it")
            playmus("Backbone-Hardy-Sandhu-(DesiTrack.Com).mp3", "done")
            log_req("eyes exercise")
            init_eyes = time.time()

        if time.time() - init_exercise > exercise_after_every:
            print("this is the time for your physical exercise , enter 'doneexer' after doing it")
            playmus("Bom_Diggy_Diggy__(VIDEO)___Zack_Knight___Jasmin_Walia___Sonu_Ke_Titu_Ki_Swee.mp3", "doneexer")
            log_req("physical exercise done")
            init_exercise = time.time()

import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import random
# import pyaudio
# import speech_recognition as sr


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices)
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speech(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour=datetime.datetime.now().hour
    if hour<12:
        engine.say("good morning sir")
        engine.runAndWait()
    if hour>=12 and hour<16:
        engine.say("good afternoon sir")
        engine.runAndWait()
    if hour>16:
        engine.say("good evening sir")
        engine.runAndWait()

#here using this command jarvis take orders

def takecommand():
    # r=sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("listening...")
    #     r.pause_threshold=1
    #     audio=r.listen(source)
    # try:
    #     print("Recognising..")
    #     task=r.recognize_google(audio,language="en-in")
    #     print(f"sir you said {task}")
    # except:
    #     print("sorry sir ,please say it again")
    # engine.say(f'sir you said ,  {task}')
    # engine.runAndWait()
    # return task


    engine.say('please enter your task sir')
    engine.runAndWait()
    try:
        task=input()
    except:
        print("sorry i don't got that")
    engine.say(f'sir your entered  task is ,  {task}')
    engine.runAndWait()
    return task

if __name__=="__main__":
    wishme()
    engine.say("how may i help you")
    engine.runAndWait()

    while True:
      task=takecommand().lower()

     #from here the task of jarvis start
      try:
        if "hello"  in task :
          engine.say("hello to you to Sir")
          engine.runAndWait()

        elif "wikipedia"  in task:
          engine.say("searching wikipedia  please wait")
          engine.runAndWait()
          task=task.replace("wikipedia","")

          result=wikipedia.summary(task,sentences=2)
          print(result)
          engine.say(result)
          engine.runAndWait()

        elif "open youtube"  in task:
          engine.say("opening youtube please wait")
          engine.runAndWait()
          webbrowser.open("youtube.com")
        elif "open google"   in task:
          engine.say("opening google please wait")
          engine.runAndWait()
          webbrowser.open("google.com")


        elif "time" in task:
          current_time=datetime.datetime.now().strftime("%H:%M:%S")
          print(current_time)
          engine.say(f"sir the time is {current_time}")

        elif "music"  in task:
          song_no=random.randint(0,167)

          music_dir= "E:\\samrat\\songs"
          songs=os.listdir(music_dir)
          #print(songs)
          engine.say("playing music for you")
          engine.runAndWait()
          os.startfile(os.path.join(music_dir,songs[song_no]))

        elif "quit" in  task:
            engine.say("bye sir")
            engine.runAndWait()
            break



         #from here the function continues

      except:
           engine.say("sorry sir i can not able to complete your task, please try again")


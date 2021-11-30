
import requests
import json
import pyttsx3

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voices', voices[0].id)

def speech(audio):
   engine.say(audio)
   engine.runAndWait()

if __name__ == "__main__":
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'category=entertainment&'
           'apiKey=7cdb635fb6dc4d38b3fd8b4116238a78')
    response = requests.get(url)
    data = response.text
    # print(data)
    news = json.loads(data)
    # print(news)

    # list of articles
    articles = news["articles"]
    speech("top 10 indian entertainment news are")

    for i in range(0, 10):          #for top 10 news
        news = articles[i]
        news_title = news["title"]
        print(news_title,"\n")
        speech(f"{i+1} : {news_title} \n")     #speak the top 10 news


    speech("thanks for listing all the news carefully")

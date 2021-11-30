import pyttsx3
import PyPDF2

# setting the speech engine and func
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voices', voices[1].id)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speech("hello world")
    # reading the book in binary form them making an object pdfReader and transferring the data to it

    # book = open("xyz" , "rb")
    # pdfReader = PyPDF2.PdfFileReader(book)

    # pages = pdfReader.numPages



    page = pdfReader.getpage(num)
    text = page.extractText()
    speech.(text)

from datetime import datetime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit
import pyautogui
import keyboard
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("your sleep time is my rest time but it's okay, i am still working for you ")
    elif hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 15:
        speak("Good noon")
    elif hour >= 15 and hour < 17:
        speak("Good afternoon")
    elif hour >= 17 and hour < 20:
        speak("Good evening")
    else:
        speak("Good night")
    speak("I am anna, your personal assistant. Please tell me how i may help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        # speak("you said (query)\n")
    except Exception as e:
        # print(e)
        print("Not recognizing!!! say that again")
        return "None"
    return query

def whatsapp():
    speak("tell me the name of the person")
    name = takeBangla()

    if "maa" in name:
        speak("Tell me the message")
        msg = takecommand()
        speak("tell me the time sir")
        speak("time in hour")
        hour = int(takecommand())
        speak("time in minutes!!!")
        minutes = int(takecommand())
        pywhatkit.sendwhatmsg("6297402255",msg,hour,minutes,20)
        speak("Ok sir sending message!!!")

    elif "baba" in name:
        speak("Tell me the message")
        msg = takecommand()
        speak("tell me the time sir")
        speak("time in hour")
        hour = int(takecommand())
        speak("time in minutes!!!")
        minutes = int(takecommand())
        pywhatkit.sendwhatmsg("9064853095",msg,hour,minutes,20)
        speak("Ok sir sending message!!!")

    else:
        speak("Tell me the phone number")
        phone = str(takecommand())
        ph = "+91" + phone
        speak("Tell me the message")
        msg = takeBangla()
        speak("tell me the time sir")
        speak("time in hour")
        hour = int(takecommand())
        speak("time in minutes!!!")
        minutes = int(takecommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, minutes, 20)
        speak("Ok sir sending message!!!")

def takeBangla():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="bn")
        print(f"User said: {query}\n")
        # speak("you said (query)\n")
    except Exception as e:
        # print(e)
        print("Not recognizing!!! say that again")
        return "None"
    return query

def trans():
    #line = str(Text)
    speak("tell me the line")
    line = takeBangla()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak("The translator for this line is" + Text)

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sourodeep168@gmail.com", "Sourodeep@rup")
    server.sendmail("sourodeep8250702644@gmail.com", to, content)
    server.close()

def weather():
    search = "temperature in "
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak(f"The temperature outside is {temperature}")

def openapp():
    speak("wait a minute sir")

    if "open c" in query:
        codepath = "C:\\Users\\USER\\Desktop\\Turbo C++.exe"
        os.startfile(codepath)

    elif "open Pycharm" in query:
        codepath1 = "C:\\program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe"
        os.startfile(codepath1)

    elif "open notepad" in query:
        codepath2 = "notepad.exe"
        os.startfile(codepath2)

    elif "open calculator" in query:
        codepath3 = "calc.exe"
        os.startfile(codepath3)

    elif "open spotify" in query:
        speak("opening....")
        codepath4 = "C:\\Users\\USER\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(codepath4)

    speak("Your command run successfully")

def closeapp():
    speak("ok sir wait a minute")

    if "youtube" in query:
        os.system("TASKKILL /F /im msedge.exe")

    elif "google" in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif "facebook" in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif "stack overflow" in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif "whatsapp" in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif "notepad" in query:
        os.system("TASKKILL /F /im notepad.exe")

    elif "calculator" in query:
        os.system("TASKKILL /F /im calculator.exe")

    elif "c" in query:
        os.system("TASKKILL /F /im Turbo C++.exe")

    elif "pycharm" in query:
        os.system("TASKKILL /F /im pycharm64.exe")

    elif "spotify" in query:
        os.system("TASKKILL /F /im Spotify")

    speak("Your command run successfully")

def youtubeauto():
    speak("What's your command???")
    comm = takecommand()

    if "pause" in comm:
        keyboard.press("space bar")

    elif "play" in comm:
        keyboard.press("space bar")

    elif "restart" in comm:
        keyboard.press("0")

    elif "mute" in comm:
        keyboard.press("m")

    elif "forward" in comm:
        keyboard.press("l")

    elif "backward" in comm:
        keyboard.press("j")

    elif "full screen" in comm:
        keyboard.press("f")

    elif "theater mode" in comm:
        keyboard.press("t")

def reader():
     book = open("E:\\books\\5th semester\\cloud computing\\cloud-computing-bible1.pdf","rb")
     pdfReader = PyPDF2.PdfFileReader(book)
     pages = pdfReader.numPages
     print("Total pages",pages)
     page = pdfReader.getPage(32)
     text = page.extractText()
     speak(text)

def speedtest():
    import speedtest
    speak("checking speed.....")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = float(downloading/800000)
    upload = speed.upload()
    uploading = float(upload/800000)

    if "uploading" in query:
        speak(f"the uploading speed is {uploading} mbps")

    elif "downloading" in query:
        speak(f"the downloading speed is {correctDown} mbps")

    else:
        speak(f"the downloading speed is {correctDown} mbps and the uploading speed is {uploading} mbps")



if __name__ == "__main__":
    # speak("hello sourodeep")
    wishme()
    while True:
        query = takecommand().lower()

        # logic
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "who invented you" in query:
            speak("i am invented by Mr. Sourodeep Chakraborty")

        elif "who is your boyfriend" in query:
            speak("my inventor Sourodeep Chakraborty")

        elif "play music" in query:
            speak("playing....")
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "how are you" in query:
            speak("I am fine...you are very kind to ask,especially in these tempestuous time")

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        elif "email" in query:
            try:
                speak("What should i say??")
                content = takecommand()
                to = "sourodeep8250702644@gmail.com"
                sendemail(to, content)
                speak("Email has been send...")

            except Exception as e:
                print(e)
                speak("Sorry i am not able to send this Email")

        elif "i love you" in query:
            speak("I like you but i love only my owner and my works and i am a loyalist so i can't love you... and i also know, you have an another girl friend. so if you need any tips, i can suggest or advice you")

        elif "owner" in query:
            speak("Thank you for creating me...")

        elif "jokes" in query:
            speak("saying...")
            tts = pyttsx3.init()
            jokes = pyjokes.get_joke()
            print(jokes)
            tts.say(jokes)
            tts.runAndWait()

        elif "bye" in query:
            speak("BYE!!!!!!")
            speak("you can call me anytime")
            break

        elif "youtube search" in query:
            speak("ok sir, this is what i found you for your search")
            #query = query.replace("","")
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query=" + query
            speak("Done sir!!!")

        elif "google search" in query:
            speak("this is what i founnd for you sir!!!")
         #   query = query.replace("","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("Done Sir!!!")

        elif "website" in query:
            speak("Okay sir, Launching...")
            query = query.replace("website","")
            query = query.replace(" ", "")
            web1 = query.replace("Open", "")
            web2 = "https://www."+web1+".com"
            webbrowser.open(web2)
            speak("Launched...")

        elif "launch" in query:
            speak("tell me the name of the web site")
            name = takecommand()
            web = "https://www."+name+".com"
            webbrowser.open(web)
            speak("Done sir!!!")

        elif "whatsapp message" in query:
            whatsapp()

        elif "screenshot" in query:
            speak("ok sir what should i name that file")
            path = takecommand()
            path1name = path + ".png"
            path1 = "E:\\screenshot\\" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("E:\\screenshot")
            speak("here is your screenshot")

        elif "open c" in query:
            openapp()

        elif "open notepad" in query:
            openapp()

        elif "open pycharm" in query:
            openapp()

        elif "open calculator" in query:
            openapp()

        elif "open spotify" in query:
            openapp()

        elif "close c" in query:
            closeapp()

        elif "close notepad" in query:
            closeapp()

        elif "close pycharm" in query:
            closeapp()

        elif "close calculator" in query:
            closeapp()

        elif "close spotify" in query:
            closeapp()

        elif "close youtube" in query:
            closeapp()

        elif "close google" in query:
            closeapp()

        elif "close stackoverflow" in query:
            closeapp()

        elif "close facebook" in query:
            closeapp()

        elif "open whatsapp" in query:
            closeapp()

        elif "pause youtube" in query:
            youtubeauto()

        elif "forward youtube" in query:
            youtubeauto()

        elif "backward youtube" in query:
            youtubeauto()

        elif "restart youtube" in query:
            youtubeauto()

        elif "mute youtube" in query:
            youtubeauto()

        elif "full youtube" in query:
            youtubeauto()

        elif "theater youtube" in query:
            youtubeauto()

        elif "play youtube" in query:
            youtubeauto()

        elif "repeat my word" in query:
            speak("Speak sir!!!")
            com = takecommand()
            speak(f"you said: {com}")

        elif "home location" in query:
            speak("please sir wait for a minute...........")
            speak("opening...")
            webbrowser.open("https://www.google.co.in/maps/@22.6633744,88.3862187,17z")

        elif "alarm" in query:
            '''speak("Enter the time: ")
            time = input(": Enter the time :")

            while True:
                Time_ac = datetime.datetime.now()
                now = Time_ac.strftime("%H:%M:%S")

                if now == time:
                    speak("time to wake up sir!!")
                    playsound("Untill I found you ! Female Version.mp3")
                    speak("Alarm Closed")

                elif now > time:
                    break'''

            speak("Sir please tell me the time to set alarm, for example, set alarm to 5:30 a.m.")
            tt = input(": Enter the time :")
            tt = tt.replace("set alarm to" , "")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        elif "translator" in query:
            trans()

        elif "remember that" in query:
            rememberMsg = query.replace("remember that","")
            speak("you tell me to remind you that: " + rememberMsg)
            remember = open("date.txt","w")
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in query:
            remember = open("date.txt","r")
            speak("you tell me that: " + remember.read())

        elif "temperature" in query:
            weather()

        elif "audiobook" in query:
            reader()

        elif "downloading speed" in query:
            speedtest()

        elif "uploading speed" in query:
            speedtest()

        elif "internet speed" in query:
            speedtest()


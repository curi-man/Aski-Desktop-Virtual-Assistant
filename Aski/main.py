

import numpy as np
import pyscreenshot
import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
from pydictionary import Dictionary
import wikipedia
import webbrowser
import subprocess
import requests
import time
import pyjokes
import os
import json
import smtplib
import ctypes
from translate import Translator
from tkinter import *
from playsound import playsound
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Aski Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivamnegi923@gmail.com', 'shivam923@')
    server.sendmail('shivamnegi923@gmail.com', to, content)
    server.close()

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def findAvailability(pincode, date):
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,date)
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    # for x in range(6):
    #     speak(x)
    for each in data:
        print("Name : " + each["name"])
        print("Address : " + each["address"])
        print("Available Capacity dose 1: ", each["available_capacity_dose1"])
        print("Available Capacity dose 1: ", each["available_capacity_dose2"])
        print("Free/Paid : " + each["fee_type"])
        print("Type : " + each["vaccine"])
        print('-------------------------------------------------------------------------------------')

def process_audio():
  wishMe()
  if __name__ == '__main__':
     while True:
     # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")

        elif 'search' in query:
            query = query.replace("search", "")
            speak("this is what i found on google about " +  query)
            webbrowser.open('https://www.google.com/search?q=' + query)

        elif 'stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")


        elif 'music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'videos' in query:
            videos_dir = 'D:\\Videos'
            videos = os.listdir(videos_dir)
            print(videos)
            os.startfile(os.path.join(videos_dir, videos[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'calculator' in query:
            os.startfile('C:\\Windows\\System32\\calc.exe')

        elif 'screenshot' in query:
            image = pyscreenshot.grab()
            image.show()
            image.save("image.png")

        elif 'notes' in query:
            speak("What should I note?")
            notes = takeCommand()
            file1 = open("myfile.txt", "w")
            file1.writelines(notes)
            file1.close()
            file1 = open("myfile.txt", "r+")

           # Not working
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif 'translator' in query:
            speak("To which language")
            lang = takeCommand()
            translator = Translator(from_lang = "English", to_lang=lang)
            speak("What do you want to translate in" + lang)
            topic = takeCommand()
            translation = translator.translate(topic)
            speak(translation)
            print(translation)

        elif "location of" in query:
            query = query.replace("location of", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif 'who are you' in query:
            speak("I am aski. An AI Virtual Assistant build by three students of Dronacharya Group of Institutions namely shivam, rishabh and rishu")
            print("I am aski. An AI Virtual Assistant build by three students of Dronacharya Group of Institutions namely shivam, rishabh and rishu")

        elif 'how are you' in query:
            speak('I am fine.Thank you')
            print('I am fine.Thank you')
        elif 'can you entertain me' in query:
            speak('Yes, you can ask me to play music, open youtube videos and I can tell you a joke also.')
            print('Yes, you can ask me to play music, open youtube videos and I can tell you a joke also.')

        elif 'sublime' in query:
            path = "C:\Program Files\Sublime Text\sublime_text.exe"
            os.startfile(path)

        elif 'code' in query:
            speak("opening vs code")
            path = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(path)

        elif 'meaning' in query:
             word = query.replace("meaning of", "")
             webbrowser.open('https://dictionary.cambridge.org/dictionary/english/' + word)

        elif 'intellij idea' in query:
            path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3\\bin\\idea64.exe"
            os.startfile(path)

        elif 'screen recording' in query:
            path = "C:\\Program Files\\Bandicam\\bdcam.exe"
            speak("opening files")
            os.startfile(path)

        elif 'files' in query:

            path = "C:"
            speak("opening files")
            os.startfile(path)

        elif 'telegram' in query:
            path = "C:\\Users\\admin\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(path)

        elif 'project' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\admin\\Documents\\Project.pptx"
            os.startfile(power)

        elif 'send message to Rishabh' in query:

            contacts = {
                "Rishabh": 7011933513,
                "rishu": 7678947597,
                "bikram": 8851251654,
                "shivam": 7900415347
            }
            num = 7011933513
            speak("Tell me the message for")
            mes = "hi"
            whatsapp.whatsapp(num, mes)


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shovitnegi123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, but I am not able to send this email")

        elif 'power off' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'news' in query:
          speak("opening newspaper")
          webbrowser.open("https://www.thehindu.com/")

        elif "calendar" in query:
            speak("Opening calendar")
            webbrowser.open("https:/calendar.google.com/calendar")

        elif "weather of" in query:
            query = query.replace("weather of", "")
            location = query
            speak("user asked to find the weather of")
            speak(location)
            webbrowser.open("https://www.google.com/search?q=" + "weather of" + location)

        elif 'Word file' in query:
            os.startfile('C://Users//admin//PycharmProjects//Aski//MS file.docx')

        elif 'vaccine' in query:
            speak("Please provide pincode")
            content = takeCommand()
            pincode = int(content)
            today = date.today()
            taarikh = today.strftime("%d-%m-%Y")
            findAvailability(pincode, taarikh)

        elif 'joke' in query:
            code = pyjokes.get_joke()
            print(code)
            speak(code)


def main_screen():
    global screen
    screen = Tk()
    screen.title("Aski")
    screen.geometry("520x520")
    screen.iconbitmap('icon-img.ico')

    name_label = Label(text="Aski", width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    Image = PhotoImage(file="mic.png")

    Image_button = Button(image=Image, command=process_audio)
    Image_button.pack(pady=10)

    screen.mainloop()


main_screen()
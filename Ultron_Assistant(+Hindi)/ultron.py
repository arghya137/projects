import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pywikihow
import requests
import os
import sys
import cv2
import speedtest
from requests import get
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
    
    speak("I am ultron. How may I help you?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:

        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'who is' in query:
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if 'how are you' in query:
            speak('I am well and good. What about you sir?')

        elif 'what is' in query:
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'where is' in query:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Google")
            print(results)
            speak(results)

        elif 'temperature' in query:
            url=f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"{temp}")
        
        elif 'how to' in query:
            how=query
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Sir, What should I search?")
            search=takeCommand().lower()
            webbrowser.open(f"{search}")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play' in query:
            speak('playing')
            query=query.replace("play", "")
            pywhatkit.playonyt(query)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'send email' in query:
            webbrowser.open("gmail.com")
        
        elif 'take screenshot' in query:
            pywhatkit.take_screenshot(query)
        
        elif 'open whatsapp' in query:
            pywhatkit.open_web()

        elif 'open wordpad' in query:
            npath="C:\\Users\\KIIT\\AppData\\Local\\Microsoft\\WindowsApps\\uwp_wpsoffice.exe"
            os.startfile(npath)
        
        elif 'open github' in query:
            npath="C:\\Users\\KIIT\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system("start cmd")
        
        elif 'open camera' in query:
            cam=cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('webcam', img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cam.release()
            cv2.destroyAllWindows()
        
        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"Device's IP address is {ip}")
        
        elif 'internet speed' in query:
            st=speedtest.Speedtest()
            dl=st.download()
            up=st.upload()
            speak(f'Sir! your internets download speed is {dl} bit per second and uploading speed is {up} bit per seconds')
            print('Downloading speed= {dl} bit per second and uploading speed is {up} bit per seconds')

        elif 'ultron stop' in query:
            speak("okay sir!")
            sys.exit()
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #hey this is jarvis






def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        r.pause_threshold = 1
        r.energy_threshold=500
        audio=r.listen(source)

    try:
        print('Recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f'user said: {query}')

    except Exception as e:
        print('Say that again please...')
        return 'None'

    return query


if __name__=="__main__":
    
    takecommand()
            

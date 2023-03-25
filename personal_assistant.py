
import datetime
import webbrowser
import os
import sys 
import pyttsx3
import wikipedia
import speech_recognition as sr
import pyaudio                        

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good morning")
    elif hour>12 and hour<18 :
        speak("good afternoon")
    else:
        speak("good evening")   

    speak("hey aishu")
    speak("this is max here how can i help you") 


def takecommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listening.....")
        r.pause_threshold = 1   
        audio = r.listen(source) 
    try :
        print("recognizing.....")
        query = r.recognize_google(audio,language="en-in")   
        print("user said:",query)
    except Exception as e :
        print(e)
        speak("say again please.....")
        return "none" 
    return query 

if __name__ == '__main__'  :
    wishme(datetime)

    if 1 :
        query = takecommand().lower()
        if 'wikipedia' in query :
            speak("searching wikipedia..... please wait for a moment ")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak=("according to wikipedia") 

            print(results) 
        elif 'open google' in query :
            speak("opening google.....")
            webbrowser.open("google.com")

        elif 'open youtube' in query :
            webbrowser.open("youtube.com")

        elif 'open command prompt' in query :
            os.system('start cmd')

        elif 'open stackoverflow' in query :
            webbrowser.open("stackoverflow.com")

        elif 'open calendar' in query :
            webbrowser.open("calender.com")

        elif 'time' in query :
            strtime=datetime.datetime.now().strftime("%h:%m:%S")
            speak(f"Aishu the time is {strTime}")

        elif 'say' in query :
            speak(query[4:])    

        elif 'about me' in query :
            speak("Aishu is the best girl in this world")
            speak("She have the world's purest heart")
            speak("I am lucky to have her as a best friend")
            speak("I will always obey her words")
            speak("I will always praise her")
            speak("I am the mental stupid idiot everything")
            speak("But not aishu")  
            speak("she is a cutie pie")  
            speak("now say me do you need any help")
        
        elif 'no thanks' in query :
            speak("thank you waiting for your commands... have a nice day")
    
                
    sys.exit()                        

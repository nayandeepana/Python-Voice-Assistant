import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import random
import COVID19Py
import sys

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

    speak("I am Friday Sir. Please tell me how may I help you")    

def calcu():
    speak("What's the first number ")
    a=takeCommand()
    speak("What's the secound number ")
    b=takeCommand()
    speak("what do you want to do")
    i=takeCommand()

    if i == 'addition':
        r=int(a)+int(b)
    elif i == 'subtraction':
        r=int(a)-int(b)
    elif i == 'division':
        r=int(a)/int(b)
    elif i == 'multiplication':
        r=int(a)*int(b)
    
    speak('The Answer is ')
    speak(r)

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

    except Exception:
        #print(e)          
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'covid' in query:
             webbrowser.open("https://www.mygov.in/covid-19")
             speak("Government of India is taking all necessary steps and prepared well to face the challenge of growing Corona Virus.")

        elif 'play music' in query:
            speak("Playing Music")
            music_dir = 'C:\\Users\\nayan\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'random' in query:
            rand=(random.randint(0,100))
            speak(rand)
        
        elif 'calculate' in query:
            calcu()
        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'who are you' in query:
            speak("I am friday, Your personal Assistant sir, i can help you find answers, get thing done")

        elif 'open code' in query:
            codePath = "C:\\Users\\nayan\\AppData\\Local\\Programs\\Microsoft VS Code.exe"
            os.startfile(codePath)
        

        elif 'email to nayan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nayandeep06@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    
        elif 'bye bye' in query:
            speak("Bye sir Have a good day.")
            sys.exit()
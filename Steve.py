import datetime
import webbrowser
import os
import smtplib
import wikipedia
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id) # To check voices available on computer.
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''This function will give audio as an output.'''

    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function will greet end user and introduce itself when called.'''

    hour = int(datetime.datetime.now().hour) # Will fetch time from datetime module.

    if hour>= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Steve Sir. Please tell me how may I help you.") # AI intro.

def takeCommand():
    '''It takes microphone input from the user and returns string output.'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recogninzing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) # Will print exception/error.
        print("Say that again please...")
        return "None"
    return query

##### Not Working #####
# def sendEmail(do, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('rhitik252@gmail.com', password.password)
#     server.sendmail('rhitik252@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tesks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikepedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia, ")
            speak(results)
            print(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open stackoverflow' in query:
          webbrowser.oprn("stackoverflow.com")
            
        elif 'open google' in query:
            webbrowser.oprn("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\rhiti\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\rhiti\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'open spotify' in query:
            codepath = "C:\\Users\\rhiti\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codepath)

        elif 'quit' or 'exit' in query:
            quit()


        #### Not Working, function sendEmail ##### 
        # elif 'email to john' in query:
        #     try:
        #         speak("What should I say? ")
        #         content = takeCommand()
        #         to = "rhitik02@gmail.com"
        #         smtplib.sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, there was a problem while sending your email, try again after some time.")
                
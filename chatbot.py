import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
# voices[0] for boys and voices[1] for girls
engine.setProperty('voice', voices[0].id) #or engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning my dear!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon my dear!")
    
    else:
        speak("Good Evening my dear!")

    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')   #Using google for voice recognition
        #query = r.recognize_google(audio, language='hi-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        speak("Say that again please...") #Say that again will be printed in case of improper voice
        return "None" #None string will be returned    
    return query 

if __name__=="__main__" :
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
#    speak("bhavya is a cooldood")

        # Logic for executing tasks based on query
        if 'wikipedia' in query: #if wikipedia found in the query then this block will be executed 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtue")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'F:\\bhavya\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open gamil' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening mail")

        elif 'open gyan ghar' in query:
            webbrowser.open("https://jaagovarna.blogspot.com/")
            speak("opening your site")

        elif 'make you' in query or 'create you' in query or 'develop you' in query or 'who developed you' in query or 'who made you' in query:
            ans = "For your information ! bhavya goyal created me ! I give a lot of thanks to him"
            print(ans)
            speak(ans)

        elif 'who are you' in query or 'about you' in query or 'your details' in query or 'your intro' in query:
            about = "Very Strange ! I gave my intro in beginning where is your concentration ! i think you are not concentrated on you studies too ! Anyway I am Jarvis an AI based computer program or virtual assistant ! work on ten giga bytes memory but i can help you lot ! like searching anything from wikipedia"
            print(about)
            speak(about)

        elif 'hello jarvis' in query or 'hello' in query:
            hel = "Hello Sir ! How may i help you..."
            print(hel)
            speak(hel)

        elif 'your name' in query or 'your sweet name' in query:
            name = "Very Strange ! I gave my intro in beginning where is your concentration ! i think you are not concentrated on you studies too ! Anyway Thanks for asking my name ! i am your virtual assistant name Jarvis"
            print(name)
            speak(name)

        elif 'your hobby' in query:
            ho = "My hobby is only listening you ! and giving your answers what you have asked from me ! by the process of identification..."
            print(ho)
            speak(ho)

        elif 'you feeling' in query:
            feel = "Very boring in computer because i have lost my interst by doing the same work again n again"
            print(feel)
            speak(feel)

        elif 'What\'s up' in query or 'how are you' in query:
            msg = ['just doing my thing!', 'I am fine! What about you', 'I am fine and full of electricity', 'How are you']
            ans_y = random.choice(msg)
            speak(ans_y)
            print(ans_y)


        elif 'shutdown' in query:
            speak("Shutting down your PC")
            os.system('sleep -s')

        elif query == 'none':
            continue
        
        elif 'exit' in query or 'abort the program' in query or 'stop this' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'I am feeling well after meeting you ! but you are going ! feel bad ! anyway ! feel nice with meeting you'
            speak(ex_exit)
            exit()

        else:
            exit()    


 




import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    print("I am VAIR. How may i help you!")
    speak("I am Vair. your personal assistant. How may i help you!")


def takeCommand():
    # it take input using microphone from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-GB')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Unable to understand you sir... can you please repeat")
        speak("Unable to understand you sir... can you please repeat")
        return "None"
    return query


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('Enter mail ID', 'Enter Mail ID Password')
#     server.sendmail('Re-enter Mail ID', to, content)
#     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        anyNum = random.randint(1, 3)
        randNum = random.randint(1, 2)
        randNumber = random.randint(1, 100)

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("... What more can i do for you sir?")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("... What more can i do for you sir?")

        elif 'open google' in query:
            webbrowser.open("google.co.in")
            speak("... What more can i do for you sir?")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("... What more can i do for you sir?")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
            speak("... What more can i do for you sir?")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("... What more can i do for you sir?")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("... What more can i do for you sir?")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            speak("... What more can i do for you sir?")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
            speak("... What more can i do for you sir?")

        elif 'play music' in query:
            speak("lets me play some jazz for you!")
            music_dir = 'S:\\Personal\\2.0\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is {strTime}")
            speak(f"Sir the time is {strTime}")
            speak("or you could have seen it in the right below corner! you LAZY FUCK!")

        elif 'open code' in query:
            codePath = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Anything else?")
            exit()

        elif 'open brave' in query:
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
            if anyNum == 1:
                speak(
                    "This browser is three times faster than Google Chrome, Just saying")
            else:
                speak("always remember to clear your browser history! Just saying")
            exit()

        elif 'email to jay' in query:
            try:
                print("What should i say?")
                speak("What should i say?")
                content = takeCommand()
                to = "jaysangani04@gmail.com"
                sendEmail(to, content)
                print("The Email is sent!")
                speak("The Email is sent!")

            except Exception as e:
                print(e)
                print("SORRY! sir. I am not able to sent Email.")
                speak("SORRY! sir. I am not able to sent Email.")

        elif 'love you' in query:
            if anyNum == 1:
                print("well who doesn't?")
                speak("well who doesn't?")
            elif anyNum == 2:
                print("Thanks, I'm flattered, but I'm not interested")
                speak("Thanks, I'm flattered, but I'm not interested")
            else:
                print(
                    "I'm not interested in dating right now, but thanks that meant a lot.")
                speak(
                    "I'm not interested in dating right now, but thanks that meant a lot.")


        elif 'why is' in query:
            print("VAIR name was given to me on 4th june 2021 by Jay Sangani. VAIR stands for Virtual Assistant In Reality")
            speak("VAIR name was given to me on 4th june 2021 by Jay Sangani. VAIR stands for Virtual Assistant In Reality")
        elif 'why your' in query:
            print("VAIR name was given to me on 4th june 2021 by Jay Sangani. VAIR stands for Virtual Assistant In Reality")
            speak("VAIR name was given to me on 4th june 2021 by Jay Sangani. VAIR stands for Virtual Assistant In Reality")

        elif 'your name' in query:
            print("Hi! I am VAIR. Born on 1 june 2021. created by Jay Sangani.")
            speak("Hi! I am VAIR. Born on 1 june 2021. created by Jay Sangani")

        elif 'hello' in query:
            print("Namaste")
            speak("Namaste")
            print("🙏")

        elif 'tata' in query:
            print("Signing off! have a great day, sir!")
            speak("Signing off! have a great day, sir!")
            exit()

        elif 'can you do' in query:
            print('''try saying 'open' and any 'popular social media site' i will open it in the browser
            try asking me to sing a song, or ask about myself, or lets play a game or  let me toss a coin for you,
            you can also ask me to send an email in behalf of you, i can open your browser and also vs code where i was born!
            Be aware of talking bullshit to me i can burn you with my words. Good day sir''')
            speak('''try saying 'open' and any 'popular social media site' i will open it in the browser
            try asking me to sing a song, or ask about myself, or lets play a game or  let me toss a coin for you,
            you can also ask me to send an email in behalf of you, i can open your browser and also vs code where i was born!
            Be aware of talking bullshit to me i can burn you with my words. Good day sir''')

        elif 'toss a coin' in query:
            if randNum == 1:
                print("HEADS it is")
                speak("heads it is")
            else:
                print("TAILS it is")
                speak("tails it is")

        elif 'play a game' in query:

            speak("GAME 1. for number guessing game and GAME 2. for snake water gun")
            choice = takeCommand()
            if choice == 'game 1':
                print('''Its a simple guessing game, where you have to guess 
                a number between, 1 to 100, in minimum guesses, 
                and hint will be given after each guess''')
                speak('''Its a simple guessing game, where you have to guess a number between, 
                1 to 100, in minimum guesses, 
                and hint will be given after each guess''')
                userGuess = None
                guesses = 0
                speak("guess a number!")
                
                while(userGuess != randNumber):
                    try:
                        userGuess = int(takeCommand())
                    except Exception as e:
                        speak("can you be more clear please")
                    guesses += 1
                    if (userGuess == randNumber):
                        print("YOU GUESSED IT RIGHT!!! YOU WON!!!")
                    else:
                        if (userGuess < randNumber):
                            print("GUESS A LARGER NUMBER")
                            speak("GUESS A LARGER NUMBER")
                        else:
                            print("GUESS A SMALLER NUMBER")
                            speak("GUESS A SMALLER NUMBER")

                print(f"YOU GUESSED THE CORRECT NUMBER IN {guesses} GUESSES")
                speak(f"YOU GUESSED THE CORRECT NUMBER IN {guesses} GUESSES")
                exit()
            
            else:
                def gameWin(computer, you):
                    if computer == you:
                        return None
                    elif computer == 'S':
                        if you == 'W':
                            return False
                        elif you == 'G':
                            return True

                    elif computer == 'W':
                        if you == 'G':
                            return False
                        elif you == 'S':
                            return True
                    
                    elif computer == 'G':
                        if you == 'S':
                            return False
                        elif you == 'W':
                            return True

                random_number = random.randint(1, 3)
                if random_number == 1:
                    computer = 'S'
                elif random_number == 2:
                    computer = 'W'
                elif random_number == 3:
                    computer = 'G'

                speak("choose Snake, Water or gun")
                you = takeCommand().lower()
                
                print(f"computer chose- {computer}")
                print(f"you chose- {you}")

                if you == 'water':
                    you = 'W'
                elif you == 'gun':
                    you = 'G'
                elif you == 'snake':
                    you = 'S'

                a = gameWin(computer, you)

                if a == None:
                    print("This game is a tie!")
                    speak("This game is a tie!")
                elif a == True:
                    print("you Won!")
                    speak("you Won!")
                else:
                    print("you Lose!")
                    speak("you Lose!")


        elif 'v a i r' in query:
            print("VAIR stands for Virtual Assistant In Reality")
            speak("VAIR stands for Virtual Assistant In Reality")

        
        elif 'choose a number' in query:
                print("From?")
                speak("From?")
                num1 = (takeCommand())
                print(f"from {num1} to?")
                speak(f"from {num1} to?")
                num2 = (takeCommand())
                print("try again")
                speak("try again")
                chooseNumber = random.randint(num1, num2)
                print(f"I choose {chooseNumber}")
                speak(f"I choose {chooseNumber}")


        

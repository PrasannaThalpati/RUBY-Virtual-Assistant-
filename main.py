# Author : Prasanna Thalpati

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ruby' in command:
                command = command.replace('ruby', '')
                print(command)


    except:
        pass
    return command

def run_ruby():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing !!!' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M,%p')
        print(time)
        talk('current time is ' + time )
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with a wifi')
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    else:
        talk('sorry ! please repeat...')


while True:
    talk('Hello  Prasanna !!!')
    talk('I am RUBY your virtual assistant here, how can I help you ?')
    run_ruby()
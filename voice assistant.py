import smtplib
import pywhatkit
import speech_recognition as sr
import subprocess
import datetime
import wikipedia
import webbrowser
import sys
import pyautogui
import os
import time
def say(text):
    subprocess.call(['say', text])
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        say("Good Afternoon")
        print("Good Afternoon")
    else:
        say("Good Evening")
        print("Good evening")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising.....")
        voice_data=r.recognize_google(audio,language='en-in')
        print("user said:",voice_data)
    except Exception as e:
        say("I didn't understand Can you please repeat Again")
        print("I didn't understand Can you please repeat Again")
        return "None"
    return voice_data
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('virtualassistant0@gmail.com','Virtualps@123')
    server.sendmail('virtualassistant0@gmail.com',to,content)
    server.close()

if _name=="main_":
    wish()
    say("How can i help you")
    print("How can i help you")
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    contacts={"lj":"+918923066771","dj":"+918012437355","sj":"+917626845144"}
    while True:
        voice_data=takecommand().lower()
        if 'wikipedia' in voice_data:
                say("Searching wikipedia")
                print("Searching on wikipedia.......")
                voice_data=voice_data.replace("wikipedia","")
                results=wikipedia.summary(voice_data,sentences=2)
                say("According to Wikipedia")
                print(results)
                say(results)
        elif 'open youtube' in voice_data:
            say("What should i search on youtube")
            print("What should i search on youtube")
            voice_data = takecommand().lower()
            pywhatkit.playonyt(voice_data)
        elif 'screenshot' in voice_data:
            say("Sir for what name i will save screenshot file")
            name=takecommand().lower()
            say("Wait for a second sir I am taking screenshot")
            time.sleep(2)
            ss=pyautogui.screenshot()
            ss.save(f"{name}.png")
            say("Done sir Now I am ready for next command")
        elif 'open mail' in voice_data:
            webbrowser.open("https://mail.google.com")
            say("Google Mail open now")
            time.sleep(5)
        elif 'open google' in voice_data:
                say("What should i search on google")
                voice_data = takecommand().lower()
                pywhatkit.search(voice_data)
                say("Searching")

        elif 'open chandigarh university management system' in voice_data:
                webbrowser.open("https://uims.cuchd.in/uims/")
        elif 'open blackboard' in voice_data:
                webbrowser.open('https://cuchd.blackboard.com')
        elif 'open stack overflow' in voice_data:
                webbrowser.open('https://stackoverflow.com')
        elif 'the time' in voice_data:
            m_time=datetime.datetime.now().strftime('%H:%M:%S')
            say(f"Sir The time is {m_time}")
        elif 'quit'  in voice_data:
            say("Quitting")
            print("Quitting....")
            sys.exit()
        elif 'sleep'  in voice_data:
            say("Sleeping")
            print("Sleeping....")
            sys.exit()
        elif 'you can sleep' in voice_data:
            say("sleeping")
            print("Sleeping..")
            sys.exit()
        elif 'Prime Minister' in voice_data:
            say(" Mister Madan Joshi")
        elif 'Pyaar' or 'pyar' in voice_data:
            say("Madan Joshi I Love You")
        elif 'open terminal' in voice_data:
            os.system('open -a Terminal .')

        elif 'send message' in voice_data:
            say("Sir whom i will send")
            print(contacts.keys())
            try:
                voice_data=takecommand().lower()
                a = contacts[voice_data]
                print(a)
                say("Sir What should i say")
                voice_data=takecommand().lower()
                hour=datetime.datetime.now().hour
                minute=(datetime.datetime.now().minute + 1)
                pywhatkit.sendwhatmsg(a,voice_data,hour,minute)
            except Exception as e:
                say("Sorry There might be some connectivity issue")
        elif 'play music' in voice_data:
            try:
                say("Which song do you want to listen")
                voice_data=takecommand().lower()
                pywhatkit.playonyt(voice_data)
                say("Playing..")
            except Exception as e:
                say("Network error")
        elif "wait for few seconds" in voice_data:
            say("Waiting..")
            time.sleep(30)
            say("Shall we start now")
        elif "wait" in voice_data:
            say("Waiting..")
            time.sleep(30)
            say("Shall we start now")
        elif 'send email' in voice_data:
            try:
                say("What should i say")
                content=takecommand().lower()
                to='saurabhjoshi686@gmail.com'
                sendmail(to,content)
                say("Email has been sent")
            except Exception as e:
                print(e)
                say("Sorry email has not been sent")
        elif 'hello' or 'good' in voice_data:
            print("How may i help you ")
            say("How may i help you ")
        elif 'fine' or 'good' in voice_data:
            say("Tell me  what can i do for you")






        say("What can i do more for you")
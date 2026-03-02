import pyttsx3 
import requests
import speech_recognition
from bs4 import BeautifulSoup
import datetime
import pyautogui
import os
import speedtest
import pandas as pd
import wolframalpha

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source: 
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def get_command():
    typed = input("Type your command: ").strip()
    return typed.lower()

if __name__ == "__main__":
    while True:
        # query = takeCommand().lower()
        query = get_command()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()   
        elif "hey" in query:
            from GreetMe import greetMe
            greetMe()     

            while True:
                # query = takeCommand().lower()
                query = get_command()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                elif "hello" in query:
                    speak("hello sir, how are you ?")
                elif "hi" in query:
                    speak("hello sir, how are you ?")    
                elif "i am fine" in query or "i m fine" in query or "am fine" in query or "m fine" in query or "me theek hu" in query or "me thik hu" in query or "i am good" in query or "i m good" in query or "me bhi theek hu" in query or "me bhi thik hu" in query or "me acha hu" in query or "me bhi acha hu" in query:
                    speak("that's fantastic, sir")
                # elif "i m fine" in query:
                #     speak("thats's fantastic sir")
                # elif "am fine" in query:
                #     speak("thats's fantastic sir")
                # elif "m fine" in query:
                #     speak("thats's fantastic sir")    
                elif "how are you" in query or "how r u" in query or "how" in query:
                    speak("as always, awesome sir")
                elif "kaise ho" in query or "tum kaise ho" in query:
                    speak("i am good, sir")
                elif "kya haal hai" in query or "kya hal hai" in query:
                    speak("everything is functioning well sir")
                # elif "kya hal hai" in query:
                #     speak("everything is functioning well sir")
                # elif "how r u" in query:
                #     speak("as always , awesome sir")                    
                # elif "tum kaise ho" in query:
                #     speak("i am good, sir")
                elif "thank you" in query or "thank u" in query or "thanks" in query or "thank" in query or "shukriya" in query or "sukriya" in query:
                    speak("you are welcome sir") 
                # elif "thank u" in query:
                #     speak("you are welcome sir") 
                # elif "thanks" in query:
                #     speak("you are welcome sir")
                # elif "thank" in query:
                #     speak("you are welcome sir")                       
                elif "how was your day" in query or "how's your day" in query or "how is your day" in query or "tumhara din kaisa tha" in query or "tumhara din kaisa gaya" in query:
                    speak("mostly sleeping sir, as device was shut downed")
                # elif "how's your day" in query:
                #     speak("mostly sleeping sir, as device was shut downed")
                # elif "how is your day" in query:
                #     speak("mostly sleeping sir, as device was shut downed")
                # elif "tumhara din kaisa tha" in query:
                #     speak("mostly sleeping sir, as device was shut downed")
                # # elif "tumhara din kaisa gaya" in query:
                # #     speak("mostly sleeping sir, as device was shut downed")
                elif "what are you doing" in query or "what r u doing" in query or "tum kya kar rahe ho" in query or "kya kar rahe ho" in query:
                    speak("nothing great, listening to you, sir")
                # elif "what r u doing" in query:
                #     speak("nothing great, listening to you, sir")
                elif "what can you do" in query or "what things can you do" in query or "tum kya kar sakte ho" in query or "tum kya kya kar sakte ho" in query:
                    speak("whatever you taught to me, sir")
                # elif "what things can you do" in query:
                #     speak("whatever you taught to me, sir")
                # elif "tum kya kar sakte ho" in query:
                #     speak("whatever you taught to me, sir")
                elif "can you shut down my pc" in query or " can you shut down my laptop" in query or "can you shut down my system" in query or "can you shut down my" in query:
                    speak("of course sir, on your command")
                # elif "can you shut down my laptop" in query:
                #     speak("of course sir, on your command")
                elif "kya tum mera laptop band kar sakte ho" in query or "tum mera laptop band kar sakte ho" in query:
                    speak("of course sir, on your command")
                elif "are you listening" in query or "kya tum mujhe sun rahe ho" in query:
                    speak("yes sir, I am listening.")
                                                        
                                         
                elif "pause" in query or "video pause kar do" in query or "video pause karo" in query or "pause kar do" in query or "pause karo" in query or "rok do" in query or "band kar do" in query or "video rok do" in query or "video band kar do" in query or "stop video" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query or "video play karo" in query or "video play kar do" in query or "play kar do" in query or "play karo" in query or "chalu kar do" in query or "chalu karo" in query or "video chalu kar do" in query or "video chalu karo" in query or "start video" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "move backward" in query or "piche jao" in query or "thoda piche jao" in query:
                    pyautogui.press("j")
                elif "skip forward" in query or "aage badho" in query or "aage badh" in query or "thoda aage badho" in query or "thoda aage badh" in query:
                    pyautogui.press("l") 
                elif "next video" in query or "agali video chalao" in query or "agali video start karo" in query or "agali video dikhao" in query:
                    pyautogui.press("N") 
                # elif "play previous video" in query:
                #     pyautogui.press("P")
                elif "increase rate" in query or "video tej karo" in query or "tej karo" in query:
                    pyautogui.press(">")  
                elif "decrease rate" in query:
                    pyautogui.press("<") 
                elif "full screen" in query or "ful screen" in query or "full screen karo" in query or "ful screen karo" in query:
                    pyautogui.press("f")
                elif "theatre mode" in query or "theatre mod" in query or "theatre mode on karo" in query or "theatre mode karo" in query or "theatre mod on karo" in query or "theatre mod karo" in query:
                    pyautogui.press("t")
                elif "theatre mod" in query:
                    pyautogui.press("t")   
                elif "volume up" in query or "awaaz badhao" in query or "aur awaaz badhao" in query or "aur awaaz badha" in query or "awaaz badha" in query:
                    from keyboard import volumeup
                    # speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query or "aur awaaz kam karo" in query:
                    from keyboard import volumedown
                    # speak("Turning volume down, sir")
                    volumedown()


                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")
                elif "open" in query:
                    from DictApp import openappweb
                    openappweb(query)
                elif "close" in query or "band karo" in query:
                    from DictApp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                # elif "wikipedia" in query:
                #     from SearchNow import searchWikipedia
                #     searchWikipedia(query)


                elif "calculate" in query:
                    from calculate import wolframalpha
                    from calculate import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "send sos message" in query:
                    speak(f"choose whether you want to send message or SOS")
                    from gps import main_function
                    main_function()
                    # speak(f"your message has been sent")


                elif "the time" in query or "time batao" in query or "kitne baj rahe hain" in query or "kitne baj gaye" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")   
                    speak(f"Sir, the time is {strTime}")
                # elif "temperature" in query or "mausam batao" in query or "bahar kya mausam hai" in query or "bahar kya mausam" in query:
                #     search = "temperature in chandigarh"
                #     url = f"https://www.google.com/search?q={search}"
                #     r  = requests.get(url)
                #     data = BeautifulSoup(r.text,"html.parser")
                #     temp = data.find("div", class_ = "BNeawe").text
                #     speak(f"current{search} is {temp}")
                # elif "weather" in query or "mausam batao" in query or "bahar kya mausam hai" in query or "bahar kya mausam" in query:
                #     search = "weather in chandigarh"
                #     url = f"https://www.google.com/search?q={search}"
                #     r  = requests.get(url)
                #     data = BeautifulSoup(r.text,"html.parser")
                #     temp = data.find("div", class_ = "BNeawe").text
                #     speak(f"current{search} is {temp}")
                elif "internet speed" in query or "meri internet speed kya hai" in query or "meri data speed kya hai" in query:
                    speak("calculating sir, please wait")
                    import speedtest
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi Upload speed is {upload_net}")
                    speak(f"Wifi download speed is {download_net}")


                elif "run database" in query:
                    speak(f"Upload your CSV file, sir")
                    from database import database
                    database()  


                elif "finally sleep" in query or "finally" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "you may sleep now" in query:
                    speak("Going to sleep, sir")
                    exit() 
                elif "you may sleep" in query:
                    speak("Going to sleep, sir")
                    exit() 
                elif "you can rest now" in query:
                    speak("Going to sleep,sir")
                    exit() 
                elif "you can rest" in query:
                    speak("Going to sleep,sir")
                    exit() 


                elif "shutdown the system" in query or "shutdown the" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
                    if shutdown == "yes":
                          speak("shutting down the system")
                          os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                          speak("okay, not shutting down")
                # elif "shut down the pc" in query:
                #     speak("Are You sure you want to shutdown")
                #     shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
                #     if shutdown == "yes":
                #           os.system("shutdown /s /t 1")
                #     elif shutdown == "no":
                #           break      
                # elif "shut down the laptop" in query:
                #     speak("Are You sure you want to shutdown")
                #     shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
                #     if shutdown == "yes":
                #           os.system("shutdown /s /t 1")
                #     elif shutdown == "no":
                #           break
            

import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "vs code": "code",
    "powerpoint": "powerpnt",
    "power point": "powerpnt",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc",
    "spotify": "spotify",
    "fileexplorer": "explorer",
    "microsoft edge": "msedge",
    "microsoft outlook": "outlook",
    "vlc": "vlc",
    "windows media": "wmplayer",
    "whatsapp desktop": "whatsapp",
    "snipping tool": "snippingtool",
    "task manager": "taskmgr",
    "control panel": "control",
    "power shell": "powershell"
}


def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "one" in query:
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")

    elif "two tab" in query or "two" in query or "two tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("two tabs closed")
    # elif "two tabs" in query:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("two tabs closed")

    elif "three tab" in query or "three" in query or "three tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("three tabs closed")
    # elif "three tabs" in query:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("three tabs closed")
        
    elif "four tab" in query or "four" in query or "four tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All four tabs closed")
    # elif "four tabs" in query:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("All four tabs closed")

    elif "five tab" in query or "five" in query or "five tabs" in query or "5 tab" in query or "5 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All five tabs closed")
    # elif "five tabs" in query:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("All five tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
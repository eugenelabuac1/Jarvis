import win32com.client as wincl
import sqlite3 
import speech_recognition as sr
import os
import webbrowser
import multiprocessing
import time
from db import *
sys.path.append('../')
new = 2
googleUrl="http://google.com/?#q="
youtubeUrl="http://youtube.com/results?search_query="

def talk(speech):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.speak(speech)
    
def recognize():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("say something")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source,timeout=10, phrase_time_limit=6)
        
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    
    except Exception as e:
        print(e)
        talk(e)
    
    return(text)
    
def commands():
    text = recognize()
    if text[0:20] == "jarvis search google":
        p1=multiprocessing.Process(target=talk, args=('Okay, searching google for {}'.format(text[21:]), ))
        p2=multiprocessing.Process(target=webbrowser.open, args=(googleUrl+text[21:], 'new=new'))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    if text[0:21] == "jarvis search youtube":
        p1=multiprocessing.Process(target=talk, args=('Okay, searching youtube for {}'.format(text[22:]), ))
        p2=multiprocessing.Process(target=webbrowser.open, args=(youtubeUrl+text[22:], 'new=new'))
        
        p1.start()
        p2.start()
        p1.join()
        p2.join()
#        add_history("search", "youtube")
        
    if text == "jarvis open notepad":
        p1=multiprocessing.Process(target=talk, args=('Opening notepad', ))
        p2=multiprocessing.Process(target=os.system, args=('start notepad.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    if text == "jarvis open chrome":
        p1=multiprocessing.Process(target=talk, args=('Opening chrome', ))
        p2=multiprocessing.Process(target=os.system, args=('start chrome.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    if text == "jarvis open word":
        p1=multiprocessing.Process(target=talk, args=('Opening word', ))
        p2=multiprocessing.Process(target=os.system, args=('start WINWORD.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    
    if text == "jarvis open excel":
        p1=multiprocessing.Process(target=talk, args=('Opening excel', ))
        p2=multiprocessing.Process(target=os.system, args=('start EXCEL.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    
    if text == "jarvis open powerpoint":
        p1=multiprocessing.Process(target=talk, args=('Opening powerpoint', ))
        p2=multiprocessing.Process(target=os.system, args=('start POWERPNT.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
         
    if text == "jarvis shutdown computer":
        p1=multiprocessing.Process(target=talk, args=('Shutting down computer in 20 seconds', ))
        p2=multiprocessing.Process(target=os.system, args=('shutdown /s /t 20', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
 
    if text == "jarvis restart computer":
        p1=multiprocessing.Process(target=talk, args=('Restarting computer in 20 seconds', ))
        p2=multiprocessing.Process(target=os.system, args=('shutdown /r /t 20', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    if text == "jarvis display history":
        talk("Displaying command history.")
        action = "SELECT * FROM history"
#        show_history()
                
        
    

    

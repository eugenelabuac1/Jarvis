import win32com.client as wincl
import speech_recognition as sr
import os
import webbrowser
import multiprocessing
import sys
import requests
import threading
sys.path.append('../')
from DAL.db import *
from UI.hist import *

new = 2
key = 'dcOhstTfDgJNCtoYDq9pApoS0F4cclnoSBi8hSztLyg'
ifttUrl = "https://maker.ifttt.com/trigger/trial/with/key/{}".format(key)
googleUrl="http://google.com/?#q="
youtubeUrl="http://youtube.com/results?search_query="
musicUrl="https://music.youtube.com/watch?v=l0U7SxXHkPY&list=PLFgquLnL59alcyTM2lkWJU34KtfPXQDaX"
def talk(speech):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.speak(speech)
    
def recognize(text):
    if '{}'.format(text) == "":
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("say something")
                talk("Say something")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source,timeout=10, phrase_time_limit=15)
        
            text = r.recognize_google(audio)
            p2=multiprocessing.Process(target=talk, args=("You said : {}".format(text), ))
            p2.start()
            p2.join()
        except Exception as e:
            print(e)
            talk("Please try again")
        commands(text)
    else:
        commands('{}'.format(text))
    
def commands(text):
    if text[0:20] == "jarvis search google":
        p1=multiprocessing.Process(target=talk, args=('Okay, searching google for {}'.format(text[21:]), ))
        p2=multiprocessing.Process(target=webbrowser.open, args=(googleUrl+text[21:], 'new=new'))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('search google',text[20:])
        
    elif text[0:21] == "jarvis search youtube":
        p1=multiprocessing.Process(target=talk, args=('Okay, searching youtube for {}'.format(text[22:]), ))
        p2=multiprocessing.Process(target=webbrowser.open, args=(youtubeUrl+text[22:], 'new=new'))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history("search youtube", text[21:])
        
    elif text[0:17] == "jarvis play music":
        p1=multiprocessing.Process(target=talk, args=('Okay, playing some music {}'.format(text[17:]), ))
        p2=multiprocessing.Process(target=webbrowser.open, args=(musicUrl, 'new=new'))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history("play", "music")
        
    elif text[0:12] == "jarvis tweet":
        p1=multiprocessing.Process(target=talk, args=('Okay, tweeting {}'.format(text[13:]), ))
        response = {"value1":text[13:]}
        requests.post(ifttUrl, data=response)
        p1.start()
        p1.join()
        add_history('tweet',text[14:])
        
    elif text == "jarvis open notepad":
        p1=multiprocessing.Process(target=talk, args=('Opening notepad', ))
        p2=multiprocessing.Process(target=os.system, args=('start notepad.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'notepad')
        
    elif text == "jarvis open chrome":
        p1=multiprocessing.Process(target=talk, args=('Opening chrome', ))
        p2=multiprocessing.Process(target=os.system, args=('start chrome.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'chrome')
        
    elif text == "jarvis open word":
        p1=multiprocessing.Process(target=talk, args=('Opening word', ))
        p2=multiprocessing.Process(target=os.system, args=('start WINWORD.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'word')
    
    elif text == "jarvis open excel":
        p1=multiprocessing.Process(target=talk, args=('Opening excel', ))
        p2=multiprocessing.Process(target=os.system, args=('start EXCEL.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'excel')
    
    elif text == "jarvis open powerpoint":
        p1=multiprocessing.Process(target=talk, args=('Opening powerpoint', ))
        p2=multiprocessing.Process(target=os.system, args=('start POWERPNT.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'powerpoint')
        
    elif text == "jarvis open onenote":
        p1=multiprocessing.Process(target=talk, args=('Opening onenote', ))
        p2=multiprocessing.Process(target=os.system, args=('start ONENOTE.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'onenote')
    
    elif text == "jarvis open outlook":
        p1=multiprocessing.Process(target=talk, args=('Opening outlook', ))
        p2=multiprocessing.Process(target=os.system, args=('start OUTLOOK.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'outlook')
        
    elif text == "jarvis open matlab":
        p1=multiprocessing.Process(target=talk, args=('Opening matlab', ))
        p2=multiprocessing.Process(target=os.system, args=('start matlab.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'matlab')
    
    elif text == "jarvis open file explorer":
        p1=multiprocessing.Process(target=talk, args=('Opening file explorer', ))
        p2=multiprocessing.Process(target=os.system, args=('start explorer.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'file explorer')
        
    elif text == "jarvis open command prompt":
        p1=multiprocessing.Process(target=talk, args=('Opening command prompt', ))
        p2=multiprocessing.Process(target=os.system, args=('start cmd.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open','prompt')
    
    elif text == "jarvis lock computer":
        p1=multiprocessing.Process(target=talk, args=('Locking computer', ))
        p2=multiprocessing.Process(target=os.system, args=('rundll32.exe user32.dll,LockWorkStation', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('lock','')
        
        
    elif text == "jarvis sleep":
        p1=multiprocessing.Process(target=talk, args=('Sleeping', ))
        p2=multiprocessing.Process(target=os.system, args=('RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('sleep', '')
        
    elif text == "jarvis shutdown computer":
        p1=multiprocessing.Process(target=talk, args=('Shutting down computer in 20 seconds', ))
        p2=multiprocessing.Process(target=os.system, args=('shutdown /s /t 20', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('shutdown', '')
        
    elif text == "jarvis restart computer":
        p1=multiprocessing.Process(target=talk, args=('Restarting computer in 20 seconds', ))
        p2=multiprocessing.Process(target=os.system, args=('shutdown /r /t 20', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('restart', '')
        
#
    elif text == "jarvis clear history":
        p1=multiprocessing.Process(target=talk, args=("Clearing history.", ))
        p1.start()
        action = "SELECT * FROM history"
        clear_history()
        passAction(action)
        show_history()

    elif text[0:14] == "jarvis display":
        if text[15:] == "history":
            p1=multiprocessing.Process(target=talk, args=("Displaying command history", ))
            p1.start()
            action = "SELECT * FROM history"
            passAction(action)
            show_history()
            
        else:
            speech = "Displaying command {} history.".format(text[15:])
            p1=multiprocessing.Process(target=talk, args=(speech, ))
            p1.start()
            action = "SELECT * FROM history WHERE action_type = " +"'" +text[15:]+"'"
            passAction(action)
            show_history()
    
        
def passAction(action):
    gui = ShowWindow3
    gui.action = action
    gui.Show_ThirdWindow(gui,action)
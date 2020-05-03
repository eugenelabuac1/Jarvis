import win32com.client as wincl
import speech_recognition as sr
import os
import webbrowser
import multiprocessing
import sys
import requests
sys.path.append('../')
from Database.db import *
from GUI.hist import *

new = 2
key = 'dcOhstTfDgJNCtoYDq9pApoS0F4cclnoSBi8hSztLyg'
ifttUrl = "https://maker.ifttt.com/trigger/trial/with/key/{}".format(key)
googleUrl="http://google.com/?#q="
youtubeUrl="http://youtube.com/results?search_query="

def talk(speech):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.speak(speech)
    
def recognize(text):
    if '{}'.format(text) == "":
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
        add_history('search',text[14:])
        
    if text[0:21] == "jarvis search youtube":
        p1=multiprocessing.Process(target=talk, args=('Okay, searching youtube for {}'.format(text[22:]), ))
        p2=multiprocessing.Process(target=webbrowser.open, args=(youtubeUrl+text[22:], 'new=new'))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history("search", "youtube")
        
    if text[0:12] == "jarvis tweet":
        p1=multiprocessing.Process(target=talk, args=('Okay, tweeting {}'.format(text[13:]), ))
        response = {"value1":text[13:]}
        requests.post(ifttUrl, data=response)
        p1.start()
        p1.join()
        add_history('tweet',text[14:])
        
    if text == "jarvis open notepad":
        p1=multiprocessing.Process(target=talk, args=('Opening notepad', ))
        p2=multiprocessing.Process(target=os.system, args=('start notepad.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'notepad')
        
    if text == "jarvis open chrome":
        p1=multiprocessing.Process(target=talk, args=('Opening chrome', ))
        p2=multiprocessing.Process(target=os.system, args=('start chrome.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'chrome')
        
    if text == "jarvis open word":
        p1=multiprocessing.Process(target=talk, args=('Opening word', ))
        p2=multiprocessing.Process(target=os.system, args=('start WINWORD.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'word')
    
    if text == "jarvis open excel":
        p1=multiprocessing.Process(target=talk, args=('Opening excel', ))
        p2=multiprocessing.Process(target=os.system, args=('start EXCEL.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'excel')
    
    if text == "jarvis open powerpoint":
        p1=multiprocessing.Process(target=talk, args=('Opening powerpoint', ))
        p2=multiprocessing.Process(target=os.system, args=('start POWERPNT.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'powerpoint')
        
    if text == "jarvis open onenote":
        p1=multiprocessing.Process(target=talk, args=('Opening onenote', ))
        p2=multiprocessing.Process(target=os.system, args=('start ONENOTE.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'onenote')
    
    if text == "jarvis open outlook":
        p1=multiprocessing.Process(target=talk, args=('Opening outlook', ))
        p2=multiprocessing.Process(target=os.system, args=('start OUTLOOK.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'outlook')
        
    if text == "jarvis open matlab":
        p1=multiprocessing.Process(target=talk, args=('Opening matlab', ))
        p2=multiprocessing.Process(target=os.system, args=('start matlab.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'matlab')
    
    if text == "jarvis open file explorer":
        p1=multiprocessing.Process(target=talk, args=('Opening file explorer', ))
        p2=multiprocessing.Process(target=os.system, args=('start explorer.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open', 'file explorer')
        
    if text == "jarvis open command prompt":
        p1=multiprocessing.Process(target=talk, args=('Opening command prompt', ))
        p2=multiprocessing.Process(target=os.system, args=('start cmd.exe', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('open','prompt')
    
    if text == "jarvis lock computer":
        p1=multiprocessing.Process(target=talk, args=('Locking computer', ))
        p2=multiprocessing.Process(target=os.system, args=('rundll32.exe user32.dll,LockWorkStation', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('lock','')
        
        
    if text == "jarvis sleep":
        p1=multiprocessing.Process(target=talk, args=('Sleeping', ))
        p2=multiprocessing.Process(target=os.system, args=('RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('sleep', '')
        
    if text == "jarvis shutdown computer":
        p1=multiprocessing.Process(target=talk, args=('Shutting down computer in 20 seconds', ))
        p2=multiprocessing.Process(target=os.system, args=('shutdown /s /t 20', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('shutdown', '')
        
    if text == "jarvis restart computer":
        p1=multiprocessing.Process(target=talk, args=('Restarting computer in 20 seconds', ))
        p2=multiprocessing.Process(target=os.system, args=('shutdown /r /t 20', ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        add_history('restart', '')
        
#

    if text == "jarvis display history":
        talk("Displaying command history")
        action = "SELECT * FROM history"
        passAction(action)
        show_history()
        
    if text == "jarvis clear history":
        talk("Clearing command  history.")
        action = "SELECT * FROM history"
        clear_history()
        passAction(action)
        show_history()
        
    if text == "jarvis display open":
        talk("Displaying history wherein action type is open.")
        action = "SELECT * FROM history WHERE action_type = 'open' "
        passAction(action)
        read_from_db_open()
    
    if text == "jarvis display search":
        talk("Displaying history wherein action type is search.")
        action = "SELECT * FROM history WHERE action_type = 'search' "
        passAction(action)
        read_from_db_search()
        
    if text == "jarvis display restart":
        talk("Displaying history wherein action type is restart.")
        action = "SELECT * FROM history WHERE action_type = 'restart' "
        passAction(action)
        read_from_db_restart()
    
    if text == "jarvis display shutdown":
        talk("Displaying history wherein action type is shutdown.")
        action = "SELECT * FROM history WHERE action_type = 'shutdown' "
        passAction(action)
        read_from_db_shutdown()
#     
    if text == "jarvis display sleep":
        talk("Displaying history wherein action type is sleep.")
        action = "SELECT * FROM history WHERE action_type = 'sleep' "
        passAction(action)
        read_from_db_sleep()
        
    if text == "jarvis display lock":
        talk("Displaying history wherein action type is lock.")
        action = "SELECT * FROM history WHERE action_type = 'lock' "
        passAction(action)
        read_from_db_lock()
        
    if text == "jarvis display tweet":
        talk("Displaying history wherein action type is tweet.")
        action = "SELECT * FROM history WHERE action_type = 'tweet' "
        passAction(action)
        read_from_db_tweet()
        
def passAction(action):
    gui = ShowWindow3
    gui.action = action
    gui.Show_ThirdWindow(gui,action)

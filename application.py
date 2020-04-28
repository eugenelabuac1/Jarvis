import win32com.client as wincl
import speech_recognition as sr
import os
import webbrowser
import multiprocessing
import sys
sys.path.append('../')
from Database.db import *
from GUI.hist import *


new = 2
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
        action = "SELECT * FROM history"
        talk("Displaying command history")
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
        


def passAction(action):
    gui = ShowWindow3
    gui.action = action
    gui.Show_ThirdWindow(gui,action)
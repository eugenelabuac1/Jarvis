'''
jarvis open
jarvis search ()
jarvis write (speech to text)
jarvis command (shutdown or restart)
jarvis when ()
jarvis compute 
'''
import win32com.client as wincl
import sqlite3 
import speech_recognition as sr
import os
import webbrowser
import sqlite3

new = 2
tabUrl="http://google.com/?#q="
speak = wincl.Dispatch("SAPI.SpVoice")

#conn = sqlite3.connect('test.db')
#print ("Opened database successfully");
#
#conn.execute('''CREATE TABLE COMPANY
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME           TEXT    NOT NULL,
#         AGE            INT     NOT NULL,
#         ADDRESS        CHAR(50),
#         SALARY         REAL);''')
#print ("Table created successfully");

#passive mode

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something")
        audio = r.listen(source,timeout=3, phrase_time_limit=3)
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
    
    if text[0:13] == "jarvis search":
        speak.speak("Searching {}".format(text[14:]))
        webbrowser.open(tabUrl+text[14:], new=new)
        
    if text[0:21] == "jarvis search youtube":
        speak.speak.("Searching youtube for {}".format(text[]))
        webbrowser.open(tabUrl
        
    if text == "jarvis open notepad":
        speak.speak("Opening notepad")
        os.system("start notepad.exe")
        
    if text == "jarvis open chrome":
        speak.speak("Opening chrome")
        os.system("start chrome.exe")
        
    if text == "jarvis open word":
        speak.speak("Opening word")
        os.system("start WINWORD.exe")
    
    if text == "jarvis shutdown computer":
        speak.speak("Shutting down pc in 20 seconds.")
        #os.system("shutdown /s /t 20")
        print("shutdown")
        
    if text == "jarvis restart computer":
        speak.Speak("Restarting pc in 20 seconds.")
        #os.system("shutdown /r /t 20")
        print("restart")

except:
    speak.Speak("Sorry I could not recognize what you said")
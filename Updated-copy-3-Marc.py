import win32com.client as wincl
import speech_recognition as sr
import os
import webbrowser


#passive mode

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something")
        audio = r.listen(source,timeout=3, phrase_time_limit=3)
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
    
 
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
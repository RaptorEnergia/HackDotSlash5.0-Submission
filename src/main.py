import os
# version 2.71 
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    speak("Shrey")
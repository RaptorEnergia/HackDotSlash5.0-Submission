import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    print("Hello Listening to your Voice")
    r.adjust_for_ambient_noise(source2, duration=2)
    print("Start to speak")
    
    audio2 = r.listen(source2)
    
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
    print("Did you Say = " + MyText)
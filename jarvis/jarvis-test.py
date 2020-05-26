import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)

try:
    print("You said :",r.recognize_google(audio))
except sr.UnknownValueError:
    print("error")
except sr.RequestError:
    print("error2")


import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"id: {voice.id}, name: {voice.name}")

engine.setProperty('voice', voices[1].id)
#Controll the speach
engine.setProperty('volume', 0.9)
engine.setProperty('rate', 150)
engine.say("Hello, I am your talking assistant.")
engine.runAndWait()
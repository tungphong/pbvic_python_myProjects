# Speak recongnition 
import speech_recognition

my_vir_ass_ear = speech_recognition.Recognizer()

# mic = speach_recognition.Microphone()
with speech_recognition.Microphone() as mic:
	print("My_vir_assistant: I'm listening")
	audio = my_vir_ass_ear.listen(mic)
try:
	object_speak = my_vir_ass_ear.recognize_google(audio)
except:
	object_speak = ""

print("You: " + object_speak)

#==================================

if object_speak == "":
	my_vir_ass_aws = "I can't hear you, please speak again."
elif object_speak == "hello":
	my_vir_ass_aws = "Hello MinhTam, I'm Pete cat. I'm your assistant."
elif object_speak == "today":
	my_vir_ass_aws == "Monday"
else:
	my_vir_ass_aws = "I'm ok. Thanks. How's about you?"

print(my_vir_ass_aws)

#======================
# pyttsx3 is a external lib
import pyttsx3

my_vir_speak = pyttsx3.init()
my_vir_speak.say(my_vir_ass_aws)
my_vir_speak.runAndWait()

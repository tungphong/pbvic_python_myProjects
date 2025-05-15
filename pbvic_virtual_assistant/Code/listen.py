# Speak recongnition 
import speech_recognition

my_vir_ass_ear = speech_recognition.Recognizer()

# mic = speach_recognition.Microphone()
with speech_recognition.Microphone() as mic:
	print("My_vir_assistant: I'm listening")
	audio = my_vir_ass_ear.listen(mic)
try:
	you = my_vir_ass_ear.recognize_google(audio)
except:
	you = ""
print("You: " + you)
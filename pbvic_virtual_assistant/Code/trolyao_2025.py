import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)
		print("Robot: ...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	if you == "":
		robot_brain = "I can't hear you, please try again"
	elif "hello" in you:
		robot_brain = "Hello, Tam's Daddy"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "president" in you:
		robot_brain = "Joe Biden"
	elif "bye" in you:
		robot_brain = "Bye, Tam's Daddy"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "Thanks, I'm fine."

	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()

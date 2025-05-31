import speech_recognition
#import pyttsx3
from gtts import gTTS
#from datetime import date
#from datetime import datetime
from openai import OpenAI
# Library for sound output
import pygame

client = OpenAI(
  api_key="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"
)

robot_ear = speech_recognition.Recognizer()
#robot_mouth = pyttsx3.init()
robot_brain = ""

# Create sound
pygame.mixer.init()

while True:
	# How to the robot recognite the Vietnamese language == ear
	with speech_recognition.Microphone() as mic:
		print("Robot: Tôi đang lắng nghe bạn nói ...")
		audio = robot_ear.listen(mic)
		print("Robot: ...")
	try:
		you = robot_ear.recognize_google(audio, language = "vi-VN")
	except:
		you = ""
	print("You: " + you)

	# Brain of robot_assistant
	# Using Chat GPT
	try:
		completion = client.chat.completions.create(
			model="gpt-4.1-nano",
			#store=True,
			messages=[
			#{"role": "user", "content": "write a haiku about ai"}
			{"role": "system", "content": "Bạn là một giáo viên cấp 2, vì thế bạn nên trả lời ngắn gọn và xúc tích"},
			{"role": "user", "content": you}
			],
			temperature = 0.7,
			max_tokens = 100
		)
	        #print(completion.choices[0].message);
	        #print(completion.choices[0].message.content);
		robot_brain = completion.choices[0].message.content
	except:
	        robot_brain = "Tôi đang bận, vui lòng để lại lời nhắn."
	
	# How the robot can speak the Vietnamese languae
	print("Robot: " + robot_brain)
	#robot_mouth.say(robot_brain)
	#robot_mouth.runAndWait()
	tts = gTTS(text = robot_brain, lang = "vi")
	tts.save("voice.mp3")

	# Output sound
	pygame.mixer.music.load("voice.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		continue

# pyttsx3 is a external lib
import pyttsx3

my_vir_ass_aws = "I can't hear you, please speak again."

my_vir_speak = pyttsx3.init()
my_vir_speak.say(my_vir_ass_aws)
my_vir_speak.runAndWait()
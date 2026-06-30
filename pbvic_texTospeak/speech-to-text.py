import speech_recognition as sr
from enum import Enum

class Language():
    ENGLISH = 'en-US'
    CHINA = 'zh-TW'
    FRENCH = 'fr-FR'
    SPANISH_SPAIN = 'es-ES'
    SPANISH_LATAM = 'es-US'
    KOREAN = 'ko-KR'
    JAPANESE = 'ja-JP'
    VIETNAMESE = 'vi-VN'

class SpeechToText(object):
    def print_mic_device_index(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("{1}, device_index={0}".format(name, index))

    # def speech_to_text(device_index, language=Language.ENGLISH):
    def speech_to_text(self,device_index, language):
        r = sr.Recognizer()
        with sr.Microphone(device_index=device_index) as source:
            print("Say something!")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language=language)
                # text = r.recognize_google(audio, language=language.value)
                print("you said: {}".format(text))
            except:
                print("Sorry, Please try again.")

stt_instance = SpeechToText()
lang = Language()
def check_mic_device_index():
    stt_instance.print_mic_device_index()

def run_speech_to_text_english(device_index, language):
    print(language)
    stt_instance.speech_to_text(device_index, language)

def run_speech_to_text_vietnamese(device_index, language):
    stt_instance.speech_to_text(device_index, language)



if __name__ == '__main__':
    # stt_instance = SpeechToText()
    # stt_instance.print_mic_device_index()
    # check_mic_device_index()
    # print(lang.ENGLISH)
    # run_speech_to_text_english(device_index = 1, language=lang.ENGLISH)
    run_speech_to_text_vietnamese(device_index=1, language=Language.VIETNAMESE)

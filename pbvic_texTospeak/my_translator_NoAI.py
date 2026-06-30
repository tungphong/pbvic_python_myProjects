import speech_recognition as sr
from enum import Enum

# translator
import translators as ts
# text to speach
import pyttsx3

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
        return text
stt_instance = SpeechToText()
lang = Language()
def check_mic_device_index():
    stt_instance.print_mic_device_index()

def run_speech_to_text_english(device_index, language):
    print(language)
    stt_instance.speech_to_text(device_index, language)

def run_speech_to_text_vietnamese(device_index, language):
    return stt_instance.speech_to_text(device_index, language)

# Translate from one language to another
def my_translator(text_to_translate, language_trans):
    translated = ts.translate_text(text_to_translate, translator='google', from_language='vi', to_language=language_trans)
    print(translated)
    return translated

# Text to speach
def run_text_to_speech(text_to_translate, lang_idex):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(f"id: {voice.id}, name: {voice.name}")

    # engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice', voices[lang_idex].id)
    # Controll the speach
    engine.setProperty('volume', 0.9)
    engine.setProperty('rate', 150)
    engine.say(text_to_translate)
    engine.runAndWait()

if __name__ == '__main__':
    # stt_instance = SpeechToText()
    # stt_instance.print_mic_device_index()
    # check_mic_device_index()
    # print(lang.ENGLISH)
    # run_speech_to_text_english(device_index = 1, language=lang.ENGLISH)
    trans_language = "ja"
    # trans_language = "en"
    text_trans = run_speech_to_text_vietnamese(device_index=1, language=Language.VIETNAMESE)
    trans = my_translator(text_trans, trans_language)
    run_text_to_speech(trans, 2)

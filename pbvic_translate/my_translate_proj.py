
import speech_recognition as sr
import openai
import pygame

# translator
import translators as ts

pygame.init()

client = openai.OpenAI(
        api_key="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"
    )

# Initialize the recognizer
r = sr.Recognizer()

def record_text(language):
    # Loop in case of errors
    while(1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                myText = r.recognize_google(audio2, language=language)

                print(myText)
                return myText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
    return

def text_to_speech(myText):
    with client.audio.speech.with_streaming_response.create(
            model="tts-1",  # Options include tts-1, tts-1-hd, gpt-4o-mini-tts
            voice="nova",  # Voices: alloy, ash, coral, echo, onyx, nova, sage, shimmer
            input=myText
    ) as audio_response:
        # Save the audio response to a file
        audio_response.stream_to_file("voice.mp3")
    return

def my_speaker():
    # Output sound
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    return

def my_translator(text_to_translate, language_trans):
    translated = ts.translate_text(text_to_translate, translator='google', from_language='vi', to_language=language_trans)
    print(translated)
    return translated

def output_text(text):
    f = open("output.txt", "a", encoding='utf-8')
    f.write(text)
    f.write("\n")
    f.close()
    return

my_language = "vi-VN"
trans_language = "ja"
if __name__ == '__main__':
    while True:
        text = record_text(my_language)
        en_text = my_translator(text, trans_language)
        text_to_speech(en_text)
        my_speaker()
        # output_text(text)
        # output_text(en_text)

        print("Wrote text")

import speech_recognition as sr
import pyttsx3

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

def output_text(text):
    f = open("output.txt", "a", encoding='utf-8')
    f.write(text)
    f.write("\n")
    f.close()
    return

my_language = "vi-VN"

if __name__ == '__main__':
    while True:
        text = record_text(my_language)
        output_text(text)

        print("Wrote text")
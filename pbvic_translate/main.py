import translators
import speech_recognition

robot_ear = speech_recognition.Recognizer()
robot_brain = ""

if __name__ == "__main__":
    while True:
        # How to the robot recognite the Vietnamese language == ear
        with speech_recognition.Microphone() as mic:
            print("Robot: Tôi đang lắng nghe bạn nói ...")
            audio = robot_ear.listen(mic)
            print("Robot: ...")
        try:
            Me = robot_ear.recognize_google(audio, language="vi-VN")
        except:
            Me = ""

        print(f"Me: {Me}")


        English_tr = translators.translate_text(Me, translator='google', from_language='vi', to_language='en')

        # bing = translators.translate_text(text, translator='bing', from_lang='ja', to_lang='en')

        # =================
        # Stop this program
        if Me == "ngừng chương trình" or Me == "ngưng chương trình":
            exit()

        try:
            robot_brain =  Me
        except:
            robot_brain = "Tôi đang bận, vui lòng lặp lại sau 5 giây."
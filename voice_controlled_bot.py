import pyttsx3
import speech_recognition as sr
from bardapi import Bard
import os

# pip install pyttsx3 SpeechRecognition bardapi

os.environ['_BARD_API_KEY'] = "Get your __Secure-1PSID cookie value from bard.google.com and place it here. The value ends with a dot."

r = sr.Recognizer()


def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def askBard(question):
    bard = Bard(timeout=30)  # Set timeout in seconds
    result = bard.get_answer(question)['content']
    print("Bard replied: ")
    print(result)
    SpeakText(result)


if __name__ == '__main__':
    print("Start speaking ...")

    while (1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("You said: ", MyText)
                print("Asking bard ...")
                askBard(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")

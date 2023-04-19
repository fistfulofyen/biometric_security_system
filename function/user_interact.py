def main():
    print("this is the interaction module for the application")

#convert audio input from mic to a sting 
import speech_recognition as sr


def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            convert_to_audio("please say again")
        except sr.RequestError:
            convert_to_audio("speech service down")



#convert text input to a mp3 audio which pc speaker play 
from playsound import playsound  # pip install playsound==1.2.2
from gtts import gTTS
import os

def playaudio(audio):
    playsound(audio)

def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")
    os.remove("textaudio.mp3")

if __name__ == '__main__':
    main()
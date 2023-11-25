import speech_recognition as sr
import spacy

#NOTE: convert audio input from mic to a sting 

def main():
    print("this is the interaction module for the application")
#---start---------------------------------------------------


nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 200
    mic = sr.Microphone()

    with mic as source:
        print("listensing")
        audio = recognizer.listen(source)
        try:
            spoken_text = recognizer.recognize_google(audio)
            spoken_name = extract_name(spoken_text)
            print(spoken_name)
            return spoken_name
        except sr.UnknownValueError:
            convert_to_audio("please say again")
            print("listensing")
            audio = recognizer.listen(source)
            spoken_text = recognizer.recognize_google(audio)
            spoken_name = extract_name(spoken_text)
            return spoken_name
        except sr.RequestError:
            convert_to_audio("speech service down")
#---end--------------------------------------------------------

#---start--------------------------------------------------------
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
#---end--------------------------------------------------------------

if __name__ == '__main__':
    main()

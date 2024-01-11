import speech_recognition as sr
import spacy

from gtts import gTTS
import os
import time
import threading
from playsound import playsound  # pip install playsound==1.2.2



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

    while True:
        with mic as source:
            print("Listening")
            audio = recognizer.listen(source)
            try:
                spoken_text = recognizer.recognize_google(audio)
                spoken_name = extract_name(spoken_text)
                print(spoken_name)
                return spoken_name
            except sr.UnknownValueError:
                #convert_to_audio("Please say again.")
                print("Listening")
            except sr.RequestError:
                convert_to_audio("Speech service down")
                break  # Exit the loop if there is a RequestError
#---end--------------------------------------------------------

#---start--------------------------------------------------------
#convert text input to a mp3 audio which pc speaker play 


def play_audio_async(message):
    """Function to play audio in a separate thread."""
    thread = threading.Thread(target=playsound, args=(message,))
    thread.start()

def convert_to_audio(text):
    audio_file = "textaudio.mp3"

    # Save the audio file
    audio = gTTS(text)
    audio.save(audio_file)

    # Play the audio in a separate thread
    play_audio_async(audio_file)

    # Wait for a short time before attempting to remove the file
    # This ensures that the file is not in use when attempting to remove it
    thread = threading.Thread(target=lambda: time.sleep(1))
    thread.start()
    thread.join()

    # Remove the file
    try:
        os.remove(audio_file)
    except PermissionError:
        print(f"PermissionError: Could not remove '{audio_file}'")
#---end--------------------------------------------------------------

if __name__ == '__main__':
    main()

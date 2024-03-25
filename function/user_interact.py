import speech_recognition as sr
import spacy
from gtts import gTTS
import os
import time
import threading
from playsound import playsound  # pip install playsound==1.2.2


print("user_interact module - activate")

"""
The script serves as an interaction module for an application, providing functions for speech 
recognition and converting text to speech. It utilizes the SpeechRecognition, spaCy, gTTS 
(Google Text-to-Speech), os, time, threading, and playsound libraries to enable voice-based interaction.
"""

#-----------------------------------
# extract person name from sentences 
#-----------------------------------
nlp = spacy.load("en_core_web_sm")
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

#----------------------------------------
# convert audio input from mic to a sting 
#----------------------------------------
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


#--------------------------------------------------------
# convert text input to a mp3 audio which pc speaker play 
#--------------------------------------------------------

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


if __name__ == '__main__':
    import control_hardware as control_hardware

    option = 1

    if option == 1:
        convert_to_audio("Hi, I am Darren")
    elif option == 2:
        convert_to_audio("your voice wave is recognized, the door will open")
        control_hardware.open_the_door(1)
    elif option == 3:
        convert_to_audio("sorry, I can not recognize your voice")
    else:
        print("Invalid option")

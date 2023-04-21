import function.user_interact as user_interact
import function.Face_DataBase as Face_DataBase


def main():
    #user_interact.convert_to_audio("sorry, I cannot recognize your face")
    #user_interact.convert_to_audio("are you looking for someone? if so, please speak their name")
    
    #below are for testing time saving 
    user_interact.convert_to_audio("cannot recognize")
    user_interact.convert_to_audio("speak name")
    
    #asking the stranger to provide a name from database. 
    try:
        looking_name = user_interact.recognize_speech()
    except AttributeError: #if the recognize_speech() failed to convert speech to text then there is no object to be upper case. 
        looking_name = user_interact.recognize_speech()
    #future adding: the sentence the stranger said may not be only the name; might be a sentence like"hi, I am looking for BOB WANG" 
    #               find a way to only extract the NAME part which we need to compare with the database. 
    
    print(looking_name)
    if looking_name in Face_DataBase.known_face_names: #if the stranger knows the name of the family 
        user_interact.convert_to_audio("welcome")
        #future adding: sending email to the owner, and a capture of the face in cam, if owner reply YES. then let the guest in 
        #future adding: ask the stanger to register their face in GUEST_LIST so that next time, they can login directly
        #future adding: emotion or guesture moitoring, if a known face is hijacked by a stranger 

    else:  #if the stranger DOES NOT knows the name of the family
        user_interact.convert_to_audio("sorry we cannot find the person you are looking for")


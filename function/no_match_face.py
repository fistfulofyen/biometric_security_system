import function.user_interact as user_interact
import function.Face_DataBase as Face_DataBase
import function.control_hardware as control_hardware


def FUNC_asking_guest_tell_family_member_name():
    #user_interact.convert_to_audio("sorry, I cannot recognize your face")
    #user_interact.convert_to_audio("are you looking for someone? if so, please speak their name")
    
    #below are for testing time saving 
    control_hardware.turn_on_LED('B')
    user_interact.convert_to_audio("cannot recognize")
    user_interact.convert_to_audio("speak name")
    
    #asking the stranger to provide a name from database. 
    try:
        looking_name = user_interact.recognize_speech()
    except AttributeError:  
        looking_name = user_interact.recognize_speech()

    
    print(looking_name)
    if looking_name in Face_DataBase.known_face_names: #if the stranger knows the name of the family 
        control_hardware.turn_on_LED('G')
        user_interact.convert_to_audio("welcome")
        #future adding: sending email to the owner, and a capture of the face in cam, if owner reply YES. then let the guest in 
        #future adding: ask the stanger to register their face in GUEST_LIST so that next time, they can login directly
        #future adding: emotion or guesture moitoring, if a known face is hijacked by a stranger 

    else:  #if the stranger DOES NOT knows the name of the family
        control_hardware.turn_on_LED('R')
        user_interact.convert_to_audio("sorry we cannot find the person you are looking for")



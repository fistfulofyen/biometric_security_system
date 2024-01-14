import function.user_interact as user_interact
import function.Bio_DataBase as Bio_DataBase
import function.control_hardware as control_hardware
print("no_match_face module - activate")

"""
The script is designed to interact with a guest by utilizing speech 
recognition and controlling hardware components based on the recognized information. The functionality 
includes asking the guest to speak their name, checking if the name matches a known friend in the database, 
prompting the guest to provide the name of the person they are looking for, and further verifying if that 
person is a known family member. The script handles errors and incorporates potential features like email 
notifications, face registration, and emotion or gesture monitoring for enhanced security.
"""

def FUNC_asking_guest_tell_family_member_name():
     
    control_hardware.turn_on_LED('B')
    user_interact.convert_to_audio("sorry I cannot recognize your face, please speak your name")

    #asking the stranger to provide a their name and check from friend database. 
    try:
        friend_name = user_interact.recognize_speech()
    except AttributeError:  
        friend_name = user_interact.recognize_speech()

    print(friend_name)

    if friend_name in Bio_DataBase.known_friend_names: #if the stranger knows the name of the family 
        user_interact.convert_to_audio("Hi,"+friend_name+",are you looking for someone? if so, please speak their name")
        
        #asking the stranger to provide a name from database. 
        try:
            looking_name = user_interact.recognize_speech()
        except AttributeError:  
            looking_name = user_interact.recognize_speech()

        
        print(looking_name)
        if looking_name in Bio_DataBase.known_face_names: #if the stranger knows the name of the family 
            control_hardware.turn_on_LED('G')
            user_interact.convert_to_audio("welcome,"+friend_name+",I will contact,"+looking_name+",for your right now.")

            
            #future adding: sending email to the owner, and a capture of the face in cam, if owner reply YES. then let the guest in 
            #future adding: ask the stranger to register their face in GUEST_LIST so that next time, they can login directly
            #future adding: emotion or gesture monitoring, if a known face is hijacked by a stranger 

        else:  #if the stranger DOES NOT knows the name of the family
            control_hardware.turn_on_LED('R')
            user_interact.convert_to_audio("sorry we cannot find the person you are looking for")
    else:
        user_interact.convert_to_audio("sorry I cannot recognize your name")


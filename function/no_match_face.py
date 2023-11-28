import function.user_interact as user_interact
import function.Bio_DataBase as Bio_DataBase
import function.control_hardware as control_hardware

# It asks the guest to speak their name, recognizing it using 
# speech recognition. If the name matches a known friend'name defined in DataBase, the system asks whom they seek. 
# After recognizing the sought person's name, it checks if it's in the known name of the family. If yes, it welcomes 
# the guest, turns on a green LED, and suggests future features. If not, it signals an error with a red LED and 
# apologizes for not finding the sought person. The code includes error handling and potential features like email notifications 
# and face registration.

def FUNC_asking_guest_tell_family_member_name():
     
    control_hardware.turn_on_LED('B')
    user_interact.convert_to_audio("sorry I cannot recognize your face")
    user_interact.convert_to_audio("please speak your name")

    #asking the stranger to provide a their name and check from friend database. 
    try:
        friend_name = user_interact.recognize_speech()
    except AttributeError:  
        friend_name = user_interact.recognize_speech()

    print(friend_name)

    if friend_name in Bio_DataBase.known_friend_names: #if the stranger knows the name of the family 
        user_interact.convert_to_audio("Hi")
        user_interact.convert_to_audio(friend_name)
        user_interact.convert_to_audio("are you looking for someone? if so, please speak their name")
        
        #asking the stranger to provide a name from database. 
        try:
            looking_name = user_interact.recognize_speech()
        except AttributeError:  
            looking_name = user_interact.recognize_speech()

        
        print(looking_name)
        if looking_name in Bio_DataBase.known_face_names: #if the stranger knows the name of the family 
            control_hardware.turn_on_LED('G')
            user_interact.convert_to_audio("welcome")
            user_interact.convert_to_audio(friend_name)
            user_interact.convert_to_audio("I will contact")
            user_interact.convert_to_audio(looking_name)
            user_interact.convert_to_audio("for your right now.")
            
            #future adding: sending email to the owner, and a capture of the face in cam, if owner reply YES. then let the guest in 
            #future adding: ask the stanger to register their face in GUEST_LIST so that next time, they can login directly
            #future adding: emotion or guesture moitoring, if a known face is hijacked by a stranger 

        else:  #if the stranger DOES NOT knows the name of the family
            control_hardware.turn_on_LED('R')
            user_interact.convert_to_audio("sorry we cannot find the person you are looking for")
    else:
        user_interact.convert_to_audio("sorry I cannot recognize your name")


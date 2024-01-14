import face_recognition
print("Bio_DataBase module - activate")

"""
The script utilizes the face_recognition library to load and encode facial features of 
individuals, storing the information in arrays for subsequent facial recognition tasks. 
These arrays, known_face_encodings and known_face_names, respectively, facilitate the 
recognition of known family members based on their stored facial features. 
"""

# Load a sample picture and learn how to recognize it
DYLAN_image = face_recognition.load_image_file("Supplementary/family_face/DYLAN.jpg")
DYLAN_face_encoding = face_recognition.face_encodings(DYLAN_image)[0]

JACKSON_image = face_recognition.load_image_file("Supplementary/family_face/Jackson.jpg")
JACKSON_face_encoding = face_recognition.face_encodings(JACKSON_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    DYLAN_face_encoding,
    JACKSON_face_encoding
    
]
known_face_names = [  #make sure to capitalize only the first letter and lower case for the rest of the name
    "Dylan",
    "Jackson"
    
]

known_friend_names = [  #make sure to capitalize only the first letter and lower case for the rest of the name
    "Mike",
    "Bob"
]

#-------------------------------------------------------------
# NOTE: below are code added using the graphic user interface.
#-------------------------------------------------------------


import face_recognition

# Load a sample picture and learn how to recognize it.s
#for some reason the file path has to be absolute path
DYLAN_image = face_recognition.load_image_file("C:/Users/tzhang/Desktop/personal/fianl_proj_face_recog_secure_system/family_face/DYLAN.jpg")
DYLAN_face_encoding = face_recognition.face_encodings(DYLAN_image)[0]

# Load a second sample picture and learn how to recognize it.
# HANS_image = face_recognition.load_image_file("family_face\HANS.jpg")
# HANS_face_encoding = face_recognition.face_encodings(HANS_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    DYLAN_face_encoding,
    #HANS_face_encoding
]
known_face_names = [  #make sure to capitalize only the first letter and lower case for the rest of the name
    "Dylan",
    "Jackson"
]

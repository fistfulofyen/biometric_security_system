import face_recognition

# Load a sample picture and learn how to recognize it.s
DYLAN_image = face_recognition.load_image_file("family_face\DYLAN.jpg")
DYLAN_face_encoding = face_recognition.face_encodings(DYLAN_image)[0]

# Load a second sample picture and learn how to recognize it.
HANS_image = face_recognition.load_image_file("family_face\HANS.jpg")
HANS_face_encoding = face_recognition.face_encodings(HANS_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    DYLAN_face_encoding,
    HANS_face_encoding
]
known_face_names_raw = [
    "Jackson",
    "Bob"
]
#uppercase all the names for rebust
known_face_names = []
for name in known_face_names_raw:
    known_face_names.append(name.upper())
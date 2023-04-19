import os
import face_recognition

# Initialize the lists of known face encodings and their names
known_face_encodings = []
known_face_names = []

# Define a function to add a new face to the database
def add_new_face(file_name, person_name):
    # Load the image file
    image = face_recognition.load_image_file(file_name)
    # Generate the face encoding
    face_encoding = face_recognition.face_encodings(image)[0]
    # Add the face encoding and name to the corresponding lists
    known_face_encodings.append(face_encoding)
    known_face_names.append(person_name)
    print(f"Added {person_name} to the database.")

# Add a new face to the database
add_new_face("DYLAN.jpg", "JACKSON")

# Add another face to the database
add_new_face("hans.jpg", "HANS")

# Print the total number of known faces
if __name__ == '__main__':
    
    print(f"Total known faces: {len(known_face_encodings)}")
    print(known_face_names)

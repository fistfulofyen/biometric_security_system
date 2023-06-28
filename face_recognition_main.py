import face_recognition
import cv2
import numpy as np
import time
import datetime
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import function.Face_DataBase as Face_DataBase
import function.no_match_face as no_match_face
import function.user_interact as user_interact
import function.patrol_mode as patrol_mode
import function.face_depth_measure as face_depth_measure
import function.control_hardware as control_hardware


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# This code imports several libraries and defines variables that will be used in facial recognition, patrol mode, 
# and face-depth measurements. It then creates a loop that runs continuously, taking video frames from a webcam and 
# processing them.
# In the loop, the code measures the distance between the camera and the face to determine if it is close enough 
# for facial recognition. It then enters patrol mode if the distance is between a certain range, using Haar cascades 
# to detect faces and bodies in the video frame. If a face or body is detected, it starts recording video until the 
# object moves out of the frame or after a set amount of time has passed since the detection. If no object is detected, 
# the code stops recording after a delay.


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

run_once_true = 0
run_once_false = 0
start_time = time.time()
Start_Recording = 0

recoding_frame_size = (int(video_capture.get(3)), int(video_capture.get(4)))
recoding_fourcc = cv2.VideoWriter_fourcc(*"mp4v")

current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

DISTANCE_TO_FACE_RECOGNITION = 40 #cm
DISTANCE_TO_NO_ACTION = 80 #cm
DISTANCE_TO_PATROL_MODE = range(int(DISTANCE_TO_FACE_RECOGNITION+5), int(DISTANCE_TO_NO_ACTION-5)) # 45 to 75 cm

#---NOTE: start patrol mode variable define and initialize, Loading Haar cascades for detecting faces and bodies  --------------------------------------------

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Initialize variables for detection and recording
detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5
#---end--------------------------------------


#---NOTE:start finding face distance from camera variable-----------------------------------
detector = FaceMeshDetector(maxFaces=1)
# Function to check if face is close enough for face recognition
distance_between_head_and_camera = face_depth_measure.get_distance()
#---end--------------------------------------

print("---camera on---") 
while True:

#---NOTE start checking if face is close enough for face recognition; printing out the distance between face and camera -------
#
    success,img = video_capture.read()
    img, faces = detector.findFaceMesh(img,draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        
        cv2.line(img,pointLeft,pointRight,(0,200,0),3)
        cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        cv2.circle(img,pointRight,5,(255,0,255),cv2.FILLED)

        width_of_two_eyes_in_pixels, _ = detector.findDistance(pointLeft,pointRight)
        Width_of_two_eyes_in_cm= 6.3
        focal_length_of_your_pc = 515 
        distance_between_head_and_camera = (Width_of_two_eyes_in_cm*focal_length_of_your_pc)/width_of_two_eyes_in_pixels
    
    #print(distance_between_head_and_camera)        
#---end----------------------------------------------------

    # Grab a single frame of video
    ret, frame = video_capture.read()

#---NOTE patrol mode starts here, if a person is in range of DISTANCE_TO_PATROL_MODE from the camera  ---------
  
    if DISTANCE_TO_PATROL_MODE.start <= distance_between_head_and_camera <= DISTANCE_TO_PATROL_MODE.stop-1:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
            
        if len(faces) + len(bodies) > 0:
            if detection:
                timer_started = False
            else:
                detection = True
                # Get the current time and create a VideoWriter object
                patrol_mode_name="patrol-"
                out = cv2.VideoWriter(
                    f"{patrol_mode_name}{current_time}.mp4", recoding_fourcc, 20, recoding_frame_size)
                print("Started Recording!")
        # If no face or body is detected, stop recording after a delay
        elif detection:
            if timer_started:
                if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                    detection = False
                    timer_started = False
                    out.release()
                    print('Stop Recording!')
            else:
                timer_started = True
                detection_stopped_time = time.time()

        # If recording is in progress, write the current frame to the video file
        if detection:
            out.write(frame)

#---end----------------------------------------------------
        

#---NOTE face recognition based security camera system starts here ---------------------

    # Only process every other frame of video to save time
    elif process_this_frame and distance_between_head_and_camera <= 40:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(Face_DataBase.known_face_encodings, face_encoding)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(Face_DataBase.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            # # If a match was found in known_face_encodings, just use the first one.

            # Check if any face in the frame matches a known face
            #below is the tolerance of the reco, lower num shows more strict 
            matches = [True if distance < 0.45 else False for distance in face_distances]
        

            # Check for both True and False matches
            if True in matches and False in matches:
                print("watch out")

            # Check for True match and perform actions if found
            elif True in matches:
                # Get the index of the best match
                best_match_index = matches.index(True)
                name = Face_DataBase.known_face_names[best_match_index]

                # Perform actions if it's the first time the face is detected or after 1 minute
                if run_once_true == 0 or time.time() - start_time >= 60:
                    
                    # turn on the Green LED light
                    control_hardware.turn_on_LED('G')
                    
                    # Speak a welcome message and the name of the person
                    user_interact.convert_to_audio("Welcome")
                    user_interact.convert_to_audio(name)
                    # Reset the welcome message timer
                    start_time = time.time()
                    # Set the run_once flag to avoid repeating the welcome message
                    run_once_true = 1
                    # turn off the Green LED light
                    control_hardware.turn_on_LED('OFF')
                elif time.time() - start_time >= 60:
                    # Reset the run_once_true flag after 60 seconds
                    run_once_true = 0


            # Check for False match and perform actions if found
            elif False in matches:
                # Perform actions if it's the first time no match was found or after 1 minute
                if run_once_false == 0 or time.time() - start_time >= 60:
                    # Call the no match face function
                    no_match_face.FUNC_asking_guest_tell_family_member_name()
                    # Reset the no match timer
                    start_time = time.time()

                    # Start recording video for 5 seconds
                    face_reco_mode_name = "guest-face-"
                    out = cv2.VideoWriter(f"{face_reco_mode_name}{current_time}.mp4", recoding_fourcc, 20, recoding_frame_size)
                    print("Started Recording!")
                    Start_Recording = 1
                    # Set the run_once flag to avoid repeating the no match message
                    run_once_false = 1

                elif run_once_false == 1 and (time.time() - start_time <= 5): #NOTE:longer video, bigger num here
                    # Continue recording video for 5 seconds
                    #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    out.write(frame)
                    print('Recording...')

                elif run_once_false == 1 and (time.time() - start_time > 5):
                    if Start_Recording == 1:
                        # Stop recording video after 5 seconds
                        out.release()
                        print('Stop Recording!!')
                        # Reset the run_once_false flag after 60 seconds
                        run_once_false = 1   #changed 
                        Start_Recording = 0

                elif time.time() - start_time >= 60:
                    # Reset the run_once_false flag after 60 seconds if video recording not started
                    if run_once_false == 1 :  #changed 
                        run_once_false = 0
                    else:
                        out.release()
                        print('Stop Recording!')
                        run_once_false = 0

            else:
                # Both flags are not reset if no match was found
                pass
#---end------------------------------------------------------------------------


            # Or instead, use the known face with the smallest distance to the new face
            #face_distances = face_recognition.face_distance(Face_DataBase.known_face_encodings, face_encoding)
            #best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = Face_DataBase.known_face_names[best_match_index]
            face_names.append(name)

    process_this_frame = not process_this_frame
    
# ---NOTE: adding the little red rectangle with matching name in the live camera frame-------     
    if distance_between_head_and_camera <= 40:
    # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#---end---------------------------------------
    

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()


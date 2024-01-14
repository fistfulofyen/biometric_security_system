#print(cv2.__version__)
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector #import cvzone
print("face_depth_measure module - activate")

"""
The script utilizes the OpenCV library and the 
FaceMeshDetector from the cvzone library to measure the depth of a face from a webcam. 
The calibration of the focal length is an essential step for accurate distance measurements.
"""

#--------------------------------------------------------------------------------------
# NOTE: the Global parameter you need to calibrate, follow the step in "main" at bottom
#--------------------------------------------------------------------------------------
FOCAL_LENGTH_OF_YOUR_PC = 1000  # NOTE : 1000 for laptop, 450 for desktop


video_capture = cv2.VideoCapture(0)

def calibrating_camera(calibration_mode,focal_length_of_your_pc_input):
    """This function initiates a webcam feed and draws a line between specific facial landmarks, 
    representing the width of the face. It calculates the width of the face in pixels and provides 
    a calculated focal length for the camera if in calibration mode (calibration_mode=0). The user 
    is prompted to place their head around 50 cm away from the camera during calibration."""

    #calibration_mode = 1  # NOTE: setting this to 0 to initiate the focal length of your own pc and then modify FOCAL_LENGTH_OF_YOUR_PC
    detector = FaceMeshDetector(maxFaces=1)
    while True :
        success,img = video_capture.read()
        #img, faces = detector.findFaceMesh(img,draw=False)
        img, faces = detector.findFaceMesh(img)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            
            cv2.line(img,pointLeft,pointRight,(0,200,0),3)
            cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
            cv2.circle(img,pointRight,5,(255,0,255),cv2.FILLED)

            width_of_two_eyes_in_pixels, _ = detector.findDistance(pointLeft,pointRight)

            Width_of_two_eyes_in_cm= 6.3
            
            #NOTE: different camera have different focal value finding the focal Length for your pc. so we need to find out 
            if calibration_mode ==0:
                distance_between_head_and_camera = 50 #NOTE:make your head 50cm away from the camera 
                test_out_focal_length_for_below = distance_between_head_and_camera*width_of_two_eyes_in_pixels/Width_of_two_eyes_in_cm
                print(test_out_focal_length_for_below) #NOTE: modify the value below in function
            elif calibration_mode ==1:
                # finding distance
                distance_between_head_and_camera = (Width_of_two_eyes_in_cm*focal_length_of_your_pc_input)/width_of_two_eyes_in_pixels
                print(distance_between_head_and_camera)

        if calibration_mode ==0:
            cv2.imshow("Image",img)
            if cv2.waitKey(1) == ord('q'):
                break

def get_distance(video_capture, detector,focal_length_of_your_pc_input):
    """This function reads frames from the webcam, detects facial landmarks, 
    and calculates the distance between the head and the camera based on 
    the calibrated focal length. The calculated distance is returned."""
    
    success, img = video_capture.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    distance_between_head_and_camera = 0  # Initialize the variable

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)

        width_of_two_eyes_in_pixels, _ = detector.findDistance(pointLeft, pointRight)
        Width_of_two_eyes_in_cm = 6.3
        distance_between_head_and_camera = (Width_of_two_eyes_in_cm * focal_length_of_your_pc_input) / width_of_two_eyes_in_pixels


    return distance_between_head_and_camera


if __name__ == '__main__':
    
    # NOTE: for every new camera or laptop with webcam that you use, you need to calibrate the "FOCAL_LENGTH_OF_YOUR_PC" parameter,
    # since every camera has different internal parameter of their only. in order to do that:
    
    # 1. place your head around 50 cm away from your webcam.
    # 2. set the calibration_mode to 0 to start the measurement process. 
    # 3. change the "FOCAL_LENGTH_OF_YOUR_PC" parameter to the reading printed out. 
    # 4. set the calibration_mode to 1 to check if the distance measuring makes sense


    calibrating_camera(calibration_mode =0, focal_length_of_your_pc_input = FOCAL_LENGTH_OF_YOUR_PC)

import cv2
print(cv2.__version__)
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

#--------------------------------------------------------------------------------------
# NOTE: the Global parameter you need to calibrate, follow the step in "main" at bottom
#--------------------------------------------------------------------------------------

FOCAL_LENGTH_OF_YOUR_PC = 600


#-------------------------------------------------------
# this is the source code for the face_depth measurement
#-------------------------------------------------------
video_capture = cv2.VideoCapture(0)

def calibrating_camera(calibration_mode,focal_length_of_your_pc_input):

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

def get_distance(video_capture, detector,FOCAL_LENGTH_OF_YOUR_PC=FOCAL_LENGTH_OF_YOUR_PC):
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
        distance_between_head_and_camera = (Width_of_two_eyes_in_cm * FOCAL_LENGTH_OF_YOUR_PC) / width_of_two_eyes_in_pixels


    return distance_between_head_and_camera


if __name__ == '__main__':
    
    # NOTE: for every new camera or laptop with webcam that you use, you need to calibrate the "FOCAL_LENGTH_OF_YOUR_PC" parameter,
    # since every camera has different internal parameter of their only. in order to do that:
    
    # 1. place your head around 50 cm away from your webcam.
    # 2. set the calibration_mode to 0 to start the measurement process. 
    # 3. change the "FOCAL_LENGTH_OF_YOUR_PC" parameter to the reading printed out. 
    # 4. set the calibration_mode to 1 to check if the distance measuring makes sense


    calibrating_camera(calibration_mode =0, focal_length_of_your_pc_input = FOCAL_LENGTH_OF_YOUR_PC)

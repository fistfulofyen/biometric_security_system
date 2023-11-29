import cv2
print(cv2.__version__)
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

video_capture = cv2.VideoCapture(0)


def get_distance(calibration_mode =1):

    #NOTE:for every new camera or laptop with webcam that you use, you need to calibrate the "focal_length_of_your_pc" parameter,
    #since every camera has different internal parameter of their only. in order to do that:
    # first: set the camera around 50 cm away from your face.
    # second: set the calibration_mode to 0 to start the measurement process. 
    # finally: change the "focal_length_of_your_pc" parameter to the reading printed out. 

    #calibration_mode = 1  # NOTE: setting this to 0 to initiate the focal length of your own pc and then modify focal_length_of_your_pc
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
                # finding depth 
                focal_length_of_your_pc = 1000 
                distance_between_head_and_camera = (Width_of_two_eyes_in_cm*focal_length_of_your_pc)/width_of_two_eyes_in_pixels
                print(distance_between_head_and_camera)


        cv2.imshow("Image",img)
        if cv2.waitKey(1) == ord('q'):
            break



if __name__ == '__main__':
    get_distance(calibration_mode =0)

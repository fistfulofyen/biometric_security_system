import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

video_capture = cv2.VideoCapture(0)


def developer_main():

    detector = FaceMeshDetector(maxFaces=1)
    mode = 1  # NOTE: setting this to 0 to initiate the focal length of your own pc 
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

            #NOTE: different camera have different focal value finding the focal Length for your pc. 
            Width_of_two_eyes_in_cm= 6.3
            
            if mode ==0:
                distance_between_head_and_camera = 50 #make your head 50cm away from the camera 
                test_out_focal_length_for_below = distance_between_head_and_camera*width_of_two_eyes_in_pixels/Width_of_two_eyes_in_cm
                print(test_out_focal_length_for_below)
            elif mode ==1:
                # finding depth 
                focal_length_of_your_pc = 515 
                distance_between_head_and_camera = (Width_of_two_eyes_in_cm*focal_length_of_your_pc)/width_of_two_eyes_in_pixels
                print(distance_between_head_and_camera)


        cv2.imshow("Image",img)
        if cv2.waitKey(1) == ord('q'):
            break



def get_distance(): #NOTE : this is used in the main script, but for better readility, look at above main()
    detector = FaceMeshDetector(maxFaces=1)
    while True :
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
            return distance_between_head_and_camera 

if __name__ == '__main__':
    developer_main()

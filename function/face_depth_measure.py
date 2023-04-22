import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

video_capture = cv2.VideoCapture(0)


def main():

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

            w, _ = detector.findDistance(pointLeft,pointRight)

            #finding the focal Length
            W= 6.3

            # finding depth 
            f = 515 
            d = (W*f)/w
            #print(d)
            return d 

        #cv2.imshow("Image",img)
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

            w, _ = detector.findDistance(pointLeft,pointRight)
            W= 6.3
            f = 515 
            d = (W*f)/w
            return d 

if __name__ == '__main__':
    get_distance()

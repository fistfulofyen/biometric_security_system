import cv2
import time
import datetime

#NOTE: this is the source code for patrol mode, 

def main():
    # Create a VideoCapture object for the default camera (0)
    cap = cv2.VideoCapture(0)

    # Load Haar cascades for detecting faces and bodies
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_fullbody.xml")

    # Initialize variables for detection and recording
    detection = False
    detection_stopped_time = None
    timer_started = False
    SECONDS_TO_RECORD_AFTER_DETECTION = 5

    # Get the size of the video frames and initialize the video codec
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:
        # Read a frame from the camera
        _, frame = cap.read()

        # Convert the frame to grayscale and detect faces and bodies
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

        # If a face or body is detected, start recording
        if len(faces) + len(bodies) > 0:
            if detection:
                timer_started = False
            else:
                detection = True
                # Get the current time and create a VideoWriter object
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(
                    f"{current_time}.mp4", fourcc, 20, frame_size)
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

        # Display the current frame on the screen
        cv2.imshow("Camera", frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) == ord('w'):
            break

    # Release the VideoWriter and VideoCapture objects, and close all windows
    out.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
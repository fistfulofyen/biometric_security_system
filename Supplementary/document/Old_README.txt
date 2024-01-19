-----------------
for window set up
-----------------

get the code to your local pc
download git bash at: https://git-scm.com/downloads
open git bash terminal choose the folder you want to store the code
get the code from repo: $ git clone https://github.com/zhant22/biometric_security_system.git
then go to VS code and install below module to run the script
python 3.10 is recommended since some libraries are not ready for newer Python version 

--------------------------------------------------
set up the face recognition env for your pc first: 
--------------------------------------------------

adding your python to your PC's path if you are using window, usually some where like this: 
-C:\Users\Administrator\AppData\Local\Programs\Python\Python39
-C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Scripts

go to the website: https://github.com/ageitgey/face_recognition for more info or just follow below steps: 

------------------------------
All package and library needed
------------------------------

pip install CMake
pip install dlib:
installing dlib in Window is tricky, we have to download the file from third part, following this video for help:https://www.youtube.com/watch?v=AUJKdehF2ZA&t=280s

pip3 install face_recognition
pip3 install opencv-python       #opeating the webcam
pip3 install SpeechRecognition   #convert your talk to text 
pip3 install gtts                #convert text to mp3 audio file 
pip3 install playsound==1.2.2    #play out the mp3 from pc speaker 
pip3 install pyaudio             #same as above 
pip3 install cvzone              #detect the distance between face and camera 
pip3 install mediapipe           #detect the distance between face and camera 
pip3 install spacy               #used to extract person name from user speech input
pip3 install pyserial            #using python to control arduino board 
python -m spacy download en_core_web_sm   #used to extract person name from user speech input

------------------------------
How to use git for the project 
------------------------------

go to the folder you store the code of this project
if you added a new file: $ git add .  (make sure the dot in the end, it means all)
if only edit existed file: $ git commit -am "your message here" 
push the code to repo: $ git push 
getting updates from git : $git pull 

if there are any problem, watch this youtube video: https://www.youtube.com/watch?v=Lk6jCVAS3Iw


------for window set up:

---get the code to your local pc
-open git bash terminal choose the folder you want to store the code
-get the code from repo: $ git clone https://github.com/zhant22/fianl_proj_face_recog_secure_system.git
-then go to VS code and install below module to run the script

---set up the face recognition env for your pc first: 

-go to the website: https://github.com/ageitgey/face_recognition for more info or just follow below steps: 

pip install CMake

-install dlib:
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
python -m spacy download en_core_web_sm   #used to extract person name from user speech input


---how to use git for the project: 
-goes to the folder you store the code of this project
-if you added a new file: $ git add .  (make sure the dot in the end, it means all)
-if only edit existed file: $ git commit -am "your message here" 
-push the code to repo: $ git push 
-getting updates from git : $git pull 

if there are any problem, watch this youtube video: https://www.youtube.com/watch?v=Lk6jCVAS3Iw


below are not for face_recognition
---set up visual machine------------------
https://www.youtube.com/watch?v=hYaCCpvjsEY

sudo apt install git 

sudo apt install build-essential

sudo apt install pkg-config

git clone https://github.com/radareorg/radare2

radare2/sys/install.sh

r2pm init

r2pm -i r2dec
r2pm -ci r2ghidra

r2pm -l 


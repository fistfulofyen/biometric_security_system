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
pip install opencv-python       #opeating the webcam
pip install SpeechRecognition   #convert your talk to text 
pip install gtts                #convert text to mp3 audio file 
pip install playsound==1.2.2    #play out the mp3 from pc speaker 
pip install pyaudio

---how to use git for the project: 
-goes to the folder you store the code of this project
-if you added a new file: $ git add .  (make sure the dot in the end, it means all)
-if only edit existed file: $ git commit -am "your message here" 
-push the code to repo: $ git push 
-getting updates from git : $git pull 

if there are any problem, watch this youtube video: https://www.youtube.com/watch?v=Lk6jCVAS3Iw

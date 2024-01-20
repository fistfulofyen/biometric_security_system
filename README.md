<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/zhant22/biometric_security_system">
    <img id="logo" src="Supplementary/readme_pic/LOGO.png" alt="Logo" width="240" height="80">
  </a>

<h3 align="center">Biometric Security System</h3>

  <p align="center">
    A security system  featured with AI assistance and biometric verification method
    <br />
    <a href="https://github.com/zhant22/biometric_security_system"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/zhant22/biometric_security_system">View Demo</a>
    ·
    <a href="https://github.com/zhant22/biometric_security_system/issues">Report Bug</a>
    ·
    <a href="https://github.com/zhant22/biometric_security_system/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/zhant22/biometric_security_system)

This project aims to develop an advanced facial recognition system to address the growing security needs and technological challenges. The system will combine state-of-the-art facial recognition technology and advanced algorithms to provide outstanding performance and functionality, meeting the requirements of multiple application areas.

<!--Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following:  `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [<img src="Supplementary\readme_pic\Dlib.png" width="50" height="20" alt="Dlib">][dlib-url]
* [<img src="Supplementary\readme_pic\CMake.png" width="70" height="20" alt="CMake">][CMake-url]
* [<img src="Supplementary\readme_pic\OpenCV.png" width="70" height="20" alt="OpenCV">][OpenCV-url]
* [<img src="Supplementary\readme_pic\MediaPipe.png" width="70" height="20" alt="MediaPipe">][MediaPipe-url]
* [<img src="Supplementary\readme_pic\spaCy.png" width="70" height="20" alt="spaCy">][spaCy-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Installing all packages and modules in order to run this project. Some of these module installation is tricky; following the instruction. 

### Prerequisites
**Installing Dlib**
Installing Dlib in Window is tricky so we have two options here: 

**Option one: Installing Dlib Manually**
we have to download the file from third part, following this video for help:
* help video: [https://www.youtube.com/watch?v=AUJKdehF2ZA&t=280s](https://www.youtube.com/watch?v=AUJKdehF2ZA&t=280s)

**Option two: Installing face_recognition with prebuild dlib library**
* Installing this forked face_recognition
  ```sh
  pip3 install face_recognition @ git+https://github.com/thetoby9944/face_recognition
  ```

**Packages installation**

Installing there following packages:
* All modules required
  ```sh
  pip3 install CMake
  pip3 install face_recognition
  pip3 install opencv-python                #operating the webcam
  pip3 install SpeechRecognition            #convert your talk to text 
  pip3 install gtts                         #convert text to mp3 audio file 
  pip3 install playsound==1.2.2             #play out the mp3 from pc speaker 
  pip3 install pyaudio                      #same as above 
  pip3 install cvzone                       #detect the distance between face and camera 
  pip3 install mediapipe                    #detect the distance between face and camera 
  pip3 install spacy                        #used to extract person name from user speech input
  pip3 install pyserial                     #using python to control arduino board 
  python -m spacy download en_core_web_sm   #used to extract person name from user speech input
  ```

### Installation

1. python **3.10** is recommended since some libraries are not ready for newer version

2. Clone the repo
   ```sh
   git clone https://github.com/zhant22/biometric_security_system.git
   ```
3. Install **All** packages required
   ```sh
   npm install
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project aims to develop an advanced facial recognition system to address the growing security needs and technological challenges. The system will combine state-of-the-art facial recognition technology and advanced algorithms to provide outstanding performance and functionality, meeting the requirements of multiple application areas.

_For more examples, please refer to the [Documentation](https://github.com/zhant22/biometric_security_system)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Facial recognition
- [x] Distance detection Surveillance Camera
- [x] AI voice assistant
- [x] Graphic User Interface
- [x] Hardware LED lights for statues indication
- [x] Step motor as door opener 
- [x] Finger print reader
    - [x] All Feature completed

See the [open issues](https://github.com/zhant22/biometric_security_system/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/zhant22/biometric_security_system](https://github.com/zhant22/biometric_security_system)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Face Recognition Library (GitHub Repository)](https://github.com/ageitgey/face_recognition)
* [CMake](https://cmake.org/)
* [Dlib](http://dlib.net/python/index.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/zhant22/biometric_security_system.svg?style=for-the-badge
[contributors-url]: https://github.com/zhant22/biometric_security_system/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zhant22/biometric_security_system.svg?style=for-the-badge
[forks-url]: https://github.com/zhant22/biometric_security_system/network/members
[stars-shield]: https://img.shields.io/github/stars/zhant22/biometric_security_system.svg?style=for-the-badge
[stars-url]: https://github.com/zhant22/biometric_security_system/stargazers
[issues-shield]: https://img.shields.io/github/issues/zhant22/biometric_security_system.svg?style=for-the-badge
[issues-url]: https://github.com/zhant22/biometric_security_system/issues
[license-shield]: https://img.shields.io/github/license/zhant22/biometric_security_system.svg?style=for-the-badge
[license-url]: https://github.com/zhant22/biometric_security_system/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username

[product-screenshot]: Supplementary/readme_pic/GUI.png

[Dlib-url]: http://dlib.net/
[CMake-url]: https://cmake.org/
[OpenCV-url]: https://opencv.org/
[MediaPipe-url]: https://developers.google.com/mediapipe
[spaCy-url]: https://spacy.io/


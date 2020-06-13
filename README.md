# LoLHighlighter
2020 Spring Capstone Project 

## Team member 
* Hyeseong Lee 
* Youngheon Kim 
* Yoonjin Han
## Features and Purpose
* **LoLHighlighter** is a web service that extracts **highlights from LCK 2020 seasons' YouTube videos**.
* By **input the url** of a LCK 2020 seasons' YouTube video, you can see the **highlight timestamp of the video**.
![image](https://user-images.githubusercontent.com/47580804/84558587-0845f900-ad6f-11ea-8d66-14873d99ccad.png)
* Click a timestamp and watch **the highlights of the time and category** that you want.
![image](https://user-images.githubusercontent.com/47580804/84558561-cae16b80-ad6e-11ea-9fd7-8f9b55124c18.png)
## Project environment
* Python 3.6(or 3.7)
* ffmpeg (https://ffmpeg.org/)
* pytesseract (https://github.com/madmaze/pytesseract)
* opencv (https://docs.opencv.org/master/)
## Installation
* At first, you need to download required libraries through pip command.
```
pip install -r requirements.txt
```
* After you downdload the whole requirements, download FFmpeg and add **ffmpeg/bin** path to the system environment variable.
  * FFmpeg download link : https://ffmpeg.zeranoe.com/builds/

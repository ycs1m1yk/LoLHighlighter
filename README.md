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
* **Windows 10**
* **Python 3.6**(or 3.7)
* **ffmpeg** (https://ffmpeg.org/)
* **pytesseract** (https://github.com/madmaze/pytesseract)
* **opencv** (https://docs.opencv.org/master/)
## Installation
###  ffmpeg installation
  - **Download link** -> https://ffmpeg.zeranoe.com/builds/
![image](https://user-images.githubusercontent.com/47580804/83952462-f4ccf680-a873-11ea-86a1-5ab9b7f187f8.png)

  - Store the downloaded file as `C:\Program Files\ffmpeg`
![image](https://user-images.githubusercontent.com/47580804/83952515-51c8ac80-a874-11ea-88f9-0a301fcd221c.png)


  - Edit the system environment -> add `C:\Program Files\ffmpeg\bin` to the PATH
![image](https://user-images.githubusercontent.com/47580804/83952505-3fe70980-a874-11ea-99b4-5865457302da.png)

### tesseract-OCR installation

  - **For only windows** -> https://github.com/UB-Mannheim/tesseract/wiki
![image](https://user-images.githubusercontent.com/47580804/83952578-b4ba4380-a874-11ea-9b32-dac8c277a0a4.png)

  - **For all OS** -> https://tesseract-ocr.github.io/tessdoc/Home.html
![image](https://user-images.githubusercontent.com/47580804/83952570-a0764680-a874-11ea-858f-274fbc072fc7.png)
- Download into `C:\Program Files\Tesseract-OCR`

  - Edit the system environment -> add `C:\Program Files\Tesseract-OCR` to the PATH
![image](https://user-images.githubusercontent.com/47580804/83952601-d4ea0280-a874-11ea-938d-89554613e1a9.png)

### .bat excution (TODO)
  - `pip install --upgrade pip`
  - `pip install -r requirements.txt`
  - etc..
## How to use 
  - Clone or download **LoLHighlighter**.
  - From the path where you downloaded **LoLHighlighter**, `LoLHighlighter\flask>flask run` at the terminal.
  - You can use **LoLHighlighter** with local server -> http://127.0.0.1:5000/
![image](https://user-images.githubusercontent.com/47580804/83952611-e29f8800-a874-11ea-9e51-c6f7f4857af4.png)


import cv2
import numpy as np
import warnings
import sys


def video_test(directory, offsets):
    print("Start Frame Capture")
    vidcap = cv2.VideoCapture(directory+'.mp4')

    if not vidcap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print("fps: ", fps)
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, fps * offsets[3][0])
    ret, image = vidcap.read()
    cv2.imwrite(directory+'frame%d.jpg' % offsets[3][0], image)
    print("Frame Capture Done")
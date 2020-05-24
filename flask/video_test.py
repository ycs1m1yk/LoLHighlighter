import cv2
import numpy as np
import warnings
import sys
import pytesseract as ptsrt


time_ocr_x_1 = 940
time_ocr_x_2 = 990
time_ocr_y_1 = 75
time_ocr_y_2 = 95


def get_game_start_time(directory):
    print("START : get game start time")
    vid_cap = cv2.VideoCapture(directory+'.mp4')

    if not vid_cap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    length = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_now = int(length/2)
    while frame_now > 0:
        vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frame_now)
        ret, image = vid_cap.read()

        sub_image = image[time_ocr_y_1: time_ocr_y_2, time_ocr_x_1: time_ocr_x_2]
        gray_sub_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
        ocr_image = cv2.resize(gray_sub_image, (250, 100))
        time_now = ptsrt.image_to_string(ocr_image)
        time_split = time_now.split(":")
        digit_count = 0
        for i in time_split:
            if i.isdigit():
                digit_count += 1
        if digit_count == 2:
            print("ingame time :", time_split[0], ":", time_split[1])
            game_start_time = int(frame_now / fps) - (60 * int(time_split[0]) + int(time_split[1]))
            print("game start time :", game_start_time)
            # cv2.imwrite(directory + '_frame_%d.jpg' % game_start_time, image)
            # cv2.imwrite(directory + '_sub_frame_%d.jpg' % game_start_time, ocr_image)
            return game_start_time
        else:
            frame_now -= fps * 60
    print("cannot get game start time")
    return -1


def get_game_end_time(directory):
    print("START : get game end time")
    vid_cap = cv2.VideoCapture(directory + '.mp4')

    if not vid_cap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    length = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_now = int(length/2)
    end_time = int(frame_now/fps)
    while frame_now <= int(length):
        vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frame_now)
        ret, image = vid_cap.read()

        sub_image = image[time_ocr_y_1: time_ocr_y_2, time_ocr_x_1: time_ocr_x_2]
        gray_sub_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
        ocr_image = cv2.resize(gray_sub_image, (250, 100))
        time_now = ptsrt.image_to_string(ocr_image)
        time_split = time_now.split(":")
        digit_count = 0

        for i in time_split:
            if i.isdigit():
                digit_count += 1
        if digit_count == 2:
            end_time = int(frame_now / fps) + 30
        """else:
            cv2.imwrite(directory + '_ocr_fail_%s.jpg' % time_now[:5], ocr_image)"""
        frame_now += fps * 30
    print("game end time :", end_time)
    return end_time

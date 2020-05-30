import cv2
import numpy as np
import pytesseract as ptsrt
import re

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

# time_ocr_x_1 = 630
# time_ocr_x_2 = 661
# time_ocr_y_1 = 51
# time_ocr_y_2 = 63

time_ocr_x_1 = 940
time_ocr_x_2 = 990
time_ocr_y_1 = 75
time_ocr_y_2 = 95

kill_ocr_x_1 = 602
kill_ocr_x_2 = 683
kill_ocr_y_1 = 11
kill_ocr_y_2 = 37

# test_image = cv2.imread("test.png")


def isValid(string):
    valid = '^([\d]+)$'  # one or more digits only
    regex = re.compile(valid)
    if regex.match(string):
        return True
    return False


def remove_whitespaces(string):
    string.replace(" ", "")
    return string


def time_ocr(image):

    # crop sub images
    time_image = image[time_ocr_y_1: time_ocr_y_2, time_ocr_x_1: time_ocr_x_2]

    # grayscale
    gray_time_image = cv2.cvtColor(time_image, cv2.COLOR_BGR2GRAY)

    # image resize
    time_ocr = cv2.resize(gray_time_image, (250, 100))

    # ocr
    time_now = ptsrt.image_to_string(
        time_ocr, lang='eng', config=tessdata_dir_config)

    # print("time_now:", time_now)

    # cv2.imshow('time', time_ocr)
    # cv2.imshow('kill_l', kill_ocr_left)
    # cv2.imshow('kill_r', kill_ocr_right)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return time_now


def kill_ocr(image):
    # crop sub images
    kill_image = image[kill_ocr_y_1: kill_ocr_y_2, kill_ocr_x_1: kill_ocr_x_2]

    # grayscale
    gray_kill_image = cv2.cvtColor(kill_image, cv2.COLOR_BGR2GRAY)

    # image resize
    kill_ocr = cv2.resize(gray_kill_image, (250, 100))

    kill_threshold = cv2.threshold(
        kill_ocr, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # crop kill sub images
    kill_ocr_left = kill_ocr[0:100, 0: 105]
    kill_ocr_right = kill_ocr[0:100, 175: 245]

    # ocr
    kill_left = ptsrt.image_to_string(
        kill_ocr_left, lang='eng', config=tessdata_dir_config+' --psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
    kill_right = ptsrt.image_to_string(
        kill_ocr_right, lang='eng', config=tessdata_dir_config+' --psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
    remove_whitespaces(kill_left)
    remove_whitespaces(kill_right)

    # if kill is not detected
    if isValid(kill_left) == False:
        # print("Detecting kill_left is failed, retry with --psm 10")
        kill_left = ptsrt.image_to_string(
            kill_ocr_left, lang='eng', config=tessdata_dir_config+' --psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    if isValid(kill_right) == False:
        # print("Detecting kill_right is failed, retry with --psm 10")
        kill_right = ptsrt.image_to_string(
            kill_ocr_right, lang='eng', config=tessdata_dir_config+' --psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    remove_whitespaces(kill_left)
    remove_whitespaces(kill_right)

    # print("kill left:", kill_left)
    # print("kill right:", kill_right)

    # cv2.imshow('kill_l', kill_ocr_left)
    # cv2.imshow('kill_r', kill_ocr_right)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return kill_left, kill_right


# if __name__ == '__main__':
#     do_ocr(test_image)

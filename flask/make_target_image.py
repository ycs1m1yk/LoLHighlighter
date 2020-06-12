import cv2

# y1:y2, x1:x2
target_y1 = 66
target_y2 = 94
target_x = [[752, 780,'left_4'],
            [787, 815, 'left_3'],
            [822, 850, 'left_2'],
            [858, 886, 'left_1'],
            [1042, 1070, 'right_1'],
            [1079, 1107, 'right_2'],
            [1115, 1143, 'right_3'],
            [1152, 1180, 'right_4']]


def make_target_image(directory, end_time):
    vid_cap = cv2.VideoCapture(directory + '.mp4')

    if not vid_cap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    vid_cap.set(cv2.CAP_PROP_POS_FRAMES, int(end_time * fps))
    ret, image = vid_cap.read()
    for x in target_x:
        target_image = image[target_y1:target_y2, x[0]:x[1]]
        cv2.imwrite('./images/target/' + x[2] + '.jpg', target_image)


# make_target_image('./video/video_extraction_httpsyoutube_PRspTODahY', 2870)
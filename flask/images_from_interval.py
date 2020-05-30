import cv2


def images_from_interval(start, end, directory):
    vid_cap = cv2.VideoCapture(directory+'.mp4')

    if not vid_cap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start * fps)
    end_frame = int(end * fps)
    step_size = int((end - start + 1) / 10 * fps)

    images = []
    for frame in range(start_frame, end_frame, step_size):
        vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, image = vid_cap.read()
        # test file write for check output
        # cv2.imwrite(directory + '_frame_%d.jpg' % frame, image)
        images.append(image)

    return images

# test code
# images_from_interval(1800, 2000, './video/video_extraction')

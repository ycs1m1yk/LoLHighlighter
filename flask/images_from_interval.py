import cv2

NUM_IMAGE = 5


def images_from_interval(start, end, directory):
    vid_cap = cv2.VideoCapture(directory+'.mp4')

    if not vid_cap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start * fps)
    end_frame = int(end * fps)
    step_size = int((end - start + 1) / NUM_IMAGE * fps)

    img_directories = []
    for frame in range(start_frame, end_frame, step_size):
        vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, image = vid_cap.read()
        # test file write for check output
        store_directory = directory + '_frame_%d.png' % frame
        cv2.imwrite(store_directory, image)
        img_directories.append(store_directory)

    return img_directories


def image_objects_from_interval(start, end, directory):
    vid_cap = cv2.VideoCapture(directory + '.mp4')

    if not vid_cap.isOpened():
        print("could not open :", directory, '.mp4')
        return -1
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start * fps)
    end_frame = int(end * fps)
    step_size = int((end - start + 1) / NUM_IMAGE * fps)

    images = []
    for frame in range(start_frame, end_frame, step_size):
        vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, image = vid_cap.read()
        # test file write for check output
        images.append(image)

    return images

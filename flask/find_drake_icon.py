from search_image import is_searched
from images_from_interval import images_from_interval 
import sys
import os 

DRAKE = ['./images/cloud.png','./images/ocean.png','./images/infernal.png','./images/mountain.png']


def is_drake_increased(start: int, end: int, video_directory: str) -> bool: 
    if start > end: 
        print('start cannot be bigger than end')
        sys.exit()

    found = []
    img_directory = images_from_interval(start, end, video_directory)
    for img in img_directory: 
        count = 0
        for drake in DRAKE: 
            if is_searched(img, drake):
                count += 1 
        if count != 0:
            found.append(count)

    print(found)
    clear_directory(img_directory)
    if len(found) >= 2:
        if found[0] < found[-1]:
            print(f'section {start}-{end}, Detected dragon count is increased')
            return True
    else:
        return False


def clear_directory(file_list):
    for f in file_list: 
        os.remove(f)

# Test code
# 1800 ~ 2000 사이에 용을 잡았는가? 
# result : True/ False 
# print(is_drake_increased(600, 1000, './video/video_extraction'))
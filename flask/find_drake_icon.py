from search_image import is_searched
from images_from_interval import images_from_interval 

def is_find_drake(start, end, video_directory): 
    drakes = ['./images/cloud.png','./images/ocean.png','./images/infernal.png','./images/mountain.png']
    img_directory = images_from_interval(start, end, video_directory)
    print(img_directory[0])

    for drake in drakes: 
        print(drake)
        for img in img_directory:
            print(img_directory.index(img))
            is_searched(img, drake)

is_find_drake(1800, 2000, './video/video_extraction')
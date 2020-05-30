from PIL import Image
from PIL import ImageChops
from PIL import ImageStat
from PIL import ImageDraw
import numpy as np
import cv2
import sys
import time

# src 는 파일 위치 형식
TOLERANCE = 30
STEP = 1
TRIAL = 0

X1 = 650
X2 = 1300
Y1 = 40
Y2 = 140


def is_searched(src, tar):
    source = Image.open(src).convert('RGB')
    #source.show()
    target = Image.open(tar).convert('RGB')
    
    if source.format != target.format: 
        source.format = target.format
    
    source = source.crop((X1, Y1, X2, Y2))
    sx, sy = source.size
    tx, ty = target.size
    
    print(src, "Source size: ", source.size, source.format)
    print(tar, "Target size: ", target.size, target.format)

    draw = ImageDraw.Draw(source)
    start = time.time()

    for y in range(sy - ty):
        for x in range(0, sx - tx, STEP):
            compare = source.crop((x, y, x + 10, y + 10))
            partial_target = target.crop((0, 0, 10, 10))
            diff = ImageChops.difference(compare, partial_target)
            stat = ImageStat.Stat(diff)
            # TOLERAN 에 따라 유사도 변형
            if max(max(stat.extrema[0]), max(stat.extrema[1]), max(stat.extrema[2])) < TOLERANCE:
                if Search(x, y, source, target) == True:
                    draw.rectangle((x, y, x+target.width, y +
                                    target.height), outline=(255, 0, 0))
                    end = time.time()
                    print('Target Found!, searching time: ', end - start)
                    # source.show()
                    return True
            

    end = time.time()
    print('Image search failed. searching time: ', end - start)
    return False


def pyramid(tar):
    img = cv2.imread(tar, cv2.IMREAD_UNCHANGED)
    tmp = img.copy()

    win_titles = ['origin', 'level1', 'level2', 'level3']
    g_down = []
    g_down.append(tmp)

    for i in range(len(win_titles) - 1):
        tmp1 = cv2.pyrDown(tmp)
        g_down.append(tmp1)
        tmp = tmp1

    return g_down


def Search(cx, cy, src, tar):
    tx, ty = tar.size
    # 타겟 이미지 크기 만큼 잘라낸다
    compare = src.crop((cx, cy, cx + tx, cy + ty))
    print('Compare size: ', compare.size)

    diff = ImageChops.difference(compare, tar)
    stat = ImageStat.Stat(diff)
    global TRIAL
    if max(max(stat.extrema[0]), max(stat.extrema[1]), max(stat.extrema[2])) <= TOLERANCE:
        print("Target found(Min, max)", stat.extrema)
        return True
    else:
        TRIAL += 1
        return False


#is_searched('./video/video_extraction_frame_59364.png', './images/cloud.png')
#is_searched('./images/source.png', './images/target.png')

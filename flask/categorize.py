from find_drake_icon import *
from ocr_test import *
from images_from_interval import *
import copy


# categorize priority
# 1. banpick: the first interval
# 2. dragon
# 3. check kill
#   3-1. teamfight
#   3-2. kill
# 4. other -> replay, pro view 같은 Game UI안나오는 부분도 포함됨.
def categorize(offsets_input, directory, game_start_time, game_end_time):
    offsets = copy.deepcopy(offsets_input)
    for interval in offsets:
        # banpick
        if interval[0] <= game_start_time:
            interval.append('Banpick')
        # after_game
        elif interval[0] > game_end_time:
            interval.append('After Game')
        # detect_dragon_increase -> dragon
        # elif is_drake_increased(start, end, directory):
            # interval.append('dragon')
        # else -> kill change detection
        else:
            images = image_objects_from_interval(interval[0], interval[1], directory)

            left_valid = False
            right_valid = False
            kill_left = 0
            kill_right = 0
            kill_left_change = 0
            kill_right_change = 0

            for num in range(len(images)):
                valid_check = 0
                left, right = kill_ocr(images[num])
                # digit validation
                # all valid
                if left.isdigit() and right.isdigit():
                    if left_valid:
                        valid_check += 1
                    else:
                        kill_left = int(left)
                        left_valid = True
                    if right_valid:
                        valid_check += 1
                    else:
                        kill_right = int(right)
                        right_valid = True
                    if valid_check == 2:
                        if int(left) - kill_left > 0:
                            kill_left_change += int(left) - kill_left
                            kill_left = int(left)
                        if int(right) - kill_right > 0:
                            kill_right_change += int(right) - kill_right
                            kill_right = int(right)
                # only left kill valid
                elif left.isdigit():
                    if left_valid:
                        if int(left) - kill_left > 0:
                            kill_left_change += int(left) - kill_left
                            kill_left = int(left)
                    else:
                        kill_left = int(left)
                        left_valid = True
                # only right valid
                elif right.isdigit():
                    if right_valid:
                        if int(right) - kill_right > 0:
                            kill_right_change += int(right) - kill_right
                            kill_right = int(right)
                    else:
                        kill_right = int(right)
                        right_valid = True
            # check kill change -> teamfight / kill / other_ingame
            change = kill_left_change + kill_right_change
            
            if change >= 2:
                interval.append('Kill & Teamfight')
            elif change > 0:
                interval.append('Kill & Teamfight')
            else:
                interval.append('Other Ingame - SuperPlay, Replay, Pro view, etc..')

    return offsets

import librosa
import numpy as np
import warnings
import sys


def audio_test(directory, game_start_time, game_end_time):
    warnings.filterwarnings("ignore")
    try:
        print("Now Extracting H/L Time-Line")
        reSampleRate = 5500
        offset = game_start_time
        duration = 360
        total_time = 0
        hits = []

        while True:
            # add offset parameter for librosa.load() to specify starting time.
            # duration parameter is the total time that librosa analyze.
            try:
                y, sr = librosa.load(
                    directory, sr=reSampleRate, offset=offset, duration=duration)
                # print('sr: ', reSampleRate)
            except Exception as e:
                print(e)
                break
            time = np.linspace(0, len(y)/sr, len(y))

            # Exclude general output values ​​to check only special values.
            adjust = np.where((y > np.min(y)+0.1) & (y < np.max(y)-0.1), 0, y)

            for i in range(adjust.size):
                if adjust[i] != 0:
                    hit_round = round(time[i] + offset)
                    hits.append(int(hit_round))

            offset += duration

            total_time += int(librosa.get_duration(y=y))
            del y

        hits_remove_dup = list(set(hits))
        hits_remove_dup.sort()

        # print('[hits_remove_dup] --', hits_remove_dup)

        hl_start = hits_remove_dup[0]
        hl_temp = hits_remove_dup[0]
        hl_end = hits_remove_dup[1]

        hl_list = []
        iteration = 1
        continue_val = 20
        while iteration < len(hits_remove_dup):
            count = 0
            while hl_end - hl_temp < continue_val:

                if iteration == len(hits_remove_dup):
                    break
                hl_end = hits_remove_dup[iteration]
                hl_temp = hits_remove_dup[iteration-1]
                iteration += 1
                count += 1

            hit_count_val = 1
            if hl_end != hits_remove_dup[len(hits_remove_dup)-1]:
                if count > hit_count_val:
                    element = [hl_start, hl_temp]
                    hl_list.append(element)
                if iteration < len(hits_remove_dup)-1:
                    hl_start = hits_remove_dup[iteration]
                    hl_temp = hits_remove_dup[iteration]
                    hl_end = hits_remove_dup[iteration+1]

            iteration += 1

        # print(len(hl_list))
        interval_resize_val = 5
        for i in range(len(hl_list)):
            hl_list[i][0] += -interval_resize_val
            hl_list[i][1] += interval_resize_val
            if hl_list[i-1][1] < game_end_time < hl_list[i][0]:
                hl_list.insert(i, [game_end_time-30, game_end_time])
        if hl_list[-1][1] < game_end_time:
            hl_list.append([game_end_time-40 , game_end_time])
        hl_list.insert(0, [game_start_time-40, game_start_time+20])

        print('[highlight result]: ', hl_list)
        print("Audio analysis finished")

        return hl_list
    except Exception as e:
        _, _, tb = sys.exc_info()  # tb -> traceback object
        print('file name = ', __file__)
        print('error line No = {}'.format(tb.tb_lineno))
        print(e)



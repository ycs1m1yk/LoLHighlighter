import librosa
import numpy as np
import warnings
import sys


def audio_test(directory):
    warnings.filterwarnings("ignore")
    try:
        print("Now Extracting H/L Time-Line")
        reSampleRate = 5500
        offset = 0
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

        while iteration < len(hits_remove_dup):
            count = 0
            while hl_end - hl_temp < 10:

                if iteration == len(hits_remove_dup):
                    break
                hl_end = hits_remove_dup[iteration]
                hl_temp = hits_remove_dup[iteration-1]
                iteration += 1
                count += 1

            if hl_end != hits_remove_dup[len(hits_remove_dup)-1]:
                if count > 1:
                    element = [hl_start, hl_temp]
                    hl_list.append(element)
                if iteration < len(hits_remove_dup)-1:
                    hl_start = hits_remove_dup[iteration]
                    hl_temp = hits_remove_dup[iteration]
                    hl_end = hits_remove_dup[iteration+1]

            iteration += 1

        # print(len(hl_list))
        for i in range(len(hl_list)):
            if hl_list[i][0] < 30:
                hl_list[i][0] == 0
            else:
                hl_list[i][0] += -30
            hl_list[i][1] += 30
        print('[highlight result]: ', hl_list)
        print("Extraction finished")

        return hl_list
    except Exception as e:
        _, _, tb = sys.exc_info()  # tb -> traceback object
        print('file name = ', __file__)
        print('error line No = {}'.format(tb.tb_lineno))
        print(e)



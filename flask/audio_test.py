import librosa
import numpy as np


def audio_test(directory):
    try:
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
                print('sr: ', reSampleRate)
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

        print(len(hits_remove_dup))
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

                hl_start = hits_remove_dup[iteration]
                hl_temp = hits_remove_dup[iteration]
                hl_end = hits_remove_dup[iteration+1]

            iteration += 1

        print('[highlight result]: ', hl_list)

    except Exception as e:
        print(e)

    return hl_list

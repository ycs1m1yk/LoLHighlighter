import librosa
import numpy as np
import matplotlib.pyplot as plt


def audio_test(directory):
    try:
        offset = 0
        figure_num = 1
        duration = 360
        hits = []

        while True:
            # add offset parameter for librosa.load() to specify starting time.
            # duration parameter is the total time that librosa analyze.
            try:
                y, sr = librosa.load(directory, offset=offset, duration=duration)
            except Exception as e:
                print(e)
                break
            time = np.linspace(0, len(y)/sr, len(y))

            # Exclude general output values ​​to check only special values.
            adjust = np.where((y > -0.5) & (y < 0.5), 0, y)
            for i in range(adjust.size):
                if adjust[i] != 0:
                    hit_round = round(time[i] + offset)
                    hits.append(int(hit_round))

            '''
            # Graph output
            plt.title(directory + ", num: " + str(figure_num))
            plt.xlabel("Time(sec)")
            plt.ylabel("Amplitude")
            plt.plot(time, adjust, c='b', label='waveform')
            plt.savefig(directory + ", num " + str(figure_num) + '.png')
            plt.show()
            '''
            offset += duration
            figure_num += 1
            del y

        hits_remove_dup = list(set(hits))
        hits_remove_dup.sort()
        print(hits_remove_dup)

    except Exception as e:
        print(e)


import librosa
import numpy as np
import matplotlib.pyplot as plt


def audio_test(directory):
    try:
        # add offset parameter for librosa.load() to specify starting time.
        # duration parameter is the total time that librosa analyze.
        y, sr = librosa.load(directory, duration=240)
        time = np.linspace(0, len(y)/sr, len(y))

        # Exclude general output values ​​to check only special values.
        adjust = np.where((y > -0.5) & (y < 0.5), 0, y)

        # Graph output
        plt.title(directory)
        plt.xlabel("Time(sec)")
        plt.ylabel("Amplitude")
        plt.plot(time, adjust, c='b', label='waveform')
        plt.savefig(directory+'.png')
        plt.show()

    except Exception as e:
        print(e)


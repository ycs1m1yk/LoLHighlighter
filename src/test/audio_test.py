import librosa
import numpy as np
import matplotlib.pyplot as plt


def audio_test(directory):
    try:
        y, sr = librosa.load(directory, sr=44100)
        print(y)
        time = np.linspace(0, len(y)/sr, len(y))

        plt.figure(1)
        plt.title(directory)
        plt.xlabel("Time(sec)")
        plt.ylabel("Amplitude")
        plt.plot(time, y, c='b', label='waveform')
        plt.savefig(directory+'.png')
        plt.show()

    except Exception as e:
        print(e)


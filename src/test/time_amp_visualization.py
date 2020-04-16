from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import time

# TODO
# ➡ Set Graph file output dir


filename = input('filename : ')
audio_path = "./audio/{0}".format(filename)

# 개별 설정 필요
offset = int(input('offset : '))
duration = int(input('duration : '))

start_time = time.time()

y, sr = librosa.load(audio_path, offset=offset, duration=duration)
xTime = np.linspace(0, len(y)/sr, len(y))

plt.figure()
xLabel = "time(sr={0})".format(sr)
yLabel = "amplitude"
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.plot(xTime, y, c='b', label='waveform')
plt.tight_layout()
plt.savefig(filename+'.png')
plt.plot()

elapsed_time = time.time() - start_time
print("duration: ", duration)
print("elapsed time: ", "%.2f" % elapsed_time, "seconds")

plt.show()

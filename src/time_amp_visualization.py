from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import time

start_time = time.time()

audio_path = "./audio/applause.wav"

# 개별 설정 필요 
offsetValue = 0.0
duration_len = 30

y, sr = librosa.load(audio_path, offset=offsetValue, duration=duration_len)

plt.figure()
plt.plot(y)
xLabel = "time(sr={0})".format(sr)
yLabel = "amplitude"
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.tight_layout()
plt.plot()

elapsed_time = time.time() - start_time
print("duration: ", duration_len)
print("elapsed time: ", "%.2f" % elapsed_time, "seconds")

plt.show()

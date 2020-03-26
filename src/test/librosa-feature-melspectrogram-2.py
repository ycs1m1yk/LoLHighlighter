from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display
import time

start_time = time.time()

audio_path = "./audio/GRF vs kt - Round 1 Game 1  LCK Spring Split  Griffin vs kt Rolster (2020).mp4"
duration_len = 60

y, sr = librosa.load(audio_path, duration=60)
librosa.feature.melspectrogram(y=y, sr=sr)
# array([[  2.891e-07,   2.548e-03, ...,   8.116e-09,   5.633e-09],
# [  1.986e-07,   1.162e-02, ...,   9.332e-08,   6.716e-09],
# ...,
# [  3.668e-09,   2.029e-08, ...,   3.208e-09,   2.864e-09],
# [  2.561e-10,   2.096e-09, ...,   7.543e-10,   6.101e-10]])

# Using a pre-computed power spectrogram would give the same result:

D = np.abs(librosa.stft(y))**2
S = librosa.feature.melspectrogram(S=D, sr=sr)

# Display of mel-frequency spectrogram coefficients, with custom
# arguments for mel filterbank construction (default is fmax=sr/2):

# Passing through arguments to the Mel filters
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                   fmax=8000)
plt.figure(figsize=(10, 4))
S_dB = librosa.power_to_db(S, ref=np.max)
librosa.display.specshow(S_dB, x_axis='time',
                         y_axis='mel', sr=sr,
                         fmax=8000)
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram')
plt.tight_layout()

elapsed_time = time.time() - start_time
print("duration: ", duration_len)
print("elapsed time: ", "%.2f" % elapsed_time, "seconds")

plt.show()

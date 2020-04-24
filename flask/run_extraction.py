import time

from extract import audio_extraction
from audio_test import audio_test


def run_extraction(url):
    print(" ------------------------------------------")
    print("|  Running extraction...")
    print(" ------------------------------------------")

    YouTubeURL = url

    try:
        audio_filename = audio_extraction(YouTubeURL)
        directory = './audio/'+audio_filename+'.mp4'

        start = time.time()
        offsets = audio_test(directory)

    except Exception as e:
        print(e)

    elapsed_time = time.time() - start
    print("elapsed time: ", "%.2f" % elapsed_time, "seconds")
    return offsets

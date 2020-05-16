import time

from extract import *
from audio_test import audio_test
from video_test import get_game_start_time

def run_extraction(url):
    print(" ------------------------------------------")
    print("|  Running extraction...")
    print(" ------------------------------------------")

    YouTubeURL = url

    try:
        audio_filename = audio_extraction(YouTubeURL)
        video_filename = video_extraction(YouTubeURL)
        audio_dir = './audio/'+audio_filename+'.mp4'
        video_dir = './video/'+video_filename

        start = time.time()
        offsets = audio_test(audio_dir)
        get_game_start_time(video_dir)

    except Exception as e:
        print(e)

    elapsed_time = time.time() - start
    print("elapsed time: ", "%.2f" % elapsed_time, "seconds")
    return offsets

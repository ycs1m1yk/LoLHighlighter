import time

from extract import *
from audio_test import audio_test
from video_test import *

def run_extraction(url):
    YouTubeURL = url
    print(" ------------------------------------------")
    print(" Running extraction :", YouTubeURL)
    print(" ------------------------------------------")

    offsets = None
    try:
        start = time.time()
        audio_filename = audio_extraction(YouTubeURL)
        video_filename = video_extraction(YouTubeURL)
        # audio_filename = 'audioExtraction'
        # video_filename = 'video_extraction'
        audio_dir = './audio/'+audio_filename+'.mp4'
        video_dir = './video/'+video_filename


        game_start_time = get_game_start_time(video_dir)
        game_end_time = get_game_end_time(video_dir)
        offsets = audio_test(audio_dir, game_start_time, game_end_time)

    except Exception as e:
        print(e)

    elapsed_time = time.time() - start
    print("elapsed time: ", "%.2f" % elapsed_time, "seconds")

    print(f'offsets: {offsets}')
    return offsets

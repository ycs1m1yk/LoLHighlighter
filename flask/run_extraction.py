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

        offsets = audio_test(directory)

    except Exception as e:
        print(e)

    return offsets

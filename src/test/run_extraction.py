from YouTubeExtraction import Extract
from YouTubeExtraction import AudioTest


YouTubeURL = input('Your YouTube URL : ')

try:
    audio_filename = Extract.audio_extraction(YouTubeURL)
    directory = audio_filename+'.mp4'

    AudioTest.audio_test(directory)

except Exception as e:
    print(e)

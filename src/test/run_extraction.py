import extract
import audio_test


YouTubeURL = input('Your YouTube URL : ')

try:
    audio_filename = extract.audio_extraction(YouTubeURL)
    directory = audio_filename+'.mp4'

    audio_test.audio_test(directory)

except Exception as e:
    print(e)

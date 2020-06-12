from pytube import YouTube
import copy
import string


def audio_extraction(url):

    print("START : audio extraction")
    print("Checking URL Validation...")

    try:
        yt = YouTube(url)
        audio_extract_stream = yt.streams.filter(only_audio=True).first()

    except Exception as e:
        print("URL Validation Error!", e)
        return e

    print("Now Downloading...")

    filename_url = copy.deepcopy(url)
    filename_url = filename_url.replace(":", "").replace("/", "").replace(".", "").strip()
    filename = "audio_extraction_" + filename_url
    parent_dir = r"./audio"

    try:
        audio_extract_stream.download(parent_dir, filename, None, True)

    except Exception as e:
        print("Download Fail!", e)
        return e

    print("Download Finished Successfully")

    return filename


def video_extraction(url):

    print("START : video extraction")
    print("Checking URL Validation...")

    try:
        yt = YouTube(url)
        video_extract_stream = yt.streams.filter(only_video=True).first()

    except Exception as e:
        print("URL Validation Error!", e)
        return e

    print("Now Downloading...")

    filename_url = copy.deepcopy(url)
    filename_url = filename_url.replace(":", "").replace("/", "").replace(".", "").strip()
    filename = "video_extraction_" + filename_url
    parent_dir = r"./video"

    try:
        video_extract_stream.download(parent_dir, filename, None, True)

    except Exception as e:
        print("Download Fail!", e)
        return e

    print("Download Finished Successfully")

    return filename


def print_default_filename(url):
    try:
        yt = YouTube(url)
        audio_extract_stream = yt.streams.filter(only_audio=True).first()
        video_extract_stream = yt.streams.filter(only_video=True).first()

        print("audio default filename : ",
              audio_extract_stream.default_filename)
        print("video default filename : ",
              video_extract_stream.default_filename)

    except Exception as e:
        print("URL Validation Error!", e)
        return e


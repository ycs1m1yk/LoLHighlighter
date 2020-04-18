from pytube import YouTube


def audio_extraction(url):
    filename = "audioExtraction"

    parent_dir = r"./audio"

    print("Checking URL Validation...")

    try:
        yt = YouTube(url)
        audio_extract_stream = yt.streams.filter(only_audio=True).first()

    except Exception as e:
        print("URL Validation Error!", e)
        return e

    print("Now Downloading...")

    try:
        audio_extract_stream.download(parent_dir, filename, None, True)

    except Exception as e:
        print("Download Fail!", e)
        return e

    print("Download Finished Successfully")

    return filename


def video_extraction(url):
    filename = "video_extraction"
    print("Checking URL Validation...")

    try:
        yt = YouTube(url)
        video_extract_stream = yt.streams.filter(only_video=True).first()

    except Exception as e:
        print("URL Validation Error!", e)
        return e

    print("Now Downloading...")

    try:
        video_extract_stream.download(None, filename, None, True)

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


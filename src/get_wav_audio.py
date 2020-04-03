from pytube import YouTube
import glob
import os.path

# link url 입력
link = input('YouTube Link> ')
yt = YouTube(link)
dl_path = r'.\audio'

print(yt.streams.filter(only_audio = True).all())
try:
    yt.streams.filter(only_audio=True).first().download(dl_path)
except Exception as e: 
    print(e)

# 테스트를 위한 new name
new_name = input("New audio name?> ")

files = glob.glob("audio/*.mp4")
for x in files: 
    if not os.path.isdir(x):
        filename = os.path.splitext(x)
        print(filename[0])
        try: 
            os.rename(x,'audio/'+new_name+'.wav')
        except: 
            pass






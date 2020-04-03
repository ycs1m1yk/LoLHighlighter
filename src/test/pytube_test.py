import os
import subprocess

import pytube

yt = pytube.YouTube("https://youtu.be/DGvPe-EYhoo")  # 다운받을 동영상 URL 지정

vids = yt.streams.all()

# 영상 형식 리스트 확인
for i in range(len(vids)):
    print(i, '. ', vids[i])

vnum = int(input("다운 받을 화질은? "))

parent_dir = r"C:\Users\satol\Documents\workspace\Python\LOLHighlighter\src\test\audio"  # 다운로드받을 디렉토리
vids[vnum].download(parent_dir)  # 다운로드 수행

new_filename = input("변환 할 mp3 파일명은?")

default_filename = vids[vnum].default_filename
subprocess.call(['ffmpeg', '-i',  # cmd 명령어 수행
                 os.path.join(parent_dir, default_filename),
                 os.path.join(parent_dir, new_filename)
                 ])

print('동영상 다운로드 및 mp3 변환 완료!')

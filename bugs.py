import glob
import ffmpeg
import os
from os.path import isdir, expanduser
def concatVideos():
    files = findWeba()
    print(files)
    streams = []
    for file in files:
        streams.append(ffmpeg.input(file))
    ffmpeg.concat(*streams,v=0,a=1).output('pizza.mp4').run()

concatVideos()

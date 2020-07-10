import glob
import ffmpeg
import os
from os.path import isdir, expanduser
def findWeba():
    home = expanduser("~")
    path = home +'/Documents/programming stuff/audioStuff/works'
    # all weba filenames
    weba_files = [f for f in os.listdir(path) if f.endswith('.weba')]
    #print(text_files)
    return weba_files

def concatVideos():
    files = findWeba()
    print(files)
    streams = []
    for file in files:
        streams.append(ffmpeg.input(file))
    ffmpeg.concat(*streams,v=0,a=1).output('pizza.mp4').run()

concatVideos()

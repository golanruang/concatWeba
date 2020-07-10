import glob
import os

stringa = ""
for f in glob.glob("*.weba"):
    stringa += f + "|"
os.system("ffmpeg -i \"concat:" + stringa + "\" -codec copy output.wav")

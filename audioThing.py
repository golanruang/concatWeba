"""
This script uses ffmpeg to merge all weba files in the
folder which the script is run. You need to have ffmpeg
installed on your computer.
To install, run this:
brew install ffmpeg-python

"""
import glob
import ffmpeg
import os
from os.path import isdir, expanduser

def concatVideos(files,path):
    """
    Purpose: concatenate the weba files into a mp4 file (downloads the file on computer)
    Parameters: a list of files to concatenate
    Return val: None
    """
    name = findID(files[0]) + '.mp4'
    pathName = path+name
    streams = []
    for file in files:
        streams.append(ffmpeg.input(file))
    ffmpeg.concat(*streams,v=0,a=1).output(pathName).run()

def findWeba(path):
    """
    Purpose: finds all weba files in a given directory
    Parameters: the path of the directory with the weba files in it (str)
    Return: a list with all the weba files names in it (list of strings)
    """
    weba_files = [f for f in os.listdir(path) if f.endswith('.weba')]
    return weba_files

def findID(file):
    """
    Purpose: find the id of file (str)
    Parameters: the file name (str)
    Return: the id number of the file (str)
    """
    numDashes=0
    numNeededDashes=4
    ID = ''
    for char in range(len(file)):
        if file[char] == '-':
            numDashes+=1
            if numDashes == numNeededDashes:
                for i in range(1,8):
                    ID = ID + file[char+i]
    return ID

def main():
    home = expanduser("~")
    path = input('Enter path: ')            # input for path that audio files/this file are in
    path = home + path
    files = findWeba(path)                  # finds all the weba files in the file
    sortedFiles = sorted(files)
    idFiles = []
    index = 0
    BOOL = True
    while sortedFiles!=[]:                  # while not interated through all weba files
        if idFiles == []:
            idFiles.append(sortedFiles[0])  # grouping the files by id number
            sortedFiles.pop(0)
        if len(sortedFiles) == 1:
            idFiles.append(sortedFiles[0])
            sortedFiles.pop(0)
            concatVideos(idFiles,path)
            idFiles=[]
            break
        if findID(idFiles[0])==findID(sortedFiles[0]):
            idFiles.append(sortedFiles[0])
            sortedFiles.pop(0)
        if findID(idFiles[0])!=findID(sortedFiles[0]):
            print(idFiles)
            concatVideos(idFiles,path)
            idFiles=[]

main()

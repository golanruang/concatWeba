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
    streams = []
    for file in files:                                 # for every file in files with the same ID
        streams.append(ffmpeg.input(file))
    ffmpeg.concat(*streams,v=0,a=1).output(name).run() # concatenate the files

def findWeba(path,acceptedNames):
    """
    Purpose: finds all weba files in a given directory
    Parameters: the path of the directory with the weba files in it (str)
    Return: a list with all the weba files names in it (list of strings)
    """
    weba_files=[]
    for f in os.listdir(path):                          # for every file in the path given
        for name in acceptedNames:
            if name in f and f.endswith('.weba'):       # if name is valid and it has the .weba file name
                weba_files.append(f)                    # add it to the list of weba files
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
    for char in range(len(file)):                        # for every character in file
        if file[char] == '-':
            numDashes+=1
            if numDashes == numNeededDashes:             # when 4 dashes are counted
                for i in range(1,8):                     # get the ID by adding the next 7 characters after the 4th dash
                    ID = ID + file[char+i]
    return ID

def main():
    acceptedNames=['aji1','viku','gtp7','l2wv','8l71','yqit','k4os','zefu']
    home = expanduser("~")
    path = input('Enter path: ')                         # input for path that audio files/this file are in
    path = home + '/' + path
    files = findWeba(path,acceptedNames)                 # finds all the weba files in the file
    sortedFiles = sorted(files)
    print(sortedFiles)
    idFiles = []
    while sortedFiles!=[]:                               # while not iterated through all weba files
        if idFiles == []:                                # grouping the files by id number
            idFiles.append(sortedFiles[0])
            sortedFiles.pop(0)
        if len(sortedFiles) == 1:                        # if its the last file in the whole directory
            idFiles.append(sortedFiles[0])               # add it to the list w/ same ids
            sortedFiles.pop(0)
            concatVideos(idFiles,path)
            break
        if findID(idFiles[0])==findID(sortedFiles[0]):   # if the id of the first file of the dir is the same as the ids in the ids list
            idFiles.append(sortedFiles[0])               # add the file in the directory to the list with same ids
            sortedFiles.pop(0)                           # remove that file from the directory
        if findID(idFiles[0])!=findID(sortedFiles[0]):   # if the id of the first file in the dir isn't the same as the ids in the ids list
            concatVideos(idFiles,path)                   # concatenate the files in the list with same ids
            idFiles=[]                                   # make the list with same ids blank (for a new id)

main()

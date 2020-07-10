"""
This script uses ffmpeg to merge all weba files in the
folder which the script is run. You need to have ffmpeg
installed on your computer.
"""
import glob
import ffmpeg
import os
from os.path import isdir, expanduser

def concatVideos(files):
    name = findID(files[0]) + '.mp4'
    print('name: '+name)
    streams = []
    for file in files:
        streams.append(ffmpeg.input(file))
    print(streams)
    ffmpeg.concat(*streams,v=0,a=1).output('pizza.mp4').run()

# def findWeba(path, pattern):
#     files = []                      # all weba filenames
#     print('all files: ', os.listdir(path).sort())
#     for file in os.listdir(path):
#         if pattern in file:
#             files.append(file)
#     return files

def findWeba(path):
    #home = expanduser("~")
    #path = home +'/Documents/programming stuff/audioStuff/uploads'
    # all weba filenames
    weba_files = [f for f in os.listdir(path) if f.endswith('.weba')]
    #print(text_files)
    return weba_files

def findID(file):
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

def stripFilename(file):
    newName = ''
    for char in file:
        if char == '.':
            return newName
        newName = newName + char

def main():
    home = expanduser("~")
    path = home +'/Documents/programming stuff/audioStuff/works'
    files = findWeba(path)
    sortedFiles = sorted(files)
    # for file in sortedFiles:
    #     print(file)
    idFiles = []
    index = 0
    BOOL = True
    while sortedFiles!=[]:
        if idFiles == []:
            idFiles.append(sortedFiles[0])
            sortedFiles.pop(0)
        print('idFiles ID: ' + str(findID(idFiles[0])) + 'sortedFilesID: ' + str(findID(sortedFiles[0])))
        if findID(idFiles[0])==findID(sortedFiles[0]):
            idFiles.append(sortedFiles[0])
            sortedFiles.pop(0)
        if findID(idFiles[0])!=findID(sortedFiles[0]):
            print(idFiles)
            concatVideos(idFiles)
            idFiles=[]
        #
        #
        #
        #
        #
        #
        #
        # id=findID(files[0])
        #
        #
        #
        #
        #
        #
        #
        # print(len(files))
        # print(range(len(files)))
        # for i in range(len(files)):
        #     #print('OG ID: ' + str(id) + ' ID: ' + str(findID(files[i])) + ' BOOL: ' + str(findID(files[i]) == id))
        #     print(i)
        #     if findID(files[i]) == id:
        #         idFiles.append(files[i])
        #         files.pop(i)
        # print(idFiles)
        # concatVideos(idFiles, path)
        #
        # # print(index)
        # # id = findID(files[index])
        # # print("file #" + str(index) + "is: " + str(files[index]))
        # # if len(idFiles)==0:
        # #     idFiles.append(files[index])
        # # elif id == findID(idFiles[0]):
        # #     idFiles.append(files[index])
        # # #if id != findID(idFiles[0]):
        # # else:
        # #     print("idFiles: ",idFiles)
        # #     concatVideos(idFiles, path)
        # #     idFiles = []
        # #     idFiles.append(id)
        # # index+=1

main()

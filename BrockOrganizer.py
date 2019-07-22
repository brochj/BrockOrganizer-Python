# -*- coding: utf-8 -*-
"""
@author: Oscar Broch Jr. - https://github.com/brochj
Created on Sun May 27 13:25:42 2018
Last Update: July 21, 2019
based on: https://www.geeksforgeeks.org/junk-file-organizer-python/
"""

import os

PATH = './'
# File extensions that will be organized
EXTENSIONS = {
    "EXECUTABLES": ['.exe', '.msi', '.jar', '.apk'],
    "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp',
               '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd'],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
               ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": ['.txt', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods',
                  '.odt', '.xps', '.dotx', '.docm', '.dox', '.xls', '.xlsx', '.ppt', '.pptx'],
    "PDFS": ['.pdf'],
    "COMPRESSED": ['.rar', '.zip', '.7z', '.bzip2',
                   '.gzip', '.tar', '.wim', '.xz', ],
    "SCRIPTS": ['.ahk', '.js', '.json'],
}


def printHeader():
    print('Organizer Files - Python [v0.0.2 - July 22, 2019]\n')
    print('author: Oscar Broch Jr. - https://github.com/brochj\n')
    return


def getFilesList(path):
    return os.listdir(path)


def printAllUserFiles(allFilesArray):
    print('List of files and folders found:\n')
    for i in range(0, len(allFilesArray)):
        print(f'{allFilesArray[i]}')
    return


def createDestinyFolder(fileFolder):
    if not os.path.exists(fileFolder):
        os.makedirs(fileFolder)


def moveFileToDestinyFolder(fileName, destinyFolderName):
    try:
        os.rename(os.path.join('./', fileName),
                  os.path.join(destinyFolderName, fileName))
    except:
        pass


def organizer(fileName, destinyFolderName):
    createDestinyFolder(destinyFolderName)
    moveFileToDestinyFolder(fileName, destinyFolderName)
    print(f'moved << {fileName} >>')
    return


def extractFileExtension(fileName):
    return str(fileName[fileName.rfind('.'):])


def main():
    printHeader()
    allUserFiles = getFilesList(PATH)
    printAllUserFiles(allUserFiles)
    for fileName in allUserFiles:
        userFileExtension = extractFileExtension(fileName)

        for fileType, extensionsList in EXTENSIONS.items():
            for extension in extensionsList:
                if userFileExtension == extension:
                    organizer(fileName, fileType.capitalize())

    print('\nYour files are now organized! =) \n')
    return


if __name__ == "__main__":
    main()

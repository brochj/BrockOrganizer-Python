# -*- coding: utf-8 -*-
"""
@author: broch
Created on Sun May 27 13:25:42 2018
Last Update: July 21, 2019
based on: https://www.geeksforgeeks.org/junk-file-organizer-python/
"""

import os

PATH = './'
# Extensões do arquivos a serem organizados
EXECUTABLES = ['.exe', '.msi', '.jar', '.apk']
IMAGES = ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp',
          '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd']
VIDEOS = [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
          ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"]
DOCUMENTS = ['.txt', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods',
             '.odt', '.xps', '.dotx', '.docm', '.dox', '.xls', '.xlsx', '.ppt', '.pptx']
PDFS = ['.pdf']
COMPRESSED = ['.rar', '.zip', '.7z', '.bzip2',
              '.gzip', '.tar', '.wim', '.xz', ]
SCRIPTS = ['.ahk', '.js', '.json']

# NOMES DAS PASTAS A SEREM CRIADAS CASO SEJA NECESSÁRIO
EXECUTAVEIS_FOLDER = './Executaveis/'
IMAGES_FOLDER = './Imagens/'
DOC_FOLDER = './Documentos/'
PDF_FOLDER = './Pdfs/'
COMPACT_FOLDER = './Compactados/'
SCRIPT_FOLDER = './Scripts/'
VIDEOS_FOLDER = './Videos/'


def printHeader():
    print('Brock Organiser - Python [Version.2 - July 03, 2018]\n')
    print('Lista de arquivos e pastas encontrados:\n')


def getFilesList(path):
    return os.listdir(path)


def printAllFilesInFolder(allFilesArray):
    for i in range(0, len(allFilesArray)):
        print('{}\n'.format(allFilesArray[i]))
    return


def createDestinyFolder(file_folder):
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)

def organizer(file_folder, cont_for):
    createDestinyFolder(file_folder)
    os.rename(os.path.join('./', cont_for),
              os.path.join(file_folder, cont_for))  # move o arquivo
    # Printa a ação que foi realizada
    print('\tfoi movido << {} >>'.format(cont_for))
    return


def extractFileExtension(fileName):
    return str(fileName[fileName.rfind('.'):])


printHeader()
allFiles = getFilesList(PATH)
printAllFilesInFolder(allFiles)

for fileName in allFiles:
    fileExtension = extractFileExtension(fileName)
    # ------ Arquivos Executáveis
    if fileExtension in EXECUTABLES:
        organizer(EXECUTAVEIS_FOLDER, fileName)
        continue

    # ------ Arquivos Imagens
    if fileExtension in IMAGES:
        organizer(IMAGES_FOLDER, fileName)
        continue

    # ------ Arquivos Documentos
    if fileExtension in DOCUMENTS:
        organizer(DOC_FOLDER, fileName)
        continue

    # ------ Arquivos Pdfs
    if fileExtension in PDFS:
        organizer(PDF_FOLDER, fileName)
        continue

    # ------ Arquivos Compactados
    if fileExtension in COMPRESSED:
        organizer(COMPACT_FOLDER, fileName)
        continue

    # ------ Arquivos Scripts
    if fileExtension in SCRIPTS:
        organizer(SCRIPT_FOLDER, fileName)
        continue

    # ------ Arquivos Scripts
    if fileExtension in VIDEOS:
        organizer(VIDEOS_FOLDER, fileName)
        continue

print('\nArquivos organizados! =)')

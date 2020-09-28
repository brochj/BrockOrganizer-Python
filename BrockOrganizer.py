# -*- coding: utf-8 -*-
"""
@author: Oscar Broch Jr. - https://github.com/brochj
Created on Sun May 27 13:25:42 2018
Last Update: August 06, 2019
based on: https://www.geeksforgeeks.org/junk-file-organizer-python/
"""

import os
from gui import GUI

PATH = './'
# File extensions that will be organized
EXTENSIONS = {
    "EXECUTABLES": ['.exe', '.msi', '.jar', '.apk'],
    "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp',
               '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd'],
    "VIDEOS": [".3gp", ".avi", ".flv", ".mng", ".mov", ".mp4", 
            ".mpeg", ".mpg", ".qt", ".vob", ".webm", ".wmv"],
    "DOCUMENTS": ['.doc', '.docm', '.docx', '.dotx', '.dox',
             '.epub', '.fdf', '.ods', '.odt', '.pages', '.ppt',
              '.pptx', '.txt', '.xls', '.xlsx', '.xps'],
    "PDFS": ['.pdf'],
    "COMPRESSED": ['.rar', '.zip', '.7z', '.bzip2',
                   '.gzip', '.tar', '.wim', '.xz', ],
    "SCRIPTS": ['.ahk', '.js', '.json'],
}


def print_header():
    print('Organizer Files - Python [v0.0.2 - July 22, 2019]\n')
    print('author: Oscar Broch Jr. - https://github.com/brochj\n')
    return


def get_files_list(path):
    return os.listdir(path)


def print_all_user_files(all_files_array):
    print('List of files and folders found:\n')
    for i in range(0, len(all_files_array)):
        print(f'{all_files_array[i]}')
    return


def create_destiny_folder(file_folder):
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)


def move_file_to_destiny_folder(file_name, destiny_folder_name):
    try:
        os.rename(os.path.join('./', file_name),
                    os.path.join(destiny_folder_name, file_name))
    except:
        pass


def organizer(file_name, destiny_folder_name):
    create_destiny_folder(destiny_folder_name)
    move_file_to_destiny_folder(file_name, destiny_folder_name)
    print(f'moved << {file_name} >>')
    return


def extract_file_extension(file_name):
    return str(file_name[file_name.rfind('.'):])


def main():
    gui = GUI()
    print_header()
    all_user_files = get_files_list(gui.path)
    print_all_user_files(all_user_files)
    for file_name in all_user_files:
        user_file_extension = extract_file_extension(file_name)

        for file_type, extensions_list in EXTENSIONS.items():
            for extension in extensions_list:
                if user_file_extension == extension:
                    organizer(file_name, file_type.capitalize())

    print('\nYour files are now organized! =) \n')
    return


if __name__ == "__main__":
    main()

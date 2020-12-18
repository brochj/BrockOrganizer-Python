# -*- coding: utf-8 -*-
"""
@author: Oscar Broch Jr. - https://github.com/brochj
Created on Sun May 27 13:25:42 2018
Last Update: Dec 18, 2020
based on: https://www.geeksforgeeks.org/junk-file-organizer-python/
"""

import os
from gui import GUI

PATH = "./"
# File extensions that will be organized
# If you want add another folder, just add a new key inside "EXTENSIONS" Dict
EXTENSIONS = {
    "EXECUTABLES": [".exe", ".msi", ".jar", ".apk"],
    "IMAGES": [
        ".jpeg",
        ".jpg",
        ".tiff",
        ".gif",
        ".bmp",
        ".png",
        ".PNG",
        ".bpg",
        ".svg",
        ".heif",
        ".psd",
    ],
    "VIDEOS": [
        ".3gp",
        ".avi",
        ".flv",
        ".mng",
        ".mov",
        ".mp4",
        ".mpeg",
        ".mpg",
        ".qt",
        ".vob",
        ".webm",
        ".wmv",
    ],
    "DOCUMENTS": [
        ".accdb",
        ".doc",
        ".docm",
        ".docx",
        ".dotx",
        ".dox",
        ".epub",
        ".fdf",
        ".ods",
        ".odt",
        ".pages",
        ".ppt",
        ".pptx",
        ".txt",
        ".xls",
        ".xlsx",
        ".xps",
    ],
    "PDFS": [".pdf"],
    "COMPRESSED": [
        ".rar",
        ".zip",
        ".7z",
        ".bzip2",
        ".gzip",
        ".tar",
        ".wim",
        ".xz",
    ],
    "SCRIPTS": [".ahk", ".js", ".json", ".mq5"],
    # "NEW FOLDER 1": [".whatever", ".extension", ".you", "want"]
}


def print_header():
    print("Brock Organizer Files - Python [v0.0.3 - Dec 18, 2020]\n")
    print("author: Oscar Broch Jr. - https://github.com/brochj\n")
    


def get_files_list(path):
    return os.listdir(path)


def print_all_user_files(all_files_array):
    print("List of files and folders found:\n")
    for i in range(0, len(all_files_array)):
        print(f"{all_files_array[i]}")
    


def create_destiny_folder(file_folder):
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)


def move_file_to_destiny_folder(path, file_name, destiny_folder_name):
    file_path = os.path.join(path, file_name)
    destiny_path = os.path.join(path, destiny_folder_name.capitalize(), file_name)

    try:
        os.rename(file_path, destiny_path)
        print(f"moved << {file_name} >>")
    except FileExistsError as e:
        print(f"\n\nERROR: Cannot move this file --->   {file_name}")
        print(e)
        print("\n\n")


def organizer(path, file_name, destiny_folder):
    create_destiny_folder(os.path.join(path, destiny_folder.capitalize()))
    move_file_to_destiny_folder(path, file_name, destiny_folder)

    


def extract_file_extension(file_name):
    return str(file_name[file_name.rfind(".") :])


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
                    organizer(gui.path, file_name, file_type)
    print("\nYour files are now organized! =) \n")
    


if __name__ == "__main__":
    main()
    input('Press any key to exit')
# TODO Create an "Undo" feature 
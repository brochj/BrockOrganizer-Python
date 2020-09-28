# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:40:54 2020

@author: broch
"""

import PySimpleGUI as sg
import pathlib
import sys


class GUI:
    def __init__(self):
        self.event = None
        self.values = None
        self.path = pathlib.Path().absolute()
        
        self.get_folder()


    def get_folder(self):
        layout = [
            [sg.InputText("./"), sg.FolderBrowse('Browse', initial_folder=self.path)],
            
            [sg.Submit('Organize Files'), sg.Cancel()],
            ]
        window = sg.Window('Select the paste', layout)
        # self.event, self.values = window.read()
        # self.path = self.values[0]
        
        # window.close()
        
        while True:
            self.event, self.values = window.Read()
            self.path = self.values[0]
            print(self.event)
            if self.event in ('Cancel', None):
                window.close()
                sys.exit("Script exit")
            elif self.event == 'Organize Files':
                break
            
        window.close()
        
    def show_logging(self, itens):
        layout = [[sg.Text('What would you like to hear rhymes about: ', size=(20,1))],
              [sg.Output(size=(30,30), key='OUTPUT')],
              [sg.Button('Print'), sg.Button('Exit')]]

        window = sg.Window('Logging', keep_on_top=True, layout=layout)
        
        log = ""
        for i in itens:
           log += i + "\n"
          
        
        while True:
            event, values = window.Read()
         
            print(event, values)
            if event in ('Exit', None):
                break
            elif event == 'Print':
                
                window['OUTPUT'].update(log)
            elif event == 'Clear':
                window['OUTPUT'].update('')
        
        window.close()
    

if __name__ == "__main__":
    gui = GUI()
    # gui.show_logging(['a','s','f','g'])
    
    
    pass


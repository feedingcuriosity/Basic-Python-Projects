#
# Python:       3.6.4
#
# Author:       Kasandra Wells
#
# Purpose:      The Tech Academy - Python Course, created script that creates a
#               GUI that allows users the ability to select a folder directory
#               from their system and display file path in text field.
#
# Tested OS:    This code was written and tested to work with Windows 10.
#

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
import browseDirectory_gui
import browseDirectory_main


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0) #this frees up the users memory from os module

def browse(self):
    filePath = filedialog.askdirectory(initialdir="/", title='Please select a directory')
    self.txt_browse1.insert(END, filePath)

if __name__ == "__main__":
    pass

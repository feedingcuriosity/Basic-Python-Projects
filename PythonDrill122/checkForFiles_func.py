#
# Python:       3.6.4
#
# Author:       Kasandra Wells
#
# Purpose:      The Tech Academy - Python Course, created GUI for a sample
#               window to check for files.
#
#
# Tested OS:    This code was written and tested to work with Windows 10.
#


import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import checkForFiles_main
import checkForFiles_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height using winfo module from tkinter
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    #messagebox must be imported explicitly to work. messagebox is a class with an askokcancel method.
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0) #this frees up the users memoryfrom os module

if __name__ == "__main__":
    pass


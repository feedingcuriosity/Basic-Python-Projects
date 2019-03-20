#
# Python:       3.6.4
#
# Author:       Kasandra Wells
#
# Purpose:      The Tech Academy - Python Course, created script that creates a
#               GUI that allows users the ability to select a source and destination
#               folder directory. The file path for both selections is then displayed
#               on the GUI. Next, the user can click a button that will automatically
#               move all .txt files in the source folder to the destination. Finally,
#               a database is created to keep record of the moved files and their
#               last modified timestamp.
#
# Tested OS:    This code was written and tested to work with Windows 10.
#

import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

import moveFile_func
import moveFile_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(800, 250)
        self.master.maxsize(800, 250)

        moveFile_func.center_window(self, 800, 250)

        self.master.title("Move .txt Files")
        self.master.configure(bg='#F0F0F0')
        self.master.protocol("WM_DELETE_WINDOW", lambda: moveFile_func.ask_quit(self))
        arg = self.master

        moveFile_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
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
import moveFile_main


def load_gui(self):
    self.btn_source = tk.Button(self.master, width=40, height=2, text='Select Source Folder',
                                command=lambda: moveFile_func.source(self))
    self.btn_source.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky=W)
    self.btn_destination = tk.Button(self.master, width=40, height=2, text='Select Destination Folder',
                                     command=lambda: moveFile_func.destination(self))
    self.btn_destination.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky=W)

    self.txt_source = tk.Entry(self.master, width=80, text='')
    self.txt_source.grid(row=0, column=1, rowspan=1, columnspan=2, padx=(0, 0), pady=(20, 10), sticky=N + W + E)
    self.txt_destination = tk.Entry(self.master, text='')
    self.txt_destination.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(0, 0), pady=(20, 10), sticky=N + W + E)

    self.btn_moveFiles = tk.Button(self.master, width=40, height=3, text='Move source .txt files to destination folder',
                                   command=lambda: moveFile_func.move_txt(self))
    self.btn_moveFiles.grid(row=3, column=0, columnspan=3, padx=(270, 10), pady=(25, 0), sticky=N + W)


if __name__ == "__main__":
    pass
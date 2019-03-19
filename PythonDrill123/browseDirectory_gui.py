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

from tkinter import *
import tkinter as tk

import browseDirectory_func
import browseDirectory_main


def load_gui(self):
    self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: browseDirectory_func.browse(self))
    self.btn_browse1.grid(row=0, column=0, padx=(200, 200), pady=(20, 20), sticky=W)

    self.txt_browse1 = tk.Entry(self.master, text='')
    self.txt_browse1.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(30, 30), pady=(0, 0), sticky=N + E + W)


if __name__ == "__main__":
    pass
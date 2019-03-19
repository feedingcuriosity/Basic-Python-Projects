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
import browseDirectory_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 105)
        self.master.maxsize(500, 105)

        browseDirectory_func.center_window(self, 500, 105)

        self.master.title("Select Directory")
        self.master.configure(bg='#F0F0F0')
        self.master.protocol("WM_DELETE_WINDOW", lambda: browseDirectory_func.ask_quit(self))
        arg = self.master

        browseDirectory_gui.load_gui(self)

help(tk)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
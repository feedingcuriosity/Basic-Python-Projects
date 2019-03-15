#
# Python:       3.6.4
#
# Author:       Kasandra Wells
#
# Purpose:      The Tech Academy - Python Course, created GUI for a sample
#               window to check for files.
#
# Tested OS:    This code was written and tested to work with Windows 10.
#        

from tkinter import *
import tkinter as tk

import checkForFiles_gui
import checkForFiles_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration (self.master is the parentwindow frame)
        self.master = master
        self.master.minsize(500,175) #(Height, Width)
        self.master.maxsize(500,175)
        # This CenterWindow method from checkForFiles_func will center our app on the user's screen
        checkForFiles_func.center_window(self,500,175)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: checkForFiles_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        checkForFiles_gui.load_gui(self)
        
                

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


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

import checkForFiles_main
import checkForFiles_func

#"self is the key to access all the class objects under parentwindow(frame)"
def load_gui(self):

    #define buttons
    #lambda = annonymous function
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse1.grid(row=1,column=0,padx=(10,10),pady=(50,5),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=2,column=0,padx=(10,10),pady=(5,5),sticky=W)
    self.btn_checkForFiles = tk.Button(self.master,width=12,height=2,text='Check for Files...')
    self.btn_checkForFiles.grid(row=3,column=0,padx=(10,0),pady=(5,5),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=3,column=4,columnspan=1,padx=(275,0),pady=(5,5),sticky=E)


    #built text boxes for data entry, that take up more than one column. Note: rowspan 1 is default and
    #doesn't need to be explicitly stated
    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=1,column=3,rowspan=1,columnspan=50,padx=(10,0),pady=(50,0),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=2,column=3,rowspan=1,columnspan=50,padx=(10,0),pady=(10,0),sticky=N+E+W)
    

    
#indicate pass because this script should not be run on its own and was created to be referenced by main.
#not as a standalone script.
if __name__ == "__main__":
    pass

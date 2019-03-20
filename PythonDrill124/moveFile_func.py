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
from os.path import join
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox, filedialog
import shutil

import moveFile_main
import moveFile_gui

#=======================
#PARENT WINDOW FUNCTIONS
#=======================
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

#=================================================
#SELECT SOURCE AND DESTINATION DIRECTORY FUNCTIONS
#=================================================
def source(self):
    sourceFilePath = filedialog.askdirectory(initialdir="/", title='Please select a directory')
    self.txt_source.insert(END, sourceFilePath)
    return sourceFilePath

def destination(self):
    destinationFilePath = filedialog.askdirectory(initialdir="/", title='Please select a directory')
    self.txt_destination.insert(END, destinationFilePath)
    return destinationFilePath


#===================================
#MoveFiles/DATABASE/OUTPUT FUNCTIONS
#===================================

def move_txt(self):
    conn = sqlite3.connect('txt_Files.db')
    def createTable():
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT, \
            col_lastModified INT \
            )")

    sourceFilePath = self.txt_source.get()
    destinationFilePath = self.txt_destination.get()
    fileList = os.listdir(sourceFilePath)
    fileCount = len(fileList)

    def find_txt():
        i = 0
        txtFiles = []
        while i < fileCount:
            fListSplit = fileList[i].split(".")  # By splitting the file name, we can determine if it is .txt file type
            if fListSplit[1] == "txt":
                txtFiles.append(fileList[i])
                i += 1
            else:
                i += 1
        return txtFiles

    find_txt()

    txtFiles = find_txt()
    txtFileCount = len(txtFiles)


    def find_mTime():
        i = 0
        filemTime = []
        while i < fileCount:
            fListSplit = fileList[i].split(".")  # By splitting the file name, we can determine if it is .txt file type
            if fListSplit[1] == "txt":
                filemTime.append(os.path.getmtime(os.path.join(sourceFilePath, fileList[i])))
                i += 1
            else:
                i += 1
        return filemTime

    find_mTime()

    filemTime = find_mTime()
    mTimeCount = len(filemTime)

    for i in filemTime:
        print(i)

    def create_list():
        i=0
        tableData = []
        while i < txtFileCount:
            tableData.append([txtFiles[i], filemTime[i]])
            i += 1
        return tableData

    create_list()
    tableData = create_list()
    print(tableData)

    def addfileName():
        sql = "INSERT INTO tbl_files (col_fileName, col_lastModified) VALUES (?,?)"
        for i in range(txtFileCount):
            cur.executemany(sql, tableData)


    def move_files():
        i=0
        while i < txtFileCount:
            shutil.move(os.path.join(sourceFilePath, txtFiles[i]), os.path.join(destinationFilePath, txtFiles[i]))
            i += 1


    with conn:
        cur = conn.cursor()
        createTable()
        addfileName()
        move_files()
        conn.commit()
    conn.close()



if __name__ == "__main__":
    pass
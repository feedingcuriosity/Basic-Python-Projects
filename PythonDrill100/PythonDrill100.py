#
# Python: 3.6.4
#
# Author: Kasandra Wells
#
# Purpose:  The Tech Academy - Python Course, completing my first drill.
#           Demonstrating how to create a script that will check a specific folder
#           on the hard drive, verify whether those files end with a ".txt" file
#           extension and if they do, print those qualifying file names and
#           their corresponding modified time-stamps to the console.
#

import os

fPath = 'C:\\Users\\kasan\\Course Python\\The-Tech-Academy-Basic-Python-Projects\\PythonDrill100'


fName = os.listdir(fPath) #This list includes the name of all files in the directory
fileCount=len(fName)#This variable is used to interate through all files in the directory

def checkFileType():
    i = 0
    while i < fileCount:
        fNameSplit = fName[i].split(".") #By splitting the file name, we can determine if it is .txt file type
        if fNameSplit[1] == "txt":
            print (fName[i], os.path.getmtime(os.path.join(fPath, fName[i])))
            #getmtime returns the time of last modificaiton in seconds
            i+=1
        else:
            i+=1

checkFileType()


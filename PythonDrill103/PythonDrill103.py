#
# Python: 3.6.4
#
# Author: Kasandra Wells
#
# Purpose:  The Tech Academy - Python Course, completing my second drill.
#           Demonstrating how to create a database and add new data into
#           the database using sqlite3 module.
#        


import sqlite3

conn = sqlite3.connect('drill103.db') #creates the database since one does not exist yet


#This block of code is the function used to create a table
def createTable():
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")

#This block of code checks the file type from the list
fList = ['information.docx', 'Hello.txt', 'myImage.png', \
         'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']
fileCount=len(fList)#This variable is used to interate through all files in the directory

def checkFileType():
    i = 0
    txtFiles = []
    while i < fileCount:
        fListSplit = fList[i].split(".") #By splitting the file name, we can determine if it is .txt file type
        if fListSplit[1] == "txt":
            txtFiles.append(fList[i])
            i+=1
        else:
            i+=1
    return txtFiles
    
checkFileType()

txtFiles = checkFileType()
txtFileCount = len(txtFiles)

#This loop will print the qualifying text files to the console.
for i in txtFiles:
    print (i)

#This function is used to populate the table with the qualifying text files.
def addValues():
    sql = "INSERT INTO tbl_files(col_fileName) VALUES (?)"
    for i in range(txtFileCount):
        cur.execute(sql, [txtFiles[i]])

#When connected to drill103.db, this code will call the functions to create table and add values.
with conn:
    cur = conn.cursor()
    createTable()
    addValues() 
    conn.commit()
conn.close()



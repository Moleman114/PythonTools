'''
 Codename:     Folderizer
 Version:      1.0
 Date:         2023-05-13
 Author:       Jett Bolen (Moleman114)
 Purpose:      File organizer based on a hardcoded dictionary
 Status:       Working

 Note for future me: Consider making this able to sort based on criteria other than file type

 TODO Add other file types
'''

import sys
import os

folderDict = {   # this holds pairs of 'content' (such as file extensions or keywords) and directory names to put them
    '.mp4': "videos",
    '.mkv': "videos",

    '.jpg': "images",
    '.png': "images",
    '.gif': "images",

    '.mp3': "audio"
}

if not(len(sys.argv) > 1):  # if no path has been input
    print("Please input at least one directory path to organize")


paths = iter(sys.argv)
for path in paths:  # for every path in the arguments
    if path != "Folderizer.py":
        filesInPath = os.listdir(path) # Gets the names of every file in that path
        
        # for every file in that path
        for file in filesInPath:

            # for every item in folderDict
            for filetype in folderDict:

                # if that file contains the key of the item in folderDict
                if file.endswith(filetype):
                    # if the corresponding folder doesn't exist
                    if not(os.path.exists(path + "/" + folderDict[filetype])):
                        # create it
                        os.mkdir(path + "\\" + folderDict[filetype])
                    # move the file into the folder
                    print("Moving file " + path + "\\" + file + " to " + path + "\\" + folderDict[filetype])
                    os.rename(path + "/" + file, path + "/" + folderDict[filetype] + "/" + file)
        print(path +  " has been organized")
                    


#! python

# Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

import os, shutil

# Selective copy - search the files with certain file extension such as .py, .pdf etc. and copy to new folder


toFind = [".pdf", ".txt", ".md"]


def copyTofolder(folder):

    folder = os.path.abspath(folder)

    sltDir = os.path.join(
        folder, "sltFolder"
    )  # this will create the folder in the src dir only with files in it

    # sltDir = os.path.abspath("sltFolder")  # sltFolder will be created in the current working directory only
    os.makedirs(sltDir, exist_ok=True)
    print("Created %s..." % (sltDir))

    # TODO: add dynamic folder naming (input by user) and search for specific file extensions

    found = False
    # first os.walk the directory
    for folderName, subfolders, fileNames in os.walk(folder):

        subfolders[:] = [
            d
            for d in subfolders
            if os.path.abspath(os.path.join(folderName, d)) != sltDir
        ]

        for fileName in fileNames:
            if any(fileName.lower().endswith(ext) for ext in toFind):
                shutil.copy(os.path.join(folderName, fileName), sltDir)
                found = True

    if not found:
        print("No files with %s found" % toFind)

    print("files are copied")
    print("Contents of %s are %s" % (sltDir, os.listdir(sltDir)))


copyTofolder(".")  # add folder path for dest

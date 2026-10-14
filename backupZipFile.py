#! python3
# backtoZipFile.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.


import zipfile, os


def makeZip(folder):

    # get abssolute folderpath
    folder = os.path.abspath(folder)

    number = 1

    while True:
        # keep incrementing the zipFile name by num
        zipfileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipfileName):
            break
        number += 1

    print("Creating %s..." % (zipfileName))
    backtoZip = zipfile.ZipFile(zipfileName, "w")

    for folderName, subfolders, fileNames in os.walk(folder):
        print("Adding %s..." % (folderName))
        backtoZip.write(folderName)
        for fileName in fileNames:  # bit complex, pay attention
            newBase = os.path.basename(folder) + "_"
            if fileName.startswith(newBase) and fileName.endswith(".zip"):
                continue
            backtoZip.write(os.path.join(folderName, fileName))

    backtoZip.close()
    print("Done.")


makeZip("../gclab")  # for only the specific folder, use relative path

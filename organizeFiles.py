# send2trash
import send2trash, os

baconfile = open("bacon.txt", "w+")
baconfile.write("Bapond-fd sv")

baconfile.seek(0)
print(baconfile.read())
baconfile.close()


# deleting this file (moving to trash, not deleting permanently)

send2trash.send2trash("bacon.txt")
print("baconfile is deleted")


# os walk
for folderName, subFolderName, filenames in os.walk("../gclab"):
    print("the current folder is: " + folderName)

    for subfolder in subFolderName:
        print("SUBFOLDER OF " + folderName + ": " + subfolder)

    for filename in filenames:
        print("FILE INSIDE " + folderName + ": " + filename)

    print("")

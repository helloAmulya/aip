import shutil, os

targetFile = input("Enter a target filename or path: ")

orgFilename = os.path.abspath(targetFile)

if not os.path.isfile(orgFilename):
    print("File not found:", orgFilename)
else:
    toadd_str = input("Enter the prefix you want to add: ")

    folder = os.path.dirname(orgFilename)
    filename = os.path.basename(orgFilename)

    prefixedFile = toadd_str + filename
    destination = os.path.join(folder, prefixedFile)

    print('Renaming "%s" to "%s"...' % (orgFilename, destination))

    shutil.move(orgFilename, destination)

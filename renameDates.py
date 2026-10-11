#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY


import shutil, os, re

datePattern = re.compile(
    r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$ 
    """,
    re.VERBOSE,
)

folderName = input(
    "enter a foldername [with ../ or ./ ] to rename dates or 'current' to for this folder only: "
)

if folderName == "current":
    folderName = "."


for amerFilename in os.listdir(folderName):
    mo = datePattern.search(amerFilename)

    if mo == None:
        print("No date found:", amerFilename)
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

    # absWorkingDir = os.path.abspath(".") # change this to give manual pathname

    absWorkingDir = os.path.abspath(folderName)

    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

    shutil.move(
        amerFilename, euroFilename
    )  # keep this commented out until you've checked that the printed source and destination paths are correct

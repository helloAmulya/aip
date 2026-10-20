#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.


import os, csv

os.makedirs("headerRemoved", exist_ok=True)

# TODO: add a logic to add the removed headers to a separate file with the original filenames attached
headerRows = []  # to collect the removed headers and filenames

for csvFilename in os.listdir("."):
    if not csvFilename.endswith(".csv"):
        continue
    print("Removing header from " + csvFilename + "...")

    csvRows = []
    with open(csvFilename, newline="") as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                headerRows.append([csvFilename, row])
                continue
            csvRows.append(row)
        with open(
            os.path.join("headerRemoved", csvFilename), "w", newline=""
        ) as csvFileObj:
            csvWriter = csv.writer(csvFileObj)
            # for row in csvRows:
            #     csvWriter.writerow(row)
            csvWriter.writerows(csvRows)

with open(
    os.path.join("headerRemoved", "headers.csv"), "w", newline=""
) as headerFileObj:
    headerWriter = csv.writer(headerFileObj)
    headerWriter.writerow(["filename", "header"])
    for filename, header in headerRows:
        headerWriter.writerow([filename, ", ".join(header)])

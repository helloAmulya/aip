import csv

# reading csv files
exampleFile = open("example1.csv")
exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)  # now the data is list of lists, we can access


# print("This will display the data on that row and col : ", exampleData[3][0])

# use the reader object to process all the rows then print
""" 
for row in exampleReader:
    print("Row #" + str(exampleReader.line_num) + " " + str(row)) 
"""
exampleFile.close()


# writing a csv
outputFile = open("new_output.csv", "w", newline="")  # newline to avoid double-space
outWrite = csv.writer(outputFile)

outWrite.writerow(["Hello, world!", "eggs", "bacon", "ham"])
outWrite.writerow(["whoami", "daddy", "prodigy", "strange"])
outputFile.close()


# we opened the file initially in 'w' mode, need to close and reopen to read
nout = open("new_output.csv")
outReader = csv.reader(nout)
outData = list(outReader)
print(outData)


# working with tsv files

csvFile = open("example2.tsv", "w", newline="")
csvWriter = csv.writer(csvFile, delimiter="\t", lineterminator="\n")
csvWriter.writerow(["apples", "oranges", "grapes"])
csvWriter.writerow(["spam", "spam", "spam", "spam"])
csvWriter.writerow(["ojophc", "cn41", "r23cac", "afads"])
csvFile.close()


tsout = open("example2.tsv")
# tsReader = csv.reader(tsout) # without delimiter the output will be not as accepted
tsReader = csv.reader(tsout, delimiter="\t")
tsData = list(tsReader)
print(tsData)

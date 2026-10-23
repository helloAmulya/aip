#! python3

import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))

print(wb.sheetnames)  # this prints the name of all the sheets in the workbook


sheet = wb["Sheet3"]  # checks if Sheet 3 is there and returns
print(sheet, type(sheet))

isActive = wb.active  # this prints the active sheet
print(isActive)


print(
    "This is — %s and Value in that cell — %s " % (isActive["A1"], isActive["A1"].value)
)  # get the cell and the value in it

print("——————————————————")
c = isActive["B1"]
print(c, c.value)
print("Row " + str(c.row) + ", Column " + c.coordinate + " is " + c.value)
# use c.row / c.column to get the number, use c.coordinate to get the column name
print("——————————————————")

print(isActive.cell(row=1, column=2))
print(isActive.cell(row=1, column=2).value)
for i in range(1, 8, 2):
    # range(start, stop, step) -> takes a jump of 2 rows: 1 -> 3 -> 5 -> 7
    print(i, isActive.cell(row=i, column=2).value)


print("——————————————————")
print(isActive.max_row)  # get dimensions of the sheet
print(isActive.max_column)

import openpyxl, pprint

example_wb = openpyxl.load_workbook("example.xlsx")
exsheet = example_wb["Sheet1"]

pprint.pprint(tuple(exsheet["A1":"C3"]))
print("\n")

# visualizing sheet data horizontally
for rowCellObj in exsheet["A1":"C3"]:
    for cellObj in rowCellObj:
        print(cellObj.coordinate, cellObj.value)
    print("——————END OF ROW——————")


isActive = example_wb.active
active_sheet_col = list(isActive.columns)
pprint.pprint(
    active_sheet_col[1]
)  # python indexing starts at 0, excel at 1, the col[1] is the 2nd in excel

for cell in active_sheet_col[1]:
    print(cell.value)

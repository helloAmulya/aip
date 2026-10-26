#! python3

from openpyxl import Workbook

wb = Workbook()  # initiate the workbook

# if you need to work on an individual sheet in a book, use 'wb.worksheet'

ws1 = wb.active  # set sheet 1 as active (default)

# wb.remove(wb.active) # Remove the default sheet

ws1.title = "Students"  # add title for sheet1

# create other sheets
ws2 = wb.create_sheet("Teachers")
ws3 = wb.create_sheet("Subjects")

# add data to each sheet

ws1.append(["Name", "Age"])  # dedault header row
ws1.append(["alice", "14"])  # data gets added after this

ws2.append(["Name", "Department"])
ws2.append(["mathew", "science"])

ws3.append(["Subject", "Code"])
ws3.append(["python", "404"])


# save the workbok

wb.save("School.xlsx")

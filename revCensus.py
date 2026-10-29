# revision of census data project with json file output

import openpyxl, pprint, json

print("opening workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")


sheet = wb["Population by Census Tract"]

countydata = {}

for row in range(2, sheet.max_row + 1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    countydata.setdefault(state, {})
    countydata[state].setdefault(county, {"tracts": 0, "pop": 0})

    countydata[state][county]["tracts"] += 1
    countydata[state][county]["pop"] += int(pop)


print("writing results...")
with open("censusNew.py", "w") as resultFile:
    resultFile.write("allData = " + pprint.pformat(countydata))
with open("censusTson.json", "w") as jsonFile:
    json.dump(countydata, jsonFile, indent=4)


resultFile.close()
print("done.")

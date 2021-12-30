import csv

data = []
headers = []

with open("dwarf_stars.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        data.append(i)
headers = data[0]
planetData = data[1:]

print(len(planetData))

for index, item in enumerate(planetData):
    try:
        item[3] = float(item[3]) * 0.102763
        item[4] = float(item[4]) * 0.000954588
    except:
        planetData.pop(index)

print(len(planetData))

planetData.sort(key=lambda planetData: planetData[0])

with open("dwarf_stars_fixed.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)
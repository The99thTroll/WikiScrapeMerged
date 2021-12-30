import csv

dataset1 = []
dataset2 = []

headers1 = []
headers2 = []

# Set Up

with open("dwarf_stars_fixed.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        dataset1.append(i)

with open("bright_stars.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        dataset2.append(i)
        
headers1 = dataset1[0]
headers2 = dataset2[0]

pData1 = dataset1[1:]
pData2 = dataset2[1:]

# Merging
planetData = []

header = headers1 + headers2
for index, item in enumerate(pData1):
    try:
        planetData.append(pData1[index] + pData2[index])
    except:
        pass
    
with open("final.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)
    csvWriter.writerows(planetData)
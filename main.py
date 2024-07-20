from outputData import outputData
import csv
from  flucCalc import flucCalc

# Setting up variables
ptID = "nabe"
ptURL = "https://b0b27394-ad79-571e-965a-2b97275913d2.cgm.bcdiabetes.ca/"
startdate = "2024-07-01T23:59:59"
enddate = "2024-07-13T23:59:59"

# Exporting CGM data from nightscout
outputData(ptID,ptURL, startdate, enddate)
csvfile = "ptData/" + ptID + "_entries.csv"

# filtering data inc. removing empty entries and getting heading indexes
with open(csvfile, encoding='cp437', errors="ignore") as file:
    data = list(csv.reader(file))
    headers = data[0]
    startDateIndex = headers.index('dateString')
    bgIndex = headers.index('glucose')
    data = data[1:] # remove headers
    filter_data = []
    for entry in data:
        if entry[bgIndex]:
            filter_data.append(entry)
    sorted_data = sorted(filter_data, key=lambda filter_data: filter_data[startDateIndex])

# calculate fluctuation defined as Time in rapid fluctuation (>0.55 mmol/l/5m)
fluc = flucCalc(sorted_data, startDateIndex, bgIndex)

print(f"Time in rapid fluctuation: {fluc:.2f}%")


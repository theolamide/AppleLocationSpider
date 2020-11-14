import requests
import re
import csv

from requests.models import Response

r = requests.get('https://www.apple.com/retail/storelist/')
rResponse = r.text.encode("utf-8")

toLook = re.findall(r'https://www.apple.com/retail/\w+', rResponse)[3:]
clean = re.compile('<.*?>')
collectedAddresses = []
# loop through resulting array and set individual store i
for i in range(0, len(toLook)):
    toAppend = []
    singleAddress = {
        "Street Address": "",
        "City": "",
        "State": "",
        "Zip": "",
        "Phone": "",
    }
    individualLink = toLook[i]
    # Go to the individual stores link
    individualStore = requests.get(individualLink)
    # encode the individual store response
    storePage = individualStore.text.encode("utf-8")
    # Find the address using the class tag. Every line has the tag, so we will have to go through them one by one
    storeAddress = re.findall(r'<p.*class=.hcard-address.*[\n]+.*?</p>', storePage)
    for address in storeAddress:
        strippedAddress = re.sub(clean, '', address)
        toAppend.append(strippedAddress)

    for j in range(0, 2):
        stripSingleAddress = toAppend[j].strip()
        splitSingleAddress = " ".join(stripSingleAddress.split())
        if j == 1:
            splitSingleAddress = splitSingleAddress.split(" ")
            if len(splitSingleAddress) == 5:
                singleAddress["City"] = splitSingleAddress[0]
                singleAddress["State"] = splitSingleAddress[1]
                singleAddress["Zip"] = splitSingleAddress[2]
                # singleAddress["Area Code"] = splitSingleAddress[3]
                singleAddress["Phone"] = splitSingleAddress[3] + '-' + splitSingleAddress[4]
            elif len(splitSingleAddress) > 5:
                City = ""
                for z in range(0, len(splitSingleAddress[:-4])):
                    City += " " + splitSingleAddress[:-4][z]
                singleAddress["City"] = City.strip(", ")
                singleAddress["State"] = splitSingleAddress[-4]
                singleAddress["Zip"] = splitSingleAddress[-3]
                singleAddress["Phone"] = splitSingleAddress[-2] + '-' + splitSingleAddress[-1]
        else:
            singleAddress["Street Address"] = splitSingleAddress

        if singleAddress not in collectedAddresses:
            collectedAddresses.append(singleAddress)

# print(collectedAddresses)
csvFile = open('AppleStoreAddresses.csv', 'w')
fieldNames = ["Street Address", "City", "State", "Zip", "Phone"]
with csvFile as exportCsv:
    writer = csv.DictWriter(exportCsv, lineterminator='\n', fieldnames=fieldNames)
    writer.writeheader()
    for element in collectedAddresses:
        writer.writerow(element)
csvFile.close()

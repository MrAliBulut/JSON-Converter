
import pandas # to convert and export json to excel
import json # to read and write json files 
import requests # to recieve data from api



#Gets the data from the desired api
def getJsonFromAPI(apiUrl):
    response = requests.get(apiUrl)

    if response.status_code == 200:
        return response.json()
    else:
        print("Unable to get data from API")
        return None


#Process the input JSON file if needed, then exporting a excel file from it
def processFile(filePath):
    with open(filePath,'r') as entry:
        JSON = json.load(entry)

        #Converting input file to excel
        df = pandas.DataFrame(JSON)
        df.to_excel("JSON_Converter/Output/Entries.xlsx", index= False)

        return JSON


#Detecting unique entries and exporting a excel file from it
def detectUniqueEntries(JSON):
    uniqueEntries_JSON = []
    for entry in JSON:
        if entry["status"] == "in":
            if entry not in uniqueEntries_JSON:
                uniqueEntries_JSON.append(entry)
    
        #Converting Unique Entries to excel
        df = pandas.DataFrame(JSON)
        df.to_excel("JSON_Converter/Output/uniqueEntries.xlsx", index= False)

    return uniqueEntries_JSON


def outputAsFile(uniqueEntries,filePath):
    with open(filePath, 'w') as output:
        json.dump(uniqueEntries,output)#,indent=4)    #indent can be used to beautify the json


#used to test in the first version of the code.
sampleJSON =[
    {"tc":"1","name": "a1 Doe", "age": 31, "email": "john.doe@example.com", "status": "in"},
    {"tc":"2","name": "a2 Doe", "age": 32, "email": "john.doe@example.com", "status": "in"},
    {"tc":"2","name": "a2 Doe", "age": 32, "email": "john.doe@example.com", "status": "in"},
    {"tc":"3","name": "a4 Doe", "age": 34, "email": "john.doe@example.com", "status": "in"},
    {"tc":"3","name": "a4 Doe", "age": 34, "email": "john.doe@example.com", "status": "in"},
    {"tc":"4","name": "a6 Doe", "age": 36, "email": "john.doe@example.com", "status": "in"},
    {"tc":"5","name": "Jane Smith", "age": 25, "email": "jane.smith@example.com","status": "out"}
]


outputPath = "JSON_Converter/Output/output.json" #pathway to dump file
inputFilePath = "JSON_Converter/Input/input.json"

outputAsFile(   detectUniqueEntries(processFile(inputFilePath)) #will detect and return unique entries   # outputAsFile(json,outputPath)
             ,outputPath)






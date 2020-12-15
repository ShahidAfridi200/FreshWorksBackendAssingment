import json
import time
import os

filePath = 'db.json'
data = {}
isScheduled = True

print("Application Started")
print("Enter file path or hit enter for default path")
path = input()



def startApp():

    while True:
        op = input ("Please input what operation you wish to perform. \n 1 to Create new Key. \n 2 to Read Key. \n 3 to Delete Key. \n 4 to exit. \n")
        if op == "1":
            f1 = input ("Please enter your key: ")

            f2 = input("Please enter value as JSON string: ")

            f3 = input("Please enter TimeToLive value in seconds or press enter for infinite TTL: ")

            if(len(f3)==0):
                f3 = -1

            createKeyValuePair(f1,f2,f3)

        elif op == "2":
            f1 = input("Please enter your key: ")

            readValueForKey(f1)

        elif op == "3":
            f1 = input("Please enter your key: ")

            deleteByKey(f1)
        elif op == "4":
            return
        else:
            print("Sorry, that was an invalid command!")



# Create a key value pair
def createKeyValuePair(key, value, ttl=-1):
    if key in data:
        print("key already exists")
    else:
        if(ttl != -1):
            currentTimeInSec = int(round(time.time()))
            ttl = currentTimeInSec+int(ttl)


        val = {"val": value, "ttl": ttl}
        newData = {key: val}
        data.update(newData)
        addToFile(data)
        print("Successfully created key value pair")


# Read value for key
def readValueForKey(key):
    if key not in data:
        print("key does not exists")
    else:
        print(data[key]["val"])

# Delete by key
def deleteByKey(key):
    if key not in data:
        print("key does not exists")
    else:
        del data[key]
        addToFile(data)
        print("Successfully deleted")


# Writing to file
def writeToFile(userFilePath):
    try:
        dictionary = {}
        json_object = json.dumps(dictionary, indent=4)
        with open(path, "w") as outfile:
            outfile.write(json_object)
            outfile.flush()
            os.fsync(outfile.fileno())
    finally:
        outfile.close()
    return



if (len(path) != 0):
    path = path + "/" + filePath
else:
    path = filePath

writeToFile(path)

def addToFile(data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

startApp()
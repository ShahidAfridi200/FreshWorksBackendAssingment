import time
import json
import os


print("Scheduler Started")
print("Enter file path or hit enter for default path for scheduling")
path = input()

if (len(path) != 0):
    path = path + "/db.json"
else:
    path = "db.json"

def removeExpiredKeys():
    print("Scheduler running!")
    if os.path.exists(path):
        loadFile = open(path)
        data = json.load(loadFile)
        l = []
        for v in data:
            ttl = data[v]["ttl"]
            if(ttl != -1):
                currentTimeInSec = int(round(time.time()))
                isExpired = data[v]["ttl"] - currentTimeInSec
                print(isExpired)
                if (isExpired <=0 ):
                    l.append(v)

        for i in range(0, len(l)):
            del data[l[i]]

        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)




while True:
    removeExpiredKeys()
    time.sleep(10)
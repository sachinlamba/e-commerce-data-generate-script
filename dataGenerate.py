import json;
#give correct file to convert to json file.
with open('amazondata_Phones.txt') as f:
    mylines = f.read().splitlines()
    objectStart = False
    saveArrayOfJsonObject = []
    for line in mylines:
        if(line == ""):
            objectStart = False
        if(objectStart):
            key_value_pair = line.split("=")
            try:
                saveArrayOfJsonObject[len(saveArrayOfJsonObject)-1][key_value_pair[0]] = key_value_pair[1]
            except:
                print("Error")
        if("ITEM" in line):
            objectStart = True
            saveArrayOfJsonObject.append({})
    #print(saveArrayOfJsonObject)
    json = json.dumps({"data" : saveArrayOfJsonObject});
    f = open("data.json","w")
    f.write(json)
    f.close()

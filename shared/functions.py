import os.path
import csv
import shared.classr as classr

encode = "utf-8"
sourceScript = "rng"
current_directory = os.path.dirname(__file__)
    
def getLocations():
    with open(current_directory + "/database/location.csv",encoding = encode) as locDB:
        
        locRows = csv.DictReader(locDB)
        locations = []
        for row in locRows:
            locID = int(row['locID'])
            mapID = row['mapID']
            locRegion = row['locRegion']
            locName = row['locName']
            mapCheckID = row['mapCheckID']
            event = bool(int(row['event']))
            itemID = int(row['itemID'])
            itemName = row['itemName']
            quantity = int(row['quantity'])
            progression = bool(int(row['progression']))
            nice = bool(int(row['nice']))
            party = bool(int(row['party']))
            crew = bool(int(row['crew']))
            item = bool(int(row['item']))
            script = row['script']
     
            locationObject = classr.location(locID,mapID,locRegion,locName,mapCheckID,event,itemID,itemName,quantity,progression,nice,party,crew,item,script)
            locations.append(locationObject)
            
    locDB.close()
    return locations

#def getItems:

def getIcon(itemID):
    with open(current_directory + "/database/itemTable.csv",encoding = encode) as itemDB:
        itemRows = csv.DictReader(itemDB) 
        for itemRow in itemRows:
            if int(itemRow['ID']) == itemID:
                icon = itemRow['3DIcon']
                itemDB.close
                return icon

def getLocFile(mapID,fileType):
    if fileType == 'script':
        for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__),os.pardir) + "/script/"):
            for file in files:
                if file.endswith('.scp') and file.find(mapID) >= 0:
                    return os.path.join(root, file)
                
    elif fileType == 'map':
        for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__),os.pardir) + "/map/"):
            for file in files:
                if file.endswith('.arb') and file.find(mapID) >= 0:
                    return os.path.join(root, file)
    else:
        raise Exception('Must specify either script or map for file retrieval or specify correct mapID')

def buildLocScripts(locID, source):

    #only build on set of scripts for river valley long shoreline, chests for dawn version share flags
    if locID == 47:
        locID = 44
    elif locID == 48:
        locID = 45
    elif locID == 49:
        locID = 46
        
    if source:
        scriptCall = sourceScript + ':' + str(locID).zfill(4)
    else:
        scriptCall = str(locID).zfill(4)
    return scriptCall

def writeStringToBytes(byteArray,offset,bytesToWrite):
    bytesToWrite = bytesToWrite.encode('utf-8')
    curOffset = offset
    
    for byte in bytesToWrite:
        byteArray[curOffset] = byte
        curOffset+=1

    return byteArray

def combineShuffledLocAndItem(shuffledLocation,inventory):
    locID = shuffledLocation.locID
    mapID = shuffledLocation.mapID
    locRegion = shuffledLocation.locRegion
    locName = shuffledLocation.locName
    mapCheckID = shuffledLocation.mapCheckID
    event = shuffledLocation.event
    itemID = inventory.itemID
    itemName = inventory.itemName
    quantity = inventory.quantity
    progression = inventory.progression
    nice = inventory.nice
    party = inventory.party
    crew = inventory.crew
    item = inventory.item
    script = shuffledLocation.script

    return classr.location(locID,mapID,locRegion,locName,mapCheckID,event,itemID,itemName,quantity,progression,nice,party,crew,item,script)

def copyLocationToNewLoc(location):
    locID = location.locID
    mapID = location.mapID
    locRegion = location.locRegion
    locName = location.locName
    mapCheckID = location.mapCheckID
    event = location.event
    itemID = location.itemID
    itemName = location.itemName
    quantity = location.quantity
    progression = location.progression
    nice = location.nice
    party = location.party
    crew = location.crew
    item = location.item
    script = location.script

    return classr.location(locID,mapID,locRegion,locName,mapCheckID,event,itemID,itemName,quantity,progression,nice,party,crew,item,script)

def getIntRewards():
    with open(current_directory + "/database/interceptionRewards.csv",encoding = encode) as rewardDB:
        
        rewardRows = csv.DictReader(rewardDB)
        intRewards = []

        for row in rewardRows:
            stage = row['stage']

            rewards = []
            for index,col in enumerate(row):
                if row[col] == '' or row[col] == None:
                    break
                elif index == 0:
                    pass
                else: 
                    rewards.append(row[col])

            stageReward = classr.interceptReward(stage,rewards)
            intRewards.append(stageReward)
            
    rewardDB.close()
    return intRewards
            
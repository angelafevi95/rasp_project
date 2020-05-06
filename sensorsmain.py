from dht import *
from mq2 import *
# from bht1750 import *

from ldr import ldr
from sound import sound
from mongoDB import mongoDB
from datetime import datetime 

## Send objects to mongoDB using date as key 
now = datetime.now()
# dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string = now.strftime("%d%m%Y%H%M")

print("date and time =", dt_string)	

########################################## Create sensor objects:

ldr1 = ldr(11)
dht = dht()
mq = MQ()
sound = sound()

########################################## Light measures
# bus = smbus.SMBus(1)
# sensor = bht1750(bus)

# print("Sensitivity: ", sensor.mtreg)
# measure = sensor.measure_high_res()

# print ("Light Level ", measure)

# lux = ldr1.get_lux()

# print(lux)

##########################################  Temperature and humidity measures
# hum, temp = dht.get_data()

# print("Humidity", hum, "%")
# print("temperature", temp, "ªC")

########################################## Air quality measures 

# listLPG, listCO, listSMOKE = mq.get_data()

# print("LPG", listLPG)
# print("CO", listCO)
# print("SMOKE", listSMOKE)

def createLists():
    ldrList = []
    dhtHumList = []
    dhtTempList = []
    mqSmokeList = []
    soundList = []

    for i in range(0,5):
        ldrList.append(ldr1.get_lux())
        hum, temp = dht.get_data()
        soundList.append(sound.voltCalculation())
        dhtHumList.append(hum)
        dhtTempList.append(temp)
        listLPG, listCO, listSMOKE = mq.get_data()
        mqSmokeList.append(listSMOKE)

        time.sleep(2)

    return ldrList, dhtHumList, dhtTempList, mqSmokeList, soundList 

def createDict(ldrList, dhtHumList, dhtTempList, mqSmokeList, soundList, sensorDict ):
    

    # sensorDict['date'] = dt_string
    # sensorDict['ldr'] = ldrList
    # sensorDict ['Hum'] = dhtHumList
    # sensorDict['Temp'] = dhtTempList
    # sensorDict['Smoke'] = mqSmokeList
    # sensorDict['Sound'] = soundList

    sensorDict['date'].append(dt_string)
    sensorDict['ldr'].append(ldrList)
    sensorDict ['Hum'].append(dhtHumList)
    sensorDict['Temp'].append(dhtTempList)
    sensorDict['Smoke'].append(mqSmokeList)
    sensorDict['Sound'].append(soundList)

    return sensorDict

ldrList, dhtHumList, dhtTempList, mqSmokeList, soundList  = createLists()
sensorDict = {}
sensorDict = createDict(ldrList, dhtHumList, dhtTempList, mqSmokeList, soundList, sensorDict)

mongo = mongoDB()

records = mongo.getCollection()
countDocs = mongo.getCountDocs(records)
print("Count", countDocs)

mongo.importData(sensorDict, records)



print("It's works!")

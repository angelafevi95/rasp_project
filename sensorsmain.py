from dht import *
from mq2 import *
# from bht1750 import *

from ldr import ldr

########################################## Light measures
# bus = smbus.SMBus(1)
# sensor = bht1750(bus)

# print("Sensitivity: ", sensor.mtreg)
# measure = sensor.measure_high_res()

#from bht1750 import *
# print ("Light Level ", measure)

# ldr1 = ldr(11)

# lux = ldr1.get_lux()
# print(lux)

##########################################  Temperature and humidity measures
# dht = dht()
# hum, temp = dht.get_data()

# print("Humidity", hum, "%")
# print("temperature", temp, "ªC")

########################################## Air quality measures 

# mq = MQ()
# listLPG, listCO, listSMOKE = mq.get_data()

# print("LPG", listLPG)
# print("CO", listCO)
# print("SMOKE", listSMOKE)





print("It's works!")

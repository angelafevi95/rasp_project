from dht import *
from mq2 import *
<<<<<<< HEAD
# from bht1750 import *

from ldr import *

## Sound noise measures
# bus = smbus.SMBus(1)
# sensor = bht1750(bus)

# print("Sensitivity: ", sensor.mtreg)
# measure = sensor.measure_high_res()
=======

#from bht1750 import *

>>>>>>> 6c21f355fe776767d47416b2834eeb1370d20980

# print ("Light Level ", measure)

## Temperature and humidity measures
# dht = dht()
# hum, temp = dht.get_data()

# print("HUmidity", hum, "%")
# print("temperature", temp, "ªC")

# ## Air quality measures 
# mq = MQ()
# listLPG, listCO, listSMOKE = mq.get_data()

# print("LPG", listLPG)
# print("CO", listCO)
# print("SMOKE", listSMOKE)

<<<<<<< HEAD
ldr = ldr(11)

print("Lux: ", ldr.get_lux())



=======
>>>>>>> 6c21f355fe776767d47416b2834eeb1370d20980
print("It's works!")

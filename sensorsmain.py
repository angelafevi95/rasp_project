
from bht1750 import *

bus = smbus.SMBus(1)
sensor = bht1750(bus)

print("Sensitivity: ", sensor.mtreg)
measure = sensor.measure_high_res()

print ("Light Level ", measure)

print ("Main done ")
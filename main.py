
from dht import dht 
from mq2 import *
import sys, time 

dht = dht()
hum, temp = dht.get_data()

print("HUmidity", hum, "%")
print("temperature", temp, "ªC")

mq = MQ()
listLPG, listCO, listSMOKE = mq.get_data()

print("LPG", listLPG)
print("CO", listCO)
print("SMOKE", listSMOKE)


print("main done bix")
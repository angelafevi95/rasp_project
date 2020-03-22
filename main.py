
from dht import dht 

dht = dht()
hum, temp = dht.get_data()

for data in hum: 
    print("HUmidity", data, "%")

print("temperature", temp, "ªC")

print("main done bix")
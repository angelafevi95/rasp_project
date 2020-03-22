
from dht import dht 

dht = dht()
hum, temp = dht.get_data()


print("HUmidity", hum, "%")

print("temperature", temp, "ªC")

print("main done bix")
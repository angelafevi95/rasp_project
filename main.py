import dht 


dht = dht()
hum, temp = dht.get_data()

dht.show_measures(hum, temp)

print("main done bix")
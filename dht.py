import Adafruit_DHT
import pandas as pd 
import time 
import matplotlib.pyplot as plt


class dht(): 

    ## New sensor creation
    self.__sensor = Adafruit_DHT.DHT11
    ## GPIO port 
    self.__port = 23

    def get_data(self):
        humidityList = []
        temperatureList = []

        humidity, temperaure = Adafruit_DHT.read_retry(self.__sensor, self.__port)
        humidityList.append(humidity)
        temperatureList.append(temperature)

        return humidityList, temperatureList

    def show_mesaures(self, humidity, temperature):
        print("Humidity", humidity, "Temperature", temperature)

    def write_to_excel(self, humidity, temperature ):
        df = pd.DataFrame({"HUMIDITY": humidity, "TEMPERATURE": temperature})
        df.to_excel("dht_measures.xlsx", sheet_name= "DHT", index = False)

    def create_figure(self, humidity, temperature ):
        plt.plot(humidity, temperature, 'ro')
        plt.title('Temperature and Humidity')
        plt.ylabel("Humidity")
        plt.xlabel('Temperature (Celsius)')
        plt.savefig('figura_test.png')

        plt.plot


dht = dht()
hum, temp = dht.get_data()

dht.show_measures(hum, temp)

print("dht hohoho")
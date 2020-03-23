
import spidev 
import time 
import so

class MCP3008:

    ## Intiliza SPI connection  
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.open(0, 0)
        self.max_speed_hz = 1000000# 1MHz

   ## Get SPI data 
   #  Input: channel (0-7)
   #  Output: data values 

   def getAnalogData(self, channel):
      
       adc = self.spi.xfer2([1, (8 + channel) << 4, ]0)
       data = ((adc[1]&3) << 8) + adc[2]

       return data  

   ## Convert SPI data to voltage
   # Input: SPI data 
   # Output: volts

   def getVolts(self, data):
      # Vref == Vdd LLC output  
        vref = 3.21  
       # if vref = 3.3 -> bits = 1032// if vref = 3.21 =>    996 bits
       volts = (data * vref) / float(996)
       volts = round(volts,1)

       return volts 

    def closeSPI(self):

        self.spi.closeSPI()

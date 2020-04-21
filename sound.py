import time
import math
from MCP3008 import MCP3008 as mcp 

class sound():

    KY_PIN                       = 1
    RL_VALUE                     = 2.2    # As per datasheet

    def __init__(self, analogPin = 1):
        self.KY_PIN = analogPin
        self.adc = mcp(1)

    def voltCalculation(self):
        vref = 5 ## LLC output 
        # If vref = 3.3 -> 1024bit => if vref = 3.21 -> 996.0bit
        raw_adc = self.adc.read(self.KY_PIN)

        vdig = (vref * raw_adc)/1023
        return vdig 


    print('sound')



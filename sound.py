import time
import math
from MCP3008 import MCP3008 as mcp 

class sound():

     RL_VALUE                     = 2.2    # As per datasheet

        ######################### Software Related Macros #########################
    CALIBARAION_SAMPLE_TIMES     = 50       # define how many samples you are going to take in the calibration phase
    CALIBRATION_SAMPLE_INTERVAL  = 500      # define the time interval(in milisecond) between each samples in the
                                            # cablibration phase
    READ_SAMPLE_INTERVAL         = 50       # define the time interval(in milisecond) between each samples in
    READ_SAMPLE_TIMES            = 5        # define how many samples you are going to take in normal operation 
                                            # normal operation

    def __init__(self, analogPin = 0):
        self.KY_PIN = analogPin
        self.adc = mcp(1)

    def voltCalculation(self, raw_adc):
        vref = 3.21 ## LLC output 
        # If vref = 3.3 -> 1024bit => if vref = 3.21 -> 996.0bit
        vdig = (996.0 * raw_adc)/vref
        return vdig 

    def sensorRead(self, KYpin ):

        val = 0.0
        for i in range(self.READ_SAMPLE_TIMES):
            rs +=  self.volCalculation(self.adc.read(KYpin))
            time.sleep(self.READ_SAMPLE_INTERVAL/1000.0)

        rs = rs/self.READ_SAMPLE_TIMES

        return rs

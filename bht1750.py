
import smbus 
import time 
import operator 

class bht1750():
   # Define constasts from the datasheet
   POWER_DOWN = 0x00
   POWER_ON = 0x01 #Power on 
   RESET = 0x07 # Reset data registered value 

   ONE_TIME_RE_MODE_1 = 0x20          

   def __init__(self, bus, addr=0x5):
       self.bus = bus 
       self.addr = addr
       self.power_down()
       self.set_sensivity()
    
   def power_down(self) :
       self._set_mode(self.POWER_DOWN)

   def _set_mode(self, mode):
        self.mode = mode 
        self.bus.write_byte(self.addr, self.mode)

   def power_on(self):
        self._set_mode(self.POWER_ON)

   def reset(self):
        self.power_on()#It has to be powered on before reseting 

   def oneshot_high_res(self):
        self._set_mode(self.ONE_TIME_RE_MODE_1)

   def set_sensivity(self, sensitivity = 69):

        if sensitivity < 31:
            self.mtreg = 31
        elif sensivity > 254:
            self.mtreg = 254
        else:
            self.mtreg = sensitivity 
        
        self.power_on()
        self._set_mode(0x40 | (self.mtreg >>5))
        self._set_mode(0x60 | (self.mtreg & 0x1f ))
        self.power_down()

   def get_result(self):

        data = self.bus.read_word_data(self.addr, self.mode)
        count = data >> 8 | (data&0xff)<<8
        mode2coeff = 2 if (self.mode & 0x03) == 0x01 else 1
        ratio = 1/(1.2 * (self.mtreg/69.0) * mode2coeff)

        return ratio

   def wait_for_result(self, additional =0):

        basetime = 0.018 if (self.mode & 0x03) == 0x03 else 0.128
        time.sleep(basetime * (self.mtreg/69.0) + additional)

   def do_measurement(self, mode, additional_delay = 0):

        self.reset()
        self._set_mode(mode)
        self.wait_for_result(additional = additional_delay) 
        return self.get_result()

   def measure_high_res(self, additional_delay = 0):
        return self.do_measurement(self.ONE_TIME_RE_MODE_1, additional_delay)


print("BHT DONE")









    

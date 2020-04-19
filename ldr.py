
import RPi.GPIO as GPIO
import time 


class ldr():

    def __init__(self, port):
        GPIO.setmode(GPIO.BCM)  ## Connected to BCM port 11 - GPIO17
        GPIO.setup(port, GPIO.IN)
        self.port = port 

    # def get_lux(self):
    #     luxList = [] 
    #     for i in range(0,5):
    #         luxList.append(GPIO.input(self.port))
    #         time.sleep(3)

    #     return luxList

    def get_lux(self):
        lux = GPIO.input(self.port)
        return lux
    

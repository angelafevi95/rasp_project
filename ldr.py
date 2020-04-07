
import RPi.GPIO as GPIO


class ldr():

    def __init__(self, port):
        GPIO.setmode(GPIO.BCM)  ## Connected to BCM port 11 - GPIO17
        GPIO.setup(port, GPIO.IN)

    def get_lux():
        return GPIO.input(self.port)

    

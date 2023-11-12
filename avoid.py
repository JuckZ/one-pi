
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

GPIO_OUT = 21

GPIO.setup(GPIO_OUT,GPIO.IN)

while True:
    if GPIO.input(GPIO_OUT)==0:
        print("There has a barrier")
        time.sleep(1)

GPIO.cleanup()

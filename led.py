import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

GPIO_R = 17
GPIO_G = 18
GPIO_B = 19
GPIO_BTN = 22

GPIO.setup(GPIO_R,GPIO.OUT)
GPIO.setup(GPIO_G,GPIO.OUT)
GPIO.setup(GPIO_B,GPIO.OUT)
GPIO.setup(GPIO_BTN,GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = 0

try:
    while True:
        button_pressed = not GPIO.input(GPIO_BTN)
        if button_pressed:
            led_state = (led_state + 1) % 3
            if led_state == 0:
                GPIO.output(GPIO_R,GPIO.HIGH)
                GPIO.output(GPIO_G,GPIO.LOW)
                GPIO.output(GPIO_B,GPIO.LOW)
            elif led_state == 1:
                GPIO.output(GPIO_R,GPIO.LOW)
                GPIO.output(GPIO_G,GPIO.HIGH)
                GPIO.output(GPIO_B,GPIO.LOW)
            elif led_state == 2:
                GPIO.output(GPIO_R,GPIO.LOW)
                GPIO.output(GPIO_G,GPIO.LOW)
                GPIO.output(GPIO_B,GPIO.HIGH)
            time.sleep(0.1)
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
GPIO.cleanup()

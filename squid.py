#squid.py Library

import RPi.GPIO as GPIO
import time

WHITE =  (030, 030, 030)
OFF =    (000, 000, 000)
RED =    (100, 000, 000)
GREEN =  (000, 100, 000)
BLUE =   (000, 000, 100)
YELLOW = (050, 050, 000)
PURPLE = (050, 000, 050)
CYAN =   (000, 050, 050)
ORANGE = (050, 015, 000)

class Squid:
	
    RED_PIN, GREEN_PIN, BLUE_PIN = 0, 0, 0

    red_pwm, green_pwm, blue_pwm = 0, 0, 0

    def __init__(self, red_pin, green_pin, blue_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.RED_PIN, self.GREEN_PIN, self.BLUE_PIN = red_pin, green_pin, blue_pin

        GPIO.setup(self.RED_PIN, GPIO.OUT)
        self.red_pwm = GPIO.PWM(self.RED_PIN, 500)
        self.red_pwm.start(0)
        
        GPIO.setup(self.GREEN_PIN, GPIO.OUT)
        self.green_pwm = GPIO.PWM(self.GREEN_PIN, 500)
        self.green_pwm.start(0)
        
        GPIO.setup(self.BLUE_PIN, GPIO.OUT)
        self.blue_pwm = GPIO.PWM(self.BLUE_PIN, 500)
        self.blue_pwm.start(0)
 
    def set_red(self, brightness):
        self.red_pwm.ChangeDutyCycle(brightness)
         
    def set_green(self, brightness):
        self.green_pwm.ChangeDutyCycle(brightness)
              
    def set_blue(self, brightness):
        self.blue_pwm.ChangeDutyCycle(brightness)
        
    def set_color(self, (r, g, b), brightness = 100):
        self.set_red(r * brightness / 100)
        self.set_green(g * brightness / 100)
        self.set_blue(b * brightness / 100)
        


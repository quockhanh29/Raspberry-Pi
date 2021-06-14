import RPi.GPIO as GPIO
import time
import subprocess

pin1 = 15
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)


for i in range(10):
    GPIO.output(pin1, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin1, GPIO.LOW)
    time.sleep(0.1)
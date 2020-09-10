#!/bin/python

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
RELAY=17
GPIO.setup(RELAY,GPIO.OUT)

if sys.argv[1] == "on":
    GPIO.output(RELAY,GPIO.HIGH)
else:
    GPIO.output(RELAY,GPIO.LOW)

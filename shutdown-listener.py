#!/usr/bin/env python

#import OLED_SCRIPT
import time
import RPi.GPIO as GPIO
import subprocess

# To disable warnings that pop up that don't seem to impact function but are anoying.
GPIO.setwarnings(False)

# Pin and Ground listener for buttonn pushes
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)                 #Pins for I/O Button
GPIO.wait_for_edge(3, GPIO.FALLING)

# Pins to be added for OLED Functions
#GPIO.setup(Null, GPIO.IN, pull_up_down=gpio.PUD_UP)             #Pins for OLED I/O
#GPIO.wait_for_egde(NUll, GPIO.FALLING)

# Command upon button pushes
subprocess.call(['shutdown', '-h', 'now'], shell=False)          #Command for I/O
#subprocess.call(['sudo', 'python', 'OLED_SCRIPT'], shell=False) #Command for OLED  

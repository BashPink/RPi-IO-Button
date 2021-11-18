#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

# To disable warnings that pop up that don't seem to impact function but are anoyying.
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)

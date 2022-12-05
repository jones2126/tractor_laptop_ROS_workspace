#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
i = 2
GPIO.setup(i, GPIO.OUT)
print " pin ", i, " setup"
time.sleep(0.2)
GPIO.output(i, GPIO.HIGH)
print " pin ", i, " output HIGH"
time.sleep(0.2)
GPIO.output(i, GPIO.LOW)
print " pin ", i, " output LOW - light on 5 seconds"
time.sleep(5)
GPIO.output(i, GPIO.HIGH)
print " pin ", i, " output HIGH - light off 5 seconds b4 EOJ"
time.sleep(5)

# Reset GPIO settings
GPIO.cleanup()

# End program cleanly with keyboard
print "EOJ"


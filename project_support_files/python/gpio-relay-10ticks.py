#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO | Relay
#--------------
# 26     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers
# matt's pins 2, 3, 4, 17, 27, 22, 10, 9

gpioList = [2, 3, 4, 17, 27, 22, 10, 9]
#layout from video gpioList = [26, 19, 13, 06, 12, 16, 20, 21] - pin 13 was a problem

for i in gpioList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
print " pins set"

# Sleep time variables

sleepTimeShort = 0.2
sleepTimeLong = 0.5
ticks = 0

# MAIN LOOP =====
# ===============
for i in gpioList:
	print "pin=", i
	GPIO.output(i, GPIO.LOW)
	time.sleep(sleepTimeShort)
	GPIO.output(i, GPIO.HIGH)
	time.sleep(sleepTimeLong)
	
# Reset GPIO settings
GPIO.cleanup()
# End program cleanly with keyboard
print " Quit"


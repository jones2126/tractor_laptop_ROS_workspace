#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO | Relay
#--------------
# 02     01
# 03     02
# 04     03
# 17     04
# 27     05
# 22     06
# 10     07
# 09     08

# initiate list with pin gpio pin numbers
# matt uses the pins 2, 3, 4, 17, 27, 22, 10, 9; I tried the pins from the video, but pin 13 was a problem so I switched to matt's pin layout
gpioList = [2, 3, 4, 17, 27, 22, 10, 9]
#layout from video gpioList = [26, 19, 13, 06, 12, 16, 20, 21] - pin 13 was a problem
print "Ctrl + C to stop"

for i in gpioList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Sleep time variables

sleepTimeShort = 0.2
sleepTimeLong = 0.1

# MAIN LOOP =====
# ===============

try:
    while True:
        for i in gpioList:
            GPIO.output(i, GPIO.LOW)
            time.sleep(sleepTimeShort);
            GPIO.output(i, GPIO.HIGH)
            time.sleep(sleepTimeLong);


# End program cleanly with keyboard
except KeyboardInterrupt:
    print "Stopping"

    # Reset GPIO settings

    GPIO.cleanup()


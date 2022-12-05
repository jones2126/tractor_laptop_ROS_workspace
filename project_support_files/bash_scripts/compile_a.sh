#!/bin/bash
# To run the script: $ bash compile_a.sh
#
# Run this script to "turn off" (unbind) the USB ports that are already programmed and to start the 
# compile process on the target device (left active) of the platformio statement
#
# (1 of 2) Comment OUT the target device you WILL be programming.  All other devices should have an active unbind statement.
# You want unbind statements to be executed so these devices are turned off and therefore retain their existing programming.
#
echo -n "1-1.3.1.2" > /sys/bus/usb/drivers/usb/unbind    # front_angle - new  /1-1.3.1.2/
echo -n "1-1.3.1.3" > /sys/bus/usb/drivers/usb/unbind    # transmission - new /1-1.3.1.3/
echo -n "1-1.3.1.4" > /sys/bus/usb/drivers/usb/unbind	 # steer_motor - new  /1-1.3.1.4/
# echo -n "1-1.3.3" > /sys/bus/usb/drivers/usb/unbind      # left speed - new   /1-1.3.3/
#
# (2 of 2) UN-COMMENT the target device/line for the platformio environment you WANT TO COMPILE
#
#  Platformio environments include: [env:joystick], [env:left_speed], [env:transmission], [env:front_angle], [env:steer_motor]
# sudo platformio run -t upload -e front_angle    # for [env:front_angle]
# sudo platformio run -t upload -e transmission   # for [env:transmission]
# sudo platformio run -t upload -e steer_motor    # for [env:steer_motor]
sudo platformio run -t upload -e left_speed     # for [env:left_speed]
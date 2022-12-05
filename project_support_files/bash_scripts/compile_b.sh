#!/bin/bash
# To run the script: $ bash compile_b.sh
#
# compile_b.sh
# this script to "turn on" the USB ports after the compile process is complete and launch the Teensy programs
#
# Comment OUT the board that IS being programmed via platformio in compile_a.sh.  It will not need the "bind" statement.  
# All other connected devices should be active so the script turns them back on since they were turned off in compile_a.sh.
#
#
echo -n "1-1.3.1.2" > /sys/bus/usb/drivers/usb/bind    # front_angle - new  /1-1.3.1.2/
echo -n "1-1.3.1.3" > /sys/bus/usb/drivers/usb/bind    # transmission - new /1-1.3.1.3/
echo -n "1-1.3.1.4" > /sys/bus/usb/drivers/usb/bind	   # steer_motor - new  /1-1.3.1.4/
# echo -n "1-1.3.3" > /sys/bus/usb/drivers/usb/bind      # left speed - new   /1-1.3.3/

# start the launch file that will initiate the Teensy's you want to test
cd /home/ubuntu/catkin_ws/src
roslaunch teensy_launch.launch
# roslaunch steer_test_launch.launch
# roslaunch transmission_test_launch.launch
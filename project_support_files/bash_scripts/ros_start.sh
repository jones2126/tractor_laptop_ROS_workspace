#!/bin/bash
# this script to startup ROS
# To run the script: $ bash ros_start.sh
cd /home/ubuntu/catkin_ws/src
# this starts 4 rosserial nodes that read teensy microcontrollers and publish
# steering angle, speed and control the steering motor and tranmission control motor
roslaunch teensy_launch.launch
# this starts the node to access the GPS signal connected to the udev port "<arg name="port" default="/dev/gps" />"
# the package will also parse the sentence and publish the data
roslaunch nmea_serial_driver.launch
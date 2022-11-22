#!/bin/bash
# this script to startup ROS
# To run the script: $ bash ros_start.sh
cd /home/tractor/catkin_ws/
roslaunch  /home/tractor/catkin_ws/src/nmea_navsat_driver/launch/nmea_to_odom.launch
rosrun  /home/tractor/catkin_ws/src/beginner_tutorials/scripts/gps_odom.py
 
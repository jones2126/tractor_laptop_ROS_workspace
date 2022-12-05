#!/bin/bash
# this script to run a series of rotopic publish commands to cmd_vel for testing purposes.
# The commands make use of the timer function.
#
timeout 10 rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
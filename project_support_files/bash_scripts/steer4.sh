#!/bin/bash
#steer4.sh
# go straight 10 seconds then turn left 5 seconds - full left is z: 1.0
timeout 25 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 1.5, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
timeout 12 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.8, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 1.0}}'
timeout 10 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.8, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: -0.1}}'
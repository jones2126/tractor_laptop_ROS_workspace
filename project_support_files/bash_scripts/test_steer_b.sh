#!/bin/bash
timeout 15 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.9, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'

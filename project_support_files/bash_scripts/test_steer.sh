#!/bin/bash
timeout 15 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.7, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
timeout 11 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.7, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: -0.5}}'
timeout 20 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.7, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
timeout 12 rostopic pub -r 10 teleop/cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.7, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: -0.5}}'
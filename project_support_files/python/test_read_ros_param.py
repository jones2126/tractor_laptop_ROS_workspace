#!/usr/bin/env python3
"""
Program to test reading ROS parameters using a single line .txt as input which 
contains float values representing a latitude and longitude
"""
import numpy as np
import rospy

origin = []

def load_file():
    global origin
    filename = 'last_position.txt'
    origin = np.loadtxt(filename, delimiter=',')

def write_params():
    global origin
    rospy.set_param('/origin_lat', float(origin[0]))
    rospy.set_param('/origin_lon', float(origin[1]))

def run_commands():
    rospy.init_node('move') # first thing, init a node!
    if rospy.has_param('/origin_lat'):
        origin_lat = rospy.get_param("/origin_lat")
        rospy.loginfo("Origin lat: %.6f", origin_lat)
    else:
        rospy.loginfo("origin_lat does not exist")
    if rospy.has_param('/origin_lon'):
        origin_lon = rospy.get_param("/origin_lon")
        rospy.loginfo("Origin lat: %.6f", origin_lon)
    else:
        rospy.loginfo("origin_lon does not exist")
    rospy.loginfo("Stopping!")
if __name__ == '__main__':
    load_file()
    write_params()
    run_commands()
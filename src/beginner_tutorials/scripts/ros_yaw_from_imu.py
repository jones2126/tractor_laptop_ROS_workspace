#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler

roll = pitch = yaw = 0.0
print("starting")
def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.orientation
    #print msg.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    yaw_in_degrees = (yaw * 180.0) / 3.141592653589793 # Convert yaw / heading to degrees 3.141592653589793
    # C = C + A
    # if( yaw_degrees < 0 ) yaw_degrees += 360.0
    # if( yaw_degrees < 0 ) yaw_degrees = yaw_degrees + 360.0
    print(yaw, yaw_in_degrees)

rospy.init_node('my_quaternion_to_euler')

# sub = rospy.Subscriber ('/imu', Imu, get_rotation)
sub = rospy.Subscriber ('imu/data', Imu, get_rotation)

r = rospy.Rate(1)
while not rospy.is_shutdown():    
    #quat = quaternion_from_euler (roll, pitch,yaw)
    #print quat
    r.sleep()
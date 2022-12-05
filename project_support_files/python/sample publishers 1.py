#!/usr/bin/python

# The program subscribes to the nmea_sentence topic, parses the GPRMC sentence and publish heading and velocity (gprmc_pub)
import rospy
import subprocess
import time

from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from actionlib_msgs.msg import GoalID


class DriveTeleop:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher("teleop/cmd_vel", Twist, queue_size=1)
        self.goal_cancel_pub = rospy.Publisher("move_base/cancel", GoalID, queue_size=1)
        # c example ros::Publisher transmission_PWM_val_pub("/transmission_PWM", &transmission_PWM_val);
        self.joy_sub = rospy.Subscriber("joy", Joy, self.on_joy, queue_size=1)


    def on_joy(self, data):

        # Drive sticks
        if data.buttons[4]: # deadman 5 button
            angular_vel = data.axes[0] 
            linear_vel = data.axes[1]

            # Publish Twist
            twist = Twist()
            twist.linear.x = linear_vel
            twist.angular.z = angular_vel
            self.cmd_vel_pub.publish(twist)


	# EStop
        if data.buttons[1]: # 2 button
            rospy.loginfo('Estop tractor')


	# Cancel move base goal
        if data.buttons[2]: # X button
            rospy.loginfo('Cancelling move_base goal')
            cancel_msg = GoalID()
            self.goal_cancel_pub.publish(cancel_msg)


def main():
    rospy.init_node("drive_teleop")
    # rospy.wait_for_service("/relay_cmd")
    controller = DriveTeleop()
    rospy.spin()
'''
Example drive_teleop.py
#!/usr/bin/python

import rospy
import subprocess
import time

from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from actionlib_msgs.msg import GoalID


class DriveTeleop:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher("teleop/cmd_vel", Twist, queue_size=1)
        self.goal_cancel_pub = rospy.Publisher("move_base/cancel", GoalID, queue_size=1)
        self.joy_sub = rospy.Subscriber("joy", Joy, self.on_joy, queue_size=1)


    def on_joy(self, data):

        # Drive sticks
        if data.buttons[4]: # deadman 5 button
            angular_vel = data.axes[0] 
            linear_vel = data.axes[1]

            # Publish Twist
            twist = Twist()
            twist.linear.x = linear_vel
            twist.angular.z = angular_vel
            self.cmd_vel_pub.publish(twist)


    # EStop
        if data.buttons[1]: # 2 button
            rospy.loginfo('Estop tractor')


    # Cancel move base goal
        if data.buttons[2]: # X button
            rospy.loginfo('Cancelling move_base goal')
            cancel_msg = GoalID()
            self.goal_cancel_pub.publish(cancel_msg)


def main():
    rospy.init_node("drive_teleop")
    # rospy.wait_for_service("/relay_cmd")
    controller = DriveTeleop()
    rospy.spin()


'''

'''
Example simple listener
#!/usr/bin/env python

# Import required Python code.
import roslib
roslib.load_manifest('node_example')
import rospy

# Import custom message data.
from node_example.msg import node_example_data

# Create a callback function for the subscriber.
def callback(data):
    # Simply print out values in our custom message.
    rospy.loginfo(rospy.get_name() + " I heard %s", data.message)
    rospy.loginfo(rospy.get_name() + " a + b = %d", data.a + data.b)

# This ends up being the main while loop.
def listener():
    # Get the ~private namespace parameters from command line or launch file.
    topic = rospy.get_param('~topic', 'chatter')
    # Create a subscriber with appropriate topic, custom message and name of callback function.
    rospy.Subscriber(topic, node_example_data, callback)
    # Wait for messages on topic, go to callback function when new messages arrive.
    rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pylistener', anonymous = True)
    # Go to the main loop.
    listener()
'''    
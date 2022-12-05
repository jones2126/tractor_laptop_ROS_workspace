import rospy
from std_msgs.msg import Int32
# credit: https://roboticsbackend.com/ros-topic-command-line-tools-practical-example-rostopic-and-rosmsg/

if __name__ == '__main__':
    rospy.init_node("counter_publisher")
    rate = rospy.Rate(5)
    pub = rospy.Publisher("/counter", Int32, queue_size=10)
    counter = 0
    rospy.loginfo("Publisher has been started.")

    while not rospy.is_shutdown():
        print("in the loop")
        counter += 1
        msg = Int32()
        msg.data = counter
        pub.publish(counter)
        rate.sleep()
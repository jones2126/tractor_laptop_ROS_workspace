#!/usr/bin/env python
#
#ROS_GUI_v5.py
# modelled after: https://raw.githubusercontent.com/ablarry91/quadcopter_IR_control/e782f49390d5527ed86678acda727f5d698c0c07/monocular_pose_estimator/src/Tkinter_GUI.py
# inspired by: https://raw.githubusercontent.com/mturktest123/rosGUI/master/ROS_GUI.py
import subprocess
import time
from tkinter import *
import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import NavSatFix, NavSatStatus, TimeReference
from geometry_msgs.msg import Twist
#from std_msgs.msg import NavSatFix

windowid1 = ''
cmd_RPi_login = "plink RPI_on_ZeroTier -pw ubuntu"  # command to login to RPi
working_directory1 = "--working-directory=/home/al"

def RPi_login_steps():
	time.sleep(.1)
	subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	time.sleep(5) # delay for the login process to the RPi
	subprocess.check_output(["xdotool", "type", "\n"])
	time.sleep(.5)
	subprocess.call(["xdotool", "windowfocus", windowid1])	

def LaunchCommand():
	global windowid1
	global cmd_RPi_login
	global working_directory1
	print("tbd")
	title1 = "login to RPi via VPN"  # title shows on the button - it can be any helpful text
	cmd_RPi_start = "bash ros_start.sh" # bash file on RPi which has the main start launch file	
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+1"])
	RPi_login_steps()
	#time.sleep(.1)
	#subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	#time.sleep(5) # delay for the login process to the RPi
	#subprocess.call(["xdotool", "windowfocus", windowid1])
	subprocess.check_output(["xdotool", "type", cmd_RPi_start + "\n"])

def JoystickCommand():
	global windowid1
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+2"])
	time.sleep(.1)
	subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	time.sleep(5) # delay for the login process to the RPi
	# this starts the joystick/gamepad process for the gamepad connected to the RPi on input js0
	# the 2.4 GHz gamepad should have been connected
	subprocess.check_output(["xdotool", "type", "roslaunch tractor_teleop drive.launch" + "\n"])

def NMEACommand():
	global windowid1
	global cmd_RPi_login
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+3"])
	time.sleep(.1)	
	subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	time.sleep(5) # delay for the login process to the RPi
	subprocess.check_output(["xdotool", "type", "cd /home/ubuntu/catkin_ws/src/nmea_navsat_driver/launch" + "\n"])
	time.sleep(.5)
	# this starts the node to access the GPS signal connected to the udev port "<arg name="port" default="/dev/gps" />"
	# the package will also parse the sentence and publish the data
	subprocess.check_output(["xdotool", "type", "roslaunch nmea_serial_driver.launch" + "\n"])

def OdomControl():
	global windowid1
	global cmd_RPi_login
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+4"])
	time.sleep(.1)	
	subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	time.sleep(5) # delay for the login process to the RPi
	subprocess.check_output(["xdotool", "type", "cd ~/catkin_ws" + "\n"])
	time.sleep(.5)
	subprocess.check_output(["xdotool", "type", "rosrun beginner_tutorials gps_odom.py" + "\n"])

def MoveBaseCommand():
	global windowid1
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+5"])
	time.sleep(.1)
	subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	time.sleep(5) # delay for the login process to the RPi
	subprocess.check_output(["xdotool", "type", "cd ~/catkin_ws" + "\n"])
	time.sleep(.5)
	subprocess.check_output(["xdotool", "type", "roslaunch lawn_tractor_sim lawn_tractor.launch" + "\n"])	

def RosbagCommand():
	global windowid1
	global cmd_RPi_login
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+6"])
	time.sleep(.1)	
	subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
	time.sleep(5) # delay for the login process to the RPi
	subprocess.check_output(["xdotool", "type", "bash ros_bagfile.sh" + "\n"])

def callback(data):	
	global low_res_angle_tk
	low_res_angle_tk.set(data.data)

def callback_gps(data):	
	global gps_status_tk
	gps_status_tk.set(data.status.status)

def callback_cmd_vel(msg):	
	global cmd_vel_angle
	global cmd_vel_speed
	cmd_vel_angle.set(msg.angular.z)
	cmd_vel_speed.set(msg.linear.x)

#create the GUI window
root = Tk()
root.geometry("600x150+30+30")
root.title('ROS GUI')
low_res_angle_tk = IntVar()
gps_status_tk = IntVar()
cmd_vel_angle = DoubleVar()
cmd_vel_speed = DoubleVar()
counter2 = IntVar()
counter3 = IntVar()
counter4 = IntVar()
frame = Frame(root)
frame.pack()

#build subframes into the main GUI frame
frame0 = Frame(frame)
frame01 = Frame(frame,borderwidth=2,relief=RAISED)
frame1 = Frame(frame)
frame2 = Frame(frame)
frame3 = Frame(frame)
frame4 = Frame(frame)

#indicate where you want the frames to be oriented
frame0.pack(side = TOP)
frame01.pack(side = TOP)
frame1.pack(side = TOP)
frame2.pack(side = TOP)
frame3.pack(side = TOP)
frame4.pack(side = TOP)

#create buttons
b0 = Button(frame0, text="Launch sensors", command=LaunchCommand)
b0.pack(side=LEFT)
b1 = Button(frame0, text="Start joystick", command=JoystickCommand)
b1.pack(side=LEFT)
b2 = Button(frame0, text="NMEA Driver",command=NMEACommand)
b2.pack(side=LEFT)
b3 = Button(frame0, text="GPS Odom",command=OdomControl)
b3.pack(side=LEFT)
b4 = Button(frame0, text="MoveBase",command=MoveBaseCommand)
b4.pack(side=LEFT)
b5 = Button(frame0, text="Rosbag",command=RosbagCommand)
b5.pack(side=LEFT)

#create text entries
frameE1 = Frame(frame01)
frameE2 = Frame(frame01)
frameE3 = Frame(frame01)
frameE4 = Frame(frame01)
frameE5 = Frame(frame01)
frameE6 = Frame(frame01)
frameE1.pack(side = LEFT)
frameE2.pack(side = LEFT)
frameE3.pack(side = LEFT)
frameE4.pack(side = LEFT)
frameE5.pack(side = LEFT)
frameE6.pack(side = LEFT)

#labels
label1 = Label(frameE1,text="low res angle")
label2 = Label(frameE2,text="gps_status")
label3 = Label(frameE3,text="heading")
label4 = Label(frameE4,text="volts")
label5 = Label(frameE5,text="cmd_speed")
label6 = Label(frameE6,text="cmd_angle")
label1.pack(side=TOP)
label2.pack(side=TOP)
label3.pack(side=TOP)
label4.pack(side=TOP)
label5.pack(side=TOP)
label6.pack(side=TOP)

#values for the labels
e1 = Label(frameE1, textvariable=low_res_angle_tk ,width = 10,justify=CENTER)
e1.pack(side=RIGHT)
e2 = Label(frameE2, textvariable=gps_status_tk ,width = 10,justify=CENTER)
e2.pack(side=RIGHT)
e3 = Label(frameE3, textvariable=counter3, width = 10,justify=CENTER)
e3.pack(side=RIGHT)
e4 = Label(frameE4, textvariable=counter4, width = 10,justify=CENTER)
e4.pack(side=RIGHT)
e5 = Label(frameE5, textvariable=cmd_vel_speed, width = 10,justify=RIGHT)
e5.pack(side=RIGHT)
e6 = Label(frameE6, textvariable=cmd_vel_angle, width = 10,justify=RIGHT)
e6.pack(side=RIGHT)

# open the initial terminal windows
#subprocess.call(["xdotool", "windowmove", windowid1.decode(), "20", "20"])
subprocess.call(["xdotool", "windowmove", windowid1, "20", "20"])
time.sleep(.1)
working_directory1 = "--working-directory=/home/al"
subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x20+450+20", working_directory1])
time.sleep(.5)
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)    
windowid1 = subprocess.check_output(["xdotool", "getactivewindow"])
print("windowid1", windowid1.decode(), windowid1)
subprocess.call(["xdotool", "windowmove", windowid1.decode(), "50", "575"]) 
time.sleep(.1)
subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=50x20+450+200", working_directory1])
time.sleep(.5)
windowid2 = subprocess.check_output(["xdotool", "getactivewindow"])
subprocess.call(["xdotool", "windowmove", windowid2.decode(), "1000", "575"])
print("windowid2", windowid2.decode())

rospy.Subscriber("/front_angle_low_res", Int16, callback)
rospy.Subscriber("/fix", NavSatFix, callback_gps)
rospy.Subscriber("/cmd_vel", Twist, callback_cmd_vel)
rospy.init_node('tkinterGUI', anonymous=True)


root.mainloop()
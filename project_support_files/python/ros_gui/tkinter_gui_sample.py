#!/usr/bin/env python
import Tkinter as tk
PKG = "my_ros_robotics"
import roslib; roslib.load_manifest(PKG)
import rospy
from sensor_msgs.msg import JointState #as JointState
from my_ros_robotics.msg import VoltageAndTemperature

rospy.init_node('tkinter_gui', anonymous=True)

# front_right_body_coxa_joint_data = None
# front_right_coxa_femur_joint_data = None
# front_right_femur_tibia_joint_data = None
#
# back_right_body_coxa_joint_data = None
# back_right_coxa_femur_joint_data = None
# back_right_femur_tibia_joint_data = None
#
# front_left_body_coxa_joint_data = None
# front_left_coxa_femur_joint_data = None
# front_left_femur_tibia_joint_data = None
#
# back_left_body_coxa_joint_data = None
# back_left_coxa_femur_joint_data = None
# back_left_femur_tibia_joint_data = None
#
# pan_joint_data = None
# tilt_joint_data = None

# def read_pan_joint_data(self, data=None):
#     pan_joint_data = data
#
# def read_tilt_joint_data(self, data=None):
#     tilt_joint_data = data
#
# #front right leg
# def read_front_right_body_coxa_joint_data(self, data=None):
#     front_right_body_coxa_joint_data = data
#
# def read_front_right_coxa_femur_joint_data(self, data=None):
#     front_right_coxa_femur_joint_data = data
#
# def read_front_right_femur_tibia_joint_data(self, data=None):
#     front_right_femur_tibia_joint_data = data
#
# #back right leg
# def read_back_right_body_coxa_joint_data(self, data=None):
#     back_right_body_coxa_joint_data = data
#
# def read_back_right_coxa_femur_joint_data(self, data=None):
#     back_right_coxa_femur_joint_data = data
#
# def read_back_right_femur_tibia_joint_data(self, data=None):
#     back_right_femur_tibia_joint_data = data
#
# #front left leg
# def read_front_left_body_coxa_joint_data(self, data=None):
#     front_left_body_coxa_joint_data = data
#
# def read_front_left_coxa_femur_joint_data(self, data=None):
#     front_left_coxa_femur_joint_data = data
#
# def read_front_left_femur_tibia_joint_data(self, data=None):
#     front_left_femur_tibia_joint_data = data
#
# #back left leg
# def read_back_left_body_coxa_joint_data(self, data=None):
#     back_left_body_coxa_joint_data = data
#
# def read_back_left_coxa_femur_joint_data(self, data=None):
#     back_left_coxa_femur_joint_data = data
#
# def read_back_left_femur_tibia_joint_data(self, data=None):
#     back_left_femur_tibia_joint_data = data

def read_JointState(self, data=None):
    joint_state_data = data
def read_TemperatureAndVoltge(self, data=None):
    temperature_and_voltage_data = data


try:
    root = tk.Tk()
except:
    print "cannot load tkinter"
    quit()

    #head

# JointState
# Velocity
# Temperature
# Voltage
# Alarm
# Shutdown

rospy.Subscriber('/walker/report/motor_temp_and_voltage',   JointState, read_TemperatureAndVoltge)
rospy.Subscriber('/joint_states',   JointState, read_JointState)

# rospy.Subscriber('/head_pan_controller/state',   JointState, read_pan_joint_data)
# rospy.Subscriber('/head_tilt_controller/state',   JointState, read_tilt_joint_data)
#
# rospy.Subscriber('/front_right_body_coxa_controller/state',   JointState, read_front_right_body_coxa_joint_data)
# rospy.Subscriber('/front_right_coxa_femur_controller/state',  JointState, read_front_right_coxa_femur_joint_data)
# rospy.Subscriber('/front_right_femur_tibia_controller/state', JointState, read_front_right_femur_tibia_joint_data)
#
# rospy.Subscriber('/back_right_body_coxa_controller/state',    JointState, read_back_right_body_coxa_joint_data)
# rospy.Subscriber('/back_right_coxa_femur_controller/state',   JointState, read_back_right_coxa_femur_joint_data)
# rospy.Subscriber('/back_right_femur_tibia_controller/state',  JointState, read_back_right_femur_tibia_joint_data)
#
# rospy.Subscriber('/front_left_body_coxa_controller/state',    JointState, read_front_left_body_coxa_joint_data)
# rospy.Subscriber('/front_left_coxa_femur_controller/state',   JointState, read_front_left_coxa_femur_joint_data)
# rospy.Subscriber('/front_left_femur_tibia_controller/state',  JointState, read_front_left_femur_tibia_joint_data)
#
# rospy.Subscriber('/back_left_body_coxa_controller/state',    JointState, read_back_left_body_coxa_joint_data)
# rospy.Subscriber('/back_left_coxa_femur_controller/state',   JointState, read_back_left_coxa_femur_joint_data)
# rospy.Subscriber('/back_left_femur_tibia_controller/state',  JointState, read_back_left_femur_tibia_joint_data)


window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry('+{}+{}'.format(window_width*2/3,0))
root.geometry('{}x{}'.format(window_width*1/3,window_height-275))
root.resizable(width=False, height=False)

w = tk.Canvas(root, width=window_width*1/3, height=window_height)
w.pack()
w.update()
print "internal x space of window"
print w.winfo_width()
print w.winfo_width()/6
print "y space of window"
print w.winfo_height()


# w.create_line(0, 0, w.winfo_width(), w.winfo_height())
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
# w.create_rectangle(50, 25, 150, 75, fill="blue")

#initialize graphics
motor = {}
for i in range(1,17):
    motor[i] = {}

start_x = 30
start_y = 30
size_x = 50
size_y = 50
spacing_gap_x = (w.winfo_width() - start_x * 2) / 8
spacing_gap_y = (w.winfo_width() - start_x * 2) / 8

spacing_x = 0
spacing_y = 1
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[8]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 1
spacing_y = 1
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[7]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 0
spacing_y = 2
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[9]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 3
spacing_y = 1
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[13]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 3
spacing_y = 0
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[14]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

laser = w.create_rectangle(position_x + 60, position_y + 10, position_x + 60 + size_x, position_y + 15, fill="red")


spacing_x = 6
spacing_y = 1
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[2]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 5
spacing_y = 1
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[1]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 6
spacing_y = 2
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[3]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 6
spacing_y = 4
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[5]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 5
spacing_y = 4
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[4]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 6
spacing_y = 5
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[6]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 0
spacing_y = 4
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[11]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 1
spacing_y = 4
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[10]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

spacing_x = 0
spacing_y = 5
position_x = start_x + spacing_gap_x * spacing_x
position_y = start_y + spacing_gap_y * spacing_y
motor[12]["block"] = w.create_rectangle(position_x, position_y, position_x + size_x, position_y + size_y, fill="green")

root.mainloop()

if __name__ == '__main__':

    while not rospy.is_shutdown():
    # joint_list = {
    #     motor1: front_right_body_coxa_joint_data,
    #     motor2: front_right_coxa_femur_joint_data,
    #     motor3: front_right_femur_tibia_joint_data,
    #     motor4: back_right_body_coxa_joint_data,
    #     motor5: back_right_coxa_femur_joint_data,
    #     motor6: back_right_femur_tibia_joint_data,
    #     motor7 front_left_body_coxa_joint_data,
    #     motor8 front_left_coxa_femur_joint_data,
    #     motor9 front_left_femur_tibia_joint_data,
    #     motor10 back_left_body_coxa_joint_data,
    #     motor11 back_left_coxa_femur_joint_data,
    #     motor12 back_left_femur_tibia_joint_data,
    #     motor13 back_left_femur_tibia_joint_data,
    #     motor14 back_left_femur_tibia_joint_data,
    #     }
        if front_right_body_coxa_joint_data != None:
            pass

    try:
        w.itemconfig(motor[1]["block"], fill="yellow")
        w.itemconfig(laser, fill="white")
    except:
        pass



# #!/usr/bin/env python
# import Tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.grid()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.quitButton = tk.Button(self, text='Quit',
#             command=self.quit)
#         self.quitButton.grid()
#
# app = Application()
# app.master.title('Sample application')
#
# app.mainloop()

import tkinter as tk
from tkinter import ttk
import rospy
from std_msgs.msg import Float32

"""
Subscribes to a ROS topic in line 27 and displays the result in a tkinter window

credit: https://www.pythontutorial.net/tkinter/tkinter-after/
credit: https://www.youtube.com/watch?v=EAAd5vXA8lE&t=260s

Before running make sure $ rostopic echo {topic} displays data 
This script can be started from the folder it resides in with $ python3 sensor_display.py

Minimun things to change/confirm:
1. line 4 - data type
2. line 28 - rostopic name to subscribe to and the data type
3. line 32 - title for the display box
4. line 35 - location for the box
5. line 46 - the number of decimal places to show (assuming the input value is float)

"""

class Display_Sensor_1(tk.Tk):

    def __init__(self):
        super().__init__()
        self.sub = rospy.Subscriber("bno085_rotvel", Float32, self.callback_sensor_1)
        self.sensor_1_data = tk.IntVar()

        # configure the root window
        self.title('IMU Rotational Velocity')
        self.resizable(0, 0)
        # width x height = 1920 x 1080 (in pixels) of the Ubuntu laptop
        self.geometry('225x70+1350+400')
        self['bg'] = 'black'
        
        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='black', foreground='red')
        self.label = ttk.Label(self, text=self.get_sensor_data(), font=('Digital-7', 20))
        self.label.pack(expand=True)
        self.label.after(1000, self.update)     # schedule an update every 1 second

    def callback_sensor_1(self, data):
        n = 2 # the number of decimal places to show
        s = '{}'.format(data.data)
        if 'e' in s or 'E' in s:
            self.sensor_1_data = '{0:.{1}f}'.format(f, n)
        else:
            i, p, d = s.partition('.')
            self.sensor_1_data =  '.'.join([i, (d+'0'*n)[:n]]) 
        # ref: https://stackoverflow.com/questions/783897/how-to-truncate-float-values
        # self.sensor_1_data = int(data.data)  # trims the float value from the rostopic to integer - any earlier version, keeping here fyi
        #print(self.sensor_1_data)   # used for debug
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)   # used for debug

    def get_sensor_data(self):
        return self.sensor_1_data

    def update(self):
        self.label.configure(text=self.get_sensor_data())
        self.label.after(1000, self.update)     # schedule another timer, update the label every 1 second 


 
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Display_Sensor_1()
    sensor.mainloop()
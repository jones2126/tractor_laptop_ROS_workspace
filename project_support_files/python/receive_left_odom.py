#!/usr/bin/env python3
#
# to make this executable run $ chmod +x receive_left_odom.py
# to execute, run $ ./receive_left_odom.py /dev/odom_left (aka ttyACM0)
import serial

if __name__ == '__main__':
    print('Please wait while the program is loading...')
    #ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    # ser = serial.Serial('/dev/odom_left', 9600, timeout=1)
    ser = serial.Serial('/dev/front_angle', 9600, timeout=1)
    ser.flush()
    print('at end of flush...')

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
#!/usr/bin/env python
import numpy as np
filename = 'cmd_vel_input2.txt'
x = np.loadtxt(filename, delimiter=',')
print (x)
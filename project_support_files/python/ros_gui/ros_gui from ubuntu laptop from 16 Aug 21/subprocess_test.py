#!/usr/bin/env python3

import subprocess
import time
import sys

cmd='ping -c5 google.com'.split()
sp = subprocess.call(cmd, shell=False)
print('step 1 end')
time.sleep(2)
print('step 2 end')
cmd_RPi_login = "plink RPI_on_ZeroTier -pw ubuntu"  # command to login to RPi
time.sleep(.1)
#subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
ssh = subprocess.Popen(["xdotool", "type", cmd_RPi_login + "\n"],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print (sys.stderr, "ERROR: %s" % error)
else:
    #print (result)
    time.sleep(1) 
    subprocess.check_output(["xdotool", "type", "\n"])
time.sleep(2)    
print('step 3 end')   
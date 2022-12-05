import subprocess
cmd = 'python script.py'

time.sleep(2)
cmd_RPi_login = "plink RPI_on_ZeroTier -pw ubuntu"  # command to login to RPi
time.sleep(.1)
subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
time.sleep(5) # delay for the login process to the RPi
subprocess.check_output(["xdotool", "type", "\n"])
time.sleep(.5)


p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate() 
result = out.split('\n')
for lin in result:
    if not lin.startswith('$'):
        print(lin)
echo -n "1-1.3.1.1" > /sys/bus/usb/drivers/usb/bind
echo -n "1-1.3.1.3" > /sys/bus/usb/drivers/usb/bind
rosrun rosserial_python serial_node.py /dev/odom_left


# python teststeer.py
# a function to monitor the heading and compare to the target heading
# The adjustment needs to be negative to simulate a left turn and positive to simulate a right turn
# if 


import time
def test_heading(target_heading, heading, tolerance, adjustment):
    lower = (target_heading - tolerance) % 360
    upper = (target_heading + tolerance) % 360
    # if lower > upper as in the case of target being 2 and tolerance being 5, lower will be 357 and upper will be 7
    # the while statement does not catch this condition; heading becomes 6 when turning left (negative adjustment) - so heading is
    # always less than lower (357) or greater than upper (7)
    # if lower < upper use "(heading < lower or heading > upper)" to control loop to increment heading
    # if lower > upper try "(heading > lower or heading < upper)" - we need neither to be true to exit the loop - target 2, upper 7, lower 357, eg heading = 6
    # 6 > 357 (false) or 6 < 7 (true)

    #print("current heading: %s, lower: %s, target: %s, uppper: %s" % (heading, lower, target_heading, upper))
    #while (lower <= heading <= upper):    # if heading is +/-  10 degrees from target keep looping
    # if (adjustment > 0) and (heading < lower or heading > upper):
    #   current heading: 8, lower: 1, target: 6, upper: 11
    while (heading < lower or heading > upper): 
        heading = (heading + adjustment) % 360
        print("current heading: %s, lower: %s, target: %s, upper: %s" % (heading, lower, target_heading, upper))
        #print(" Heading: %s" % heading)
        time.sleep(.2)
    print("passed target target_heading %s degrees at: %s" % (target_heading, time.strftime('%X %x %Z')))
    print(" Heading: %s" % heading)    

#*******************
# main
#*******************
# going left 88 -> 2 -> 262 -> 179 -> 88
# going right 88 -> 179 -> 262 -> 2 -> 88
print("Starting ....")
#test_heading(262, 2, 5, -5)    # worked 
#test_heading(179, 262, 5, -5)  # worked 
#test_heading(88, 179, 5, -5)  # worked
#test_heading(179, 88, 5, 5)  # worked
#test_heading(262, 179, 5, 5)  # worked
#test_heading(88, 2, 5, 5)  # worked
#test_heading(270, 2, 5, 5)  # worked 
#test_heading(100, 80, 5, 5)  # worked
#test_heading(11, 88, 5, -5) # works
#test_heading(2, 262, 5, 5) # does not work
#test_heading(2, 88, 5, -5)  # does not work
#test_heading(6, 88, 5, -5) # works
#test_heading(4, 88, 5, -5) # does not work
#test_heading(2, 88, 5, -1) # does not work
test_heading(3, 88, 2, -1)


print("EOJ ....")
#!/usr/bin/env python
def load_file():
    try:
        with open("cmd_vel_input.txt", "r") as f:
            #for line in f:
            data = f.readlines()
                #a = line.split()
            #print(line)
            print(data)
    except:
        #rospy.loginfo("File failed to load")
        print("File failed to open")
    finally:
        f.close()

if __name__ == '__main__':
    try:
        load_file()
    except:
        print("load_file function failed")

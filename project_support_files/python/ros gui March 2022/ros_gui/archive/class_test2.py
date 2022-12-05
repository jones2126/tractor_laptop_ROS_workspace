class Steps_to_Process:
    def __init__(self, data):
        self.data = data

class Display_Sensor_1:
    def __init__(self, data):
        self.data = data    

class ROS_GUI:
    def Inside_ROS_GUI_Class1(self, data):
        return Steps_to_Process(data)
    def Inside_ROS_GUI_Class2(self, data):
        return Display_Sensor_1(data)

object1 = ROS_GUI()
object2 = object1.Inside_ROS_GUI_Class1('data sent to class1/object2')
object3 = object1.Inside_ROS_GUI_Class2('data sent to class2/object3')
print (object3.data)
print(type(object3))

class Steps_to_Process:
    def __init__(self, data):
        self.data = data

class ROS_GUI:
    def SecondClass(self, data):
        return Steps_to_Process(data)

FirstClass = ROS_GUI()
#app = ROS_GUI()
SecondClass = FirstClass.SecondClass('now you see me')
print (SecondClass.data)
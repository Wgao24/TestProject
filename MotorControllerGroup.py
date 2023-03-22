from motor import Motor

class MotorControllerGroup:
    def __init__(self, list_of_motors:list):
        #self.motorList = []
        self.motorList = list_of_motors

    def addMotor(self,motor:Motor):
        self.motorList.insert(1, motor)

    def setSpeed(self,speed):
        for x in self.motorList:
            x.setSpeed(speed)

    def printMotorGroups(self):
        for x in self.motorList:
            print(x.speed)
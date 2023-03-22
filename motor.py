
class Motor:
    def __init__(self):
        self.speed = .5

    def setSpeed(self,speed):
        self.speed = speed
    def speedUp(self):
        self.speed = self.speed * 2
    def speedDown(self):
        self.speed = self.speed / 2
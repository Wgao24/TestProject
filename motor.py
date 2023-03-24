
class Motor:
    def __init__(self):
        self.speed = .5

    def setSpeed(self,speed):
        speed = max(-1, speed)
        speed = min( 1, speed)
        speed = speed^3##making a deadzone
        self.speed = speed
    def speedUp(self):
        self.speed = self.speed * 2
    def speedDown(self):
        self.speed = self.speed / 2
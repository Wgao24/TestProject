# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from motor import Motor
from MotorControllerGroup import MotorControllerGroup
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    x = Motor()
    y = Motor()
    x.speedUp()
    y.speedDown()
    group = MotorControllerGroup([x,y])
    #group.addMotor(x)
    #group.addMotor(y)
    group.printMotorGroups()
    group.setSpeed(.75)
    group.printMotorGroups()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

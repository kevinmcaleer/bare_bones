"""
This project uses the Pimoroni MicroPython build

https://github.com/pimoroni/pimoroni-pico/releases

"""
# Scared
# October 2022
# Kevin McAleer
from servo import Servo 
from range_finder import RangeFinder
from time import sleep

MAX_ANGLE = 70
MIN_ANGLE = 10
SCARED_DISTANCE = 30.0

class BareBones():

    rangefinder = RangeFinder()
    def __init__(self):
        self.servo = Servo(16)
        
    def scared_face(self):
        """ Open the Jaw and raise the eyebrows """
        
        self.servo.value(MAX_ANGLE)
        print('I\'m scared!')
        
    def not_scared_face(self):
        """ Close the Jaw and lower the eyebrows """
        
        self.servo.value(MIN_ANGLE)
        print('I\'m not scared anymore')

    def is_scared(self):
        if self.rangefinder.distance() <= SCARED_DISTANCE:
            return True
        else:
            return False
    

# Main Program
skeleton = BareBones()

while True:
    if skeleton.is_scared():
        skeleton.scared_face()
    else:
        skeleton.not_scared_face()
    sleep(0.25)
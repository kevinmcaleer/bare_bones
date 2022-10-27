from servo import Servo
from range_finder import RangeFinder
from time import sleep

MAX_ANGLE = 70
MIN_ANGLE = 10
SCARED_DISTANCE = 30

class BareBones():
    rangefinder = RangeFinder()

    
    def __init__(self):
        self.servo = Servo(16)
        
    def scared_face(self):
        self.servo(MAX_ANGLE)
        print('I am SCARED!')
        
    def not_scared_face(self):
        self.servo(MIN_ANGLE)
        print('I am not SCARED.')
        
    def is_scared(self):
        if self.rangefinder.distance() <= SCARED_DISTANCE:
            return True
        else:
            return False
        
        
# Main program

skeleton = BareBones()

while True:
    if skeleton.is_scared():
        skeleton.scared_face()
    else:
        skeleton.not_scared_face()
    sleep(0.25)
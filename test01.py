from machine import Pin

from time import sleep_us, ticks_us, sleep

class RangeFinder():
    trigger = Pin(0, Pin.OUT)
    echo = Pin(1, Pin.IN)
    
    def distance(self):
        """ Returns the distance in cm"""
        
        # Set the signal on and off to zero
        signalon = 0
        signaloff = 0
        
        #reset the trigger
        self.trigger.low()
        sleep_us(2)
        
        self.trigger.high()
        sleep_us(5)
        self.trigger.low()
        
        while self.echo.value() == 0:
            signaloff = ticks_us()
        while self.echo.value() == 1:
            signalon = ticks_us()
        
        elapsed_microseconds = signalon - signaloff
        self.duration = elapsed_microseconds
        self.distance_to_object = (elapsed_microseconds * 0.343) / 2
        return round(self.distance_to_object / 10, 1)
    
#create a range finder
rangefinder = RangeFinder()

while True:
    distance = rangefinder.distance()
    print(f'distance is {distance}')
    sleep(0.25)

from machine import Pin
from time import sleep_us, ticks_us, sleep

class RangeFinder():
    trigger = machine.Pin(0, Pin.OUT)
    echo = machine.Pin(1, Pin.IN)

    def distance(self):
        """ Returns the distance in cm """
        
        # set the signal on & off times to zero
        signalon = 0
        signaloff = 0
        
        # reset the trigger
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
        return round(self.distance_to_object / 10 ,1) 

# Create a rangefinder object
rangefinder = RangeFinder()

while True:
    # Get the distance and print to the console
    distance = rangefinder.distance()
    print(f'distance is {distance}')
    sleep(0.25)

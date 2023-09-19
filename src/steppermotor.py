import RPi.GPIO as GPIO 
from time import sleep             


class StepperMotor():
    
    def __init__(self) -> None:
        self.setup_gpios()

    def setup_gpios(self):
        GPIO.setmode(GPIO.BOARD)           # choose BCM or BOARD  
        GPIO.setup(11, GPIO.OUT)           # set pin 11 as an output- connected to STEP
        GPIO.setup(12, GPIO.OUT)		   # set pin 12 as an output- connected to DIR
        GPIO.setup(13, GPIO.OUT)		   # set pin 13 as an output- connected to NOT SLEEP
        # TODO: define denominator for setting stepper motor increment
        #enable the motor
        sleep(0.1) # check if sleep is necessary
        GPIO.output(13,1)
        sleep(0.5) # check if sleep is necessary

    def move_motor(self, n_steps: int=10) -> None:
        # set direction to +
        direction = n_steps > 0 # TODO: should we implement the negative case aswell?
        GPIO.output(12, direction)
        sleep(0.1) # check if necessary
        #start driving the motor
        try:  
            for _ in range(abs(n_steps)):  # TODO: can this be done in a cleaner way?  
                GPIO.output(11, 1)         # make one step
                sleep(0.02)
                GPIO.output(11, 0)         # reset, wait for next step  
                sleep(0.02)
                 
        except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
                # rethink if this makes sense
                GPIO.cleanup()             # resets all GPIO ports used by this program  
        
        GPIO.cleanup() # TODO: Dont get the logic behind this implementation...

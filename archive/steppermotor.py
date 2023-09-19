import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)           # choose BCM or BOARD  
GPIO.setup(11, GPIO.OUT)           # set pin 11 as an output- connected to STEP
GPIO.setup(12, GPIO.OUT)		   # set pin 12 as an output- connected to DIR
GPIO.setup(13, GPIO.OUT)		   # set pin 13 as an output- connected to NOT SLEEP
# TODO: define denominator for setting stepper motor increment

#enable the motor
sleep(0.1)
GPIO.output(13,1)
sleep(0.5)


nSteps = int(input("Input steps:"))

#set direction to +
direction = nSteps>0

GPIO.output(12,direction)
sleep(0.1)

#start driving the motor
try:  
	for i in range(abs(nSteps)):  
		GPIO.output(11,1)         # make one step
		sleep(0.02)
		GPIO.output(11,0)         # reset, wait for next step  
		sleep(0.02)
		
		      
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        GPIO.cleanup()                 # resets all GPIO ports used by this program  

GPIO.cleanup() # include in shutdown class

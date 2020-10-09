import time
import os

#specify sleep duration
sleepTime = 0.1

#Define some other stuff
brightnessIncrement  = 2
dutyCycle = 0

def pwmLed(pin, frequency, dutyCyclePercentage):
    command = "fast-gpio pwm %d %d %d" % (pin, frequency, dutyCyclePercentage)
    os.system(command)

#Infinite loop FTW
while True:
    dutyCycle=dutyCycle+brightnessIncrement

    #Assign GPIO 0 to the pwm duty cycle value
    pwmLed(0, 50, dutyCycle)

    #flip the value
    if(dutyCycle <= 0) or (dutyCycle >= 100):
        #reverse direction at 0 and 100
        brightnessIncrement = -brightnessIncrement
    # make the program pause
    time.sleep(sleepTime)
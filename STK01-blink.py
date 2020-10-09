import onionGpio
import time

#specify sleep duration
sleepTime = 0.5

#instance a PGIO object
gpio0 = onionGpio.OnionGpio(0)

# set output direction to zero (LOW) as default
gpio0.setOutputDirection(0)

#Initialize a variable to hold the value of the LED
ledValue = 1

# infinite loops FTW
while True:
        #Set GPIO value to ledvalue
        gpio0.setValue(ledValue)

        #flip the ledvalue (for that blinking effect)
        if ledValue == 1:
                ledValue = 0
        else:
            ledValue = 1
            
        time.sleep(sleepTime)
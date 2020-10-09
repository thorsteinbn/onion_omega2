import onionGpio
import time

#specify sleep duration
sleepTime = 0.5

#instance a PGIO object
gpio0 = onionGpio.OnionGpio(0)
gpio1 = onionGpio.OnionGpio(1)
gpio2 = onionGpio.OnionGpio(2)

# set output direction to zero (LOW) as default
gpio0.setOutputDirection(0)

#Initialize a variable to hold the value of the LED
ledValue = 1

gpio0.setValue(0)
gpio1.setValue(0)
gpio2.setValue(0)

# infinite loops FTW
while True:
        
        gpio0.setValue(1)
        time.sleep(sleepTime)
        gpio0.setValue(0)
        gpio1.setValue(1)
        time.sleep(sleepTime)
        gpio1.setValue(0)
        gpio2.setValue(1)
        time.sleep(sleepTime)
        gpio2.setValue(0)
import onionGpio
import time

#specify sleep duration
sleepTime = 0.5

#instance a PGIO object
gpio0 = onionGpio.OnionGpio(0)
gpio1 = onionGpio.OnionGpio(1)
gpio2 = onionGpio.OnionGpio(2)

gpio0._freeGpio()
gpio1._freeGpio()
gpio2._freeGpio()


# set output direction to zero (LOW) as default
gpio0.setOutputDirection(0)
gpio1.setOutputDirection(0)
gpio2.setOutputDirection(0)

#Set initial valued to 0
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
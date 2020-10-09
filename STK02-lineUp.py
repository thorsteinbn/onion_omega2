import onionGpio
import time

#specify sleep duration
sleepTime = 0.2

#Create and populate the list over GPIO pin numbers
gpioPins = [0, 1, 2, 3, 18, 19]

#init empty list that will hold our GPIO objects to control LEDs.
gpioObjects = []

#Print out the GPIOs that are being used
print('Using GPIOs:')
for gpioElement in gpioPins:
    print(gpioElement)

#populate the gpioObjects list
for gpioElement in gpioPins:
    #instantiate a GPIO object for this pin
    ledObj = onionGpio.OnionGpio(gpioElement)
    #Set to outputdirection with zero being default value
    ledObj.setOutputDirection(0)
    #add the GPIO object to the list
    gpioObjects.append(ledObj)

#create a variable to hold the value for the led (1 = on, 0 = off)
ledValue = 1

#infinite loop FTW
while True:
    #Set all of the GPIOs to ledValue
    for gpio in gpioObjects:
        gpio.setValue(ledValue)
        #pause after each led is changed
        time.sleep(sleepTime)

    #Flip the ledValue variable
    if ledValue == 1:
        ledValue = 0
    else:
        ledValue = 1
from gpiozero import LED # Importeer LED en LEDBoard uit gpiozero-bibliotheek
from time import sleep # importeer sleep

led_pins = [5, 6, 13, 19, 26, 16, 20, 21] #Herken alle pins
leds = [LED(pin) for pin in led_pins] #

while True: # blijf herhalen
    for i in range(len(leds)): # overloop de leds een voor een
        leds[i].on() # zet huidige led aan
        sleep(0.1) # wacht voor 0,1 seconden
        leds[i].off() # zet huidige led uit

    for i in range(len(leds) -1, -1, -1): # overloop de leds een voor een in de andere richting
        leds[i].on() # zet huidige led aan
        sleep(0.1) # wacht voor 0,1 seconden
        leds[i].off() # zet huidige led uit
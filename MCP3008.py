import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP3008
from gpiozero import LED
from adafruit_mcp3xxx.analog_in import AnalogIn 
#importeer alle libraries hierboven

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP3008.MCP3008(spi, cs)

channel1 = AnalogIn(mcp, MCP3008.P0)
channel2 = AnalogIn(mcp, MCP3008.P0)
channel3 = AnalogIn(mcp, MCP3008.P0)

led_rood = LED(17) #Led rood is op pin 17
led_groen = LED(27) #Led groen is op pin 27
led_blauw = LED(22) #Led is blauw is op pin 22
while True: # Zo lang dat het True is
    print("Raw ADC Value: ", channel1.value) #Print de tekst met de waarde in de terminal
    print("ADC Voltage: " + str(channel1.voltage) + "V") #Print de tekst met de waarde in de terminal
    if(channel1.value < 0.001): # Als de channel waarde kleiner is dan 0,001
        led_rood.value = 0 #Led waarde is 0
    else:
        led_rood.value = channel1.value #Led waarde is gelijk aan channel waarde
    time.sleep(0.5) # Wacht 0,5 seconden

    print("Raw ADC Value: ", channel2.value) #Print de tekst met de waarde in de terminal
    print("ADC Voltage: " + str(channel2.voltage) + "V") #Print de tekst met de waarde in de terminal
    if(channel2.value < 0.001): # Als de channel waarde kleiner is dan 0,001
        led_groen.value = 0 #Led waarde is 0
    else:
        led_groen.value = channel2.value #Led waarde is gelijk aan channel waarde
    time.sleep(0.5) # Wacht 0,5 seconden

    print("Raw ADC Value: ", channel3.value) #Print de tekst met de waarde in de terminal
    print("ADC Voltage: " + str(channel3.voltage) + "V") #Print de tekst met de waarde in de terminal
    if(channel3.value < 0.001): # Als de channel waarde kleiner is dan 0,001
        led_blauw.value = 0 #Led waarde is 0
    else:
        led_blauw.value = channel3.value #Led waarde is gelijk aan channel waarde
    time.sleep(0.5) # Wacht 0,5 seconden
import time
import board
import adafruit_dht
from w1thermsensor import W1ThermSensor
from gpiozero import LED
from time import sleep

LED_1 = LED(5)
LED_2 = LED(6)
LED_3 = LED(13)
LED_4 = LED(19)
LED_5 = LED(26)
LED_6 = LED(16)
LED_7 = LED(20)
LED_8 = LED(21)

dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
    
while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(1.0)
    
    temperature_in_celsius = sensor.get_temperature()
    print(temperature_in_celsius)
    sleep(1)
    if temperature_in_celsius >= 0:
        LED_1.on()
    else:
        LED_1.off()
    if temperature_in_celsius >= 5:
        LED_2.on()
    else:
        LED_2.off()
    if temperature_in_celsius >= 10:
        LED_3.on()
    else:
        LED_3.off()
    if temperature_in_celsius >= 15:
        LED_4.on()
    else:
        LED_4.off()
    if temperature_in_celsius >= 20:
        LED_5.on()
    else:
        LED_5.off()
    if temperature_in_celsius >= 25:
        LED_6.on()
    else:
        LED_6.off()
    if temperature_in_celsius >= 30:
        LED_7.on()
    else:
        LED_7.off()
    if temperature_in_celsius >= 35:
        LED_8.on()
    else:
        LED_8.off()
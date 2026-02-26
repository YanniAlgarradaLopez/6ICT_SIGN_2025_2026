import time
from gpiozero import Servo
import board
import adafruit_dht
from gpiozero.tools import sin_values
# import modules


servo = Servo(17) # servo op pin 17

dhtDevice = adafruit_dht.DHT11(board.D18) # DHT op pin 18

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0) # wacht 2 seconden
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(1.0) # wacht 1 seconden

    if temperature_c < 15: # als temperatuur onder de 15 graden
        servo_waarde = -1 # servo waarde is gelijk aan -1

    if temperature_c > 20: # als tmperatuur boven de 20 graden
        servo_waarde = 1 # servo waarde is gelijk aan 1

    else: # anders
        servo_waarde = ((temperature_c - 15) / 5) * 2 - 1 # servo waarde is gelijk aan dat
    
    servo.value = servo_waarde # servo.value is gelijk aan servo_waarde
    servo.source = sin_values() # servo.source is gelijk aan sin_values
    servo.source_delay = 0.1 # wacht 0.1 seconden

    time.sleep(1.0) # wacht 1 seconden
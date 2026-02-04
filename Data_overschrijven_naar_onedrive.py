import time
import board
import adafruit_dht
import subprocess


dhtDevice = adafruit_dht.DHT11(board.D18)

huidige_tijd = time.ctime()
print(huidige_tijd)

tijd_in_seconden = time.time()
print(tijd_in_seconden)

tijdzone = time.tzname
print(tijdzone)
    
while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        f
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    subprocess.run(["/bin/bash", "/home/rpi/overschrijven.sh"])
    time.sleep(2.0)
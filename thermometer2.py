import time
import board
import adafruit_dht
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
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

    f = open("mijndata.txt","w")
    f.write(temperature_in_celsius)
    f.close()

    f = open("mijndata.txt","a")
    f.write(temperature_in_celsius)
    f.close()

    f = open("mijndata.txt","r")
    inhoud = f.read() # variabele inhoud krijgt waarde van bestand
    print(inhoud) # print de inhoud
    f.close() # sluit het bestand
    time(1) # wacht 1 seconden
    
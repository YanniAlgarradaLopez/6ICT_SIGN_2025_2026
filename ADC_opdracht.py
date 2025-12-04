from signal import pause
import board
import datetime
import os
import csv
import adafruit_mcp3xxx.mcp3008 as MCP3008
import adafruit_dht
from gpiozero import MCP3008, LED
from adafruit_mcp3xxx.analog_in import AnalogIn 
#importeer alle libraries hierboven


dhtDevice = adafruit_dht.DHT11(board.D18)
pin = 4
datum = datetime.datetime.now()
bestandsnaam = f"/home/pi/dht_data_{datum.strftime('%Y-%m-%d')}.csv"



with open(bestandsnaam, 'a') as csvfile:
    writer = csv.writer(csvfile)
    if not os.path.exists(bestandsnaam):
        writer.writerow(['Datum', 'Tijd', 'Temperatuur (°C)'])
    huidige_tijd = datetime.datetime.now()
    (huidige_tijd, temperatuur) = adafruit_dht.read_retry(dhtDevice, pin)
    if temperatuur is None:
        writer.writerow([huidige_tijd.strftime('%Y-%m-%d'),
                         f"{temperatuur:.1f}"])
        print(f"Gegevens opgeslagen: {huidige_tijd}, Temperatuur: {temperatuur}°C")
    else:
        print("Fout bij uitlezen sensor, probeer het opnieuw")

while True:
    try:
        temperature_c = dhtDevice.temperature
        print(f"Temp: {temperature_c:.1f} C")
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
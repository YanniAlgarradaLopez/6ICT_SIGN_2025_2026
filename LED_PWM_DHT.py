import RPi.GPIO as GPIO
from gpiozero import PWMLED
from time import sleep
import adafruit_dht
import board

Rode_LED = PWMLED(17)
Groene_LED = PWMLED(27)
Blauwe_LED = PWMLED(22)
dhtDevice = adafruit_dht.DHT11(board.D18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(Rode_LED, GPIO.OUT)
GPIO.setup(Groene_LED, GPIO.OUT)
GPIO.setup(Blauwe_LED, GPIO.OUT)

rood = GPIO.PWM(Rode_LED, 100)
groen = GPIO.PWM(Groene_LED, 100)
blauw = GPIO.PWM(Blauwe_LED, 100)

rood.start(0)
groen.start(0)
blauw.start(0)

kleuren = [[0,0,225], [30, 144, 255], [0, 191, 255], [135, 206, 250], [0, 255, 255], [151, 255, 255], [0, 245, 255], [78, 238, 148], [0, 255, 0], [124, 252, 0], [255, 246, 143], [205, 205, 0], [238, 221, 130], [238, 173, 14], [205, 133, 0], [255, 127, 0], [238, 149, 114], [250, 128, 114], [205, 55, 0], [205, 38, 38], [255, 0, 0]]


while True:
        temperature_c = dhtDevice.temperature
        print("Temp: {:.1f} C ".format(temperature_c))
        temperatuur = max(0, min(40, temperatuur))
        kleur_index = int((temperatuur / 40) * (len(kleuren) - 1))
        rood, groen, blauw = kleuren[kleur_index]
        rood.ChangeDutyCycle((rood / 255) * 100)
        groen.ChangeDutyCycle((groen / 255) * 100)
        blauw.ChangeDutyCycle((blauw / 255) * 100)
        print("temperatuur: ", temperatuur, "°C", rood, groen ,blauw)

        sleep(2.0)
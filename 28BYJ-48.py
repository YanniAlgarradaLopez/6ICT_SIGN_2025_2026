import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib

GpioPins = [18, 23, 24, 25]

mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

afstand = int(input("Hoeveel mm moet het draaien? "))

rotaties = afstand/1

mymotortest.motor_run(GpioPins, .01, 510, False, False, "half", .05)

GPIO.cleanup()
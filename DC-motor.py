from gpiozero import Motor, MCP3008 # Importeer libraries

pot = MCP3008(0) # pot is MCP3008 op pin 0
motor = Motor(forward=17, backward=14) # motor is forward op pin 17 en backward op pin 14

while True:
    motor.forward(pot.value) # motor snelheid draait mee op waarde van potentiometer
import time as time, board, adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)

f=open("tempText.txt","w")
f.write("nr. Tijd Temp(°C) Vochtigheid(%) ")
f.close()
teller = 1

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        tijd = time.strftime("%H:%M:%S")
        f = open("tempText.txt","a")
        f.write(f"{teller} {tijd}  {temperature_c} {humidity} ")
        
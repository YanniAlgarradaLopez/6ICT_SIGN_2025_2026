import time as time

huidige_tijd = time.localtime()
print("Huidige tijd")

tijd_in_seconden = time.ctime()
print(tijd_in_seconden)

tijdzone = time.tzname
print(tijdzone)
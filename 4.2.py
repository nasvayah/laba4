import RPi.GPIO as gpio
import math
import time
gpio.setmode(gpio.BCM)
def binbin(x):
    return[int(element) for element in bin(x)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]
for lamp in dac:
    gpio.setup(lamp,gpio.OUT)
try:
    t = float(input('input period: '))
    k = int(input('input times: '))
    c = 0
    for i in range(k):
        while c < 255:
            n = binbin(c)
            gpio.output(dac, n)
            c += 1
            u = 3.3 / 256 * int(c)
            print(u)
            time.sleep(t/500)
        while c > 0:
            n = binbin(c)
            gpio.output(dac, n)
            c -= 1
            u = 3.3 / 256 * int(c)
            print(round(u, 3))
            time.sleep(t/500) 

finally:
    for lamp in dac:
        gpio.output(lamp,0)
    gpio.cleanup()
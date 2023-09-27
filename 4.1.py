import RPi.GPIO as g
import math
g.setmode(g.BCM)
def binbin(x):
    return[int(element) for element in bin(x)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]
for lamp in dac:
    g.setup(lamp,g.OUT)
try:
    while True:
        n = input('input integer between 0 and 255: ')
        if n == 'q':
            print('exit')
            break
        elif n.count('.') > 0:
            print('float, not integer')
            continue
        elif n.count('-') > 0:
            print('integer must be positive')
            continue
        elif not n.isdigit():
            print('string, not integer')
            continue
        elif int(n) > 255:
            print('integer must be < 256')
            continue
        n = int(n)
        binlist = binbin(n)
        
        g.output(dac, binlist)
        if binlist.count(1) == 0:
            u = 0
        else:
            u = round(3.3 *n / 256, 3)
        print('u = ', u, ' v')

finally:
    for lamp in dac:
        g.output(lamp,0)
    g.cleanup()

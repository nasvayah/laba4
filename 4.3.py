import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(11, gpio.OUT)

try:
    pers = int(input('input %'))
    p = gpio.PWM(11, 1000)
    p.start(pers)
    input('stop: ')
    p.stop()
finally:
    gpio.output(11, 0)
    gpio.cleanup()   
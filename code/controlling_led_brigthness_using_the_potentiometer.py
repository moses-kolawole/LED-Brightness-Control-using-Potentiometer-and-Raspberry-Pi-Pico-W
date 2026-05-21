from machine import Pin, ADC, PWM
from time import sleep

potpin = 28
mypot = ADC(potpin)

ledlight = PWM(Pin(6))
ledlight.freq(1000)

while True:
    potval = mypot.read_u16()

    ledlight.duty_u16(potval)

    sleep(0.01)
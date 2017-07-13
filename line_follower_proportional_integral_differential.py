#!/usr/bin/env python
__author__ = 'Piotr Bigos'

import ev3dev.ev3 as ev3
import time

cr = ev3.ColorSensor()
motor1 = ev3.LargeMotor('outA')
motor2 = ev3.LargeMotor('outB')
cr.mode = 'COL-REFLECT'

ev3.Sound.speak('White').wait()
time.sleep(2)
global white
white = cr.value()

ev3.Sound.speak('Black').wait()
time.sleep(2)
global black
black = cr.value()
r = (black + white) / 2

# print(black, white, r)

def check():
    cr.mode = 'COL-COLOR'
    return cr.value() == 5

x, kp, kd, ki, previous, suma, ep = 40, 1.2, 0, 0, 0, 0, 0

# main loop

while True:

    cr.mode = 'COL-REFLECT'
    now = cr.value()
    en = r - now
    suma += now

    if now < r:
        motor1.run_direct(duty_cycle_sp=x+(ki*suma+kp*en+kd*(en-ep)))
        motor2.run_direct(duty_cycle_sp=x-(ki*suma+kp*en+kd*(en-ep)))
    elif now > r:
        motor1.run_direct(duty_cycle_sp=x-(ki*suma+kp*en+kd*(en-ep)))
        motor2.run_direct(duty_cycle_sp=x+(ki*suma+kp*en+kd*(en-ep)))

    previous = now
    ep = en
    if check():
        break


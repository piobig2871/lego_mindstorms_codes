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

x = 30
k = 1.5

# main loop

while True:
    cr.mode = 'COL-REFLECT'
    now = cr.value()
    e = r - now
    # print now
    if now < r:
        motor1.run_direct(duty_cycle_sp=x+k*e)
        motor2.run_direct(duty_cycle_sp=x-k*e)
        if check():
            break

    elif now > r:
        motor1.run_direct(duty_cycle_sp=x-k*e)
        motor2.run_direct(duty_cycle_sp=x+k*e)
        if check():
            break

"""
Created by: Sophie
Created on: Sep 2023
This module is a Micro:bit MicroPython program that does math
"""

from microbit import *

display.clear()
sleep(1)

display.scroll("a rectangle has dimensions of 5cm and 3cm.")
display.scroll("the perimeter of a rectangle is " + str(2 * (5 + 3)) + "cm")
display.scroll("the area of a rectangle is " + str(5 * 3) + "cm^2")

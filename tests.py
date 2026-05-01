import config
import pygame

import override

def armada(canvas):
    override.drawPin(10, 10, 'RB', 0, canvas)
    override.drawPin(10, 20, 'RB', 180, canvas)
    override.drawPin(10, 30, 'RB', 90, canvas)
    override.drawPin(10, 40, 'RB', 270, canvas)

    override.drawPin(20, 10, 'RY', 0, canvas)
    override.drawPin(20, 20, 'RY', 180, canvas)
    override.drawPin(20, 30, 'RY', 90, canvas)
    override.drawPin(20, 40, 'RY', 270, canvas)

    override.drawPin(30, 10, 'BY', 0, canvas)
    override.drawPin(30, 20, 'BY', 180, canvas)
    override.drawPin(30, 30, 'BY', 90, canvas)
    override.drawPin(30, 40, 'BY', 270, canvas)

    override.drawPin(40, 10, 'YY', 0, canvas)
    override.drawPin(40, 20, 'YY', 180, canvas)
    override.drawPin(40, 30, 'YY', 90, canvas)
    override.drawPin(40, 40, 'YY', 270, canvas)

    override.drawPin(50, 10, 'R', 0, canvas)
    override.drawPin(50, 20, 'B', 0, canvas)
    override.drawPin(50, 30, 'Y', 0, canvas)

    override.drawCup(60, 10, 'OT', 0, canvas)
    override.drawCup(60, 20, 'OT', 180, canvas)
    override.drawCup(60, 30, 'OT', 90, canvas)
    override.drawCup(60, 40, 'OT', 270, canvas)

    override.drawCup(70, 10, 'TO', 0, canvas)
    override.drawCup(70, 20, 'TO', 180, canvas)
    override.drawCup(70, 30, 'TO', 90, canvas)
    override.drawCup(70, 40, 'TO', 270, canvas)

def offsetTest(canvas):
    override.drawPin(0, 0, 'RB', 0, canvas)

def cupDiameterTest(canvas):
    for i in range(8):
        override.drawPin((i * 3.16), 0, 'B', 0, canvas)
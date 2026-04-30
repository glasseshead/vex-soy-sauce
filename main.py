import pygame, sys, os
from pygame.locals import *
import config

import render
import override

# initialize
pygame.init()

# set clock

# set up canvas
canvas = pygame.display.set_mode((config.canvasX, config.canvasY))
pygame.display.set_caption('VEX Soy Sauce')

while True:
    # control loop
    for event in pygame.event.get():
        # exit control
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # render field
    render.renderField(canvas)
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

    override.drawCup(70, 10, 'TO', 0, canvas)
    override.drawCup(70, 20, 'TO', 180, canvas)

    # update ticks
    pygame.display.update()
    config.fpsClock.tick(config.fps)
import pygame, sys, os
from pygame.locals import *
import config

import render

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

    # update ticks
    pygame.display.update()
    config.fpsClock.tick(config.fps)
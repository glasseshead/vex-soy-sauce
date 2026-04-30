import pygame

import config
import override

def renderGame(game, canvas):
    return

def renderTiles(canvas):
    # render field perimeter
    pygame.draw.rect(canvas, (200, 200, 200), (140, 60, 520, 520))

    # may not be the best way to do this but hey i need to do something
    for i in range(6):
        for j in range(6):
            # checkerboard
            if ((j % 2 == 0 and i % 2 != 0) or
                (j % 2 != 0 and i % 2 == 0)): 
                pygame.draw.rect(canvas, (95, 95, 95), (160 + 80 * j, 80 + 80 * i, 80, 80))
            else:  
                pygame.draw.rect(canvas, (100, 100, 100), (160 + 80 * j, 80 + 80 * i, 80, 80))

def renderField(canvas):
    # background
    canvas.fill(config.canvasBGColour)

    # render tiles, game
    renderTiles(canvas)
    renderGame('override hs', canvas)
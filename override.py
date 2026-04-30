import pygame, math

import config

def renderPin(x, y, type, orientation, rotation, canvas):
    # types: YY, BY, RY, BR, R, B, Y
    # orientation: side, up
    # rotation: clockwise 0-360
    img = pygame.image.load(f'assets/pin_{type}_{orientation}.png').convert_alpha()

    if orientation == 'side':
        size = (int(3.02 * config.tickPerIn), int(6.50 * config.tickPerIn))
    else:  # 'up'
        size = (int(3.02 * config.tickPerIn), int(3.02 * config.tickPerIn))

    img = pygame.transform.smoothscale(img, size)
    img = pygame.transform.rotate(img, rotation)

    canvas.blit(img, (x, y))

def renderCup(x, y, type, orientation, rotation, canvas):
    # types: transparent, opaque
    # orientation: side, up
    # rotation: clockwise 0-360
    img = pygame.image.load(f'assets/cup_{type}_{orientation}.png').convert_alpha()

    if orientation == 'side':
        size = (int(3.16 * config.tickPerIn), int(6.48 * config.tickPerIn))
    else:  # 'up'
        size = (int(3.16 * config.tickPerIn), int(3.16 * config.tickPerIn))

    img = pygame.transform.smoothscale(img, size)
    img = pygame.transform.rotate(img, rotation)

    canvas.blit(img, (x, y))
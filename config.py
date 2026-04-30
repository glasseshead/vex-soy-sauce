import pygame

# initialize fps values
fps = 60
fpsClock = pygame.time.Clock()

# initialize canvas values
canvasX, canvasY = 800, 640
canvasBGColour = (66, 77, 79)

# inches per tick conversion
# i named it this to conform with ftc
inPerTick = 24 / 80
tickPerIn = 80 / 24

# colours
BLUE = (36, 143, 203)
RED = (178, 30, 46)
YELLOW = (234, 230, 34)
BLACK = (71, 73, 82)
TRANSPARENT = (233, 233, 236)
bottomBrightnessDisparity = -20
topBrightnessDisparity = 20
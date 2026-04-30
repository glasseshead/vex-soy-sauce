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
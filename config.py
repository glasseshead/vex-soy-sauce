import pygame

# initialize fps values
fps = 60
fpsClock = pygame.time.Clock()

# initialize canvas values
canvasX, canvasY = 800, 640
canvasBGColour = (66, 77, 79)

# pixels per inch conversion
# this is actually supposed to be ticks per inch
# i named it this to conform with ftc
tickPerIn = 80 / 24
import pygame, math

import config

'''
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
'''

def drawPin(x, y, type, rotation, canvas):
    x, y = x * config.tickPerIn + 160, y * config.tickPerIn + 80

    # types: YY, BY, RY, BR, R, B, Y
    # rotation: clockwise 0-360

    if type == 'RB':
        half_w = (3.02 * config.tickPerIn) / 2
        half_h = (6.50 * config.tickPerIn) / 2
        inner_w = (1.40 * config.tickPerIn) / 2

        if rotation == 0:
            # vertical orientation
            pygame.draw.polygon(canvas, config.RED, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])
            pygame.draw.polygon(canvas, config.BLUE, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])

        elif rotation == 180:
            # vertical orientation
            pygame.draw.polygon(canvas, config.RED, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])
            pygame.draw.polygon(canvas, config.BLUE, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])

        elif rotation == 90:
            pygame.draw.polygon(canvas, config.RED, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.BLUE, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])

        elif rotation == 270:
            pygame.draw.polygon(canvas, config.RED, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.BLUE, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])

    if type == 'RY':
        half_w = (3.02 * config.tickPerIn) / 2
        half_h = (6.50 * config.tickPerIn) / 2
        inner_w = (1.40 * config.tickPerIn) / 2

        if rotation == 0:
            # vertical orientation
            pygame.draw.polygon(canvas, config.RED, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])

        elif rotation == 180:
            # vertical orientation
            pygame.draw.polygon(canvas, config.RED, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])

        elif rotation == 90:
            pygame.draw.polygon(canvas, config.RED, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])

        elif rotation == 270:
            pygame.draw.polygon(canvas, config.RED, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])

    if type == 'BY':
        half_w = (3.02 * config.tickPerIn) / 2
        half_h = (6.50 * config.tickPerIn) / 2
        inner_w = (1.40 * config.tickPerIn) / 2

        if rotation == 0:
            # vertical orientation
            pygame.draw.polygon(canvas, config.BLUE, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])

        elif rotation == 180:
            # vertical orientation
            pygame.draw.polygon(canvas, config.BLUE, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])

        elif rotation == 90:
            pygame.draw.polygon(canvas, config.BLUE, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])

        elif rotation == 270:
            pygame.draw.polygon(canvas, config.BLUE, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])

    if type == 'YY':
        half_w = (3.02 * config.tickPerIn) / 2
        half_h = (6.50 * config.tickPerIn) / 2
        inner_w = (1.40 * config.tickPerIn) / 2

        if rotation == 0:
            # vertical orientation
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])

        elif rotation == 180:
            # vertical orientation
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])

        elif rotation == 90:
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])

        elif rotation == 270:
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x - half_h, y + inner_w),
                (x - half_h, y - inner_w)
            ])
            pygame.draw.polygon(canvas, config.YELLOW, [
                (x, y - half_w),
                (x, y + half_w),
                (x + half_h, y + inner_w),
                (x + half_h, y - inner_w)
            ])

    if type == 'R':
        pygame.draw.circle(canvas, (178 + config.bottomBrightnessDisparity, 30 + config.bottomBrightnessDisparity, 46 + config.bottomBrightnessDisparity), (x, y), int(3.16 * config.tickPerIn) // 2)
        pygame.draw.circle(canvas, (178, 30, 46), (x, y), int(2.35 * config.tickPerIn) // 2)
        pygame.draw.circle(canvas, (178 + config.topBrightnessDisparity, 30 + config.topBrightnessDisparity, 46 + config.topBrightnessDisparity), (x, y), int(1.4 * config.tickPerIn) // 2)

    if type == 'B':
        pygame.draw.circle(canvas, (36 + config.bottomBrightnessDisparity, 143 + config.bottomBrightnessDisparity, 203 + config.bottomBrightnessDisparity), (x, y), int(3.16 * config.tickPerIn) // 2)
        pygame.draw.circle(canvas, (36, 143, 203), (x, y), int(2.35 * config.tickPerIn) // 2)
        pygame.draw.circle(canvas, (36 + config.topBrightnessDisparity, 143 + config.topBrightnessDisparity, 203 + config.topBrightnessDisparity), (x, y), int(1.4 * config.tickPerIn) // 2)

    if type == 'Y':
        pygame.draw.circle(canvas, (234 + config.bottomBrightnessDisparity, 230 + config.bottomBrightnessDisparity, 34 + config.bottomBrightnessDisparity), (x, y), int(3.16 * config.tickPerIn) // 2)
        pygame.draw.circle(canvas, (234, 230, 34), (x, y), int(2.35 * config.tickPerIn) // 2)
        pygame.draw.circle(canvas, (234 + config.topBrightnessDisparity, 230 + config.topBrightnessDisparity, 34 + config.topBrightnessDisparity), (x, y), int(1.4 * config.tickPerIn) // 2)

def drawCup(x, y, type, rotation, canvas):
    x, y = x * config.tickPerIn + 160, y * config.tickPerIn + 80

    # types: T, O
    # rotation: clockwise 0-360

    if type == 'OT':
        half_w = (2.32 * config.tickPerIn) / 2
        half_h = (6.48 * config.tickPerIn) / 2
        inner_w = (3.16 * config.tickPerIn) / 2

        if rotation == 0:
            pygame.draw.polygon(canvas, config.BLACK, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])
            pygame.draw.polygon(canvas, config.TRANSPARENT, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])

        elif rotation == 180:
            pygame.draw.polygon(canvas, config.BLACK, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y + half_h),
                (x - inner_w, y + half_h)
            ])
            pygame.draw.polygon(canvas, config.TRANSPARENT, [
                (x - half_w, y),
                (x + half_w, y),
                (x + inner_w, y - half_h),
                (x - inner_w, y - half_h)
            ])
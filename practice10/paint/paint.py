import pygame
import sys
import math

pygame.init()

#SCREEN
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#VARIABLES
mode = "blue"  
drawing = True
points = []

shape_start = None  

radius = 5


#DRAW FUNCTION
def drawLineBetween(screen, index, start, end, width, color_mode):

    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:
        color = WHITE

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations if iterations != 0 else 0
        x = int(start[0] * (1 - progress) + end[0] * progress)
        y = int(start[1] * (1 - progress) + end[1] * progress)
        pygame.draw.circle(screen, color, (x, y), width)


#MAIN LOOP
while True:

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():

        # EXIT
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #KEYBOARD
        if event.type == pygame.KEYDOWN:

            # colors
            if event.key == pygame.K_r:
                mode = "red"
            elif event.key == pygame.K_g:
                mode = "green"
            elif event.key == pygame.K_b:
                mode = "blue"

            # tools
            elif event.key == pygame.K_1:
                mode = "brush"
            elif event.key == pygame.K_2:
                mode = "rect"
            elif event.key == pygame.K_3:
                mode = "circle"
            elif event.key == pygame.K_4:
                mode = "eraser"

        #MOUSE DOWN
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mode == "rect" or mode == "circle":
                shape_start = event.pos

            if event.button == 1:
                if mode == "eraser":
                    mode = "eraser"

        #MOUSE UP
        if event.type == pygame.MOUSEBUTTONUP:

            if mode == "rect" and shape_start:
                end = event.pos
                pygame.draw.rect(screen, WHITE,
                                 pygame.Rect(shape_start[0],
                                             shape_start[1],
                                             end[0] - shape_start[0],
                                             end[1] - shape_start[1]))
                shape_start = None

            if mode == "circle" and shape_start:
                end = event.pos
                radius_circle = int(math.sqrt(
                    (end[0] - shape_start[0]) ** 2 +
                    (end[1] - shape_start[1]) ** 2
                ))

                pygame.draw.circle(screen, WHITE, shape_start, radius_circle)
                shape_start = None

        #DRAW FREE HAND
        if event.type == pygame.MOUSEMOTION and mode in ["brush", "red", "green", "blue", "eraser"]:
            points.append(event.pos)
            points = points[-256:]

    #BACKGROUND
    screen.fill(BLACK)

    #DRAW LINES
    i = 0
    while i < len(points) - 1:
        drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        i += 1

    #UPDATE
    pygame.display.flip()
    clock.tick(60)
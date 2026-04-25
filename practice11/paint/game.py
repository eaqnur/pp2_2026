import pygame
import sys
import math

pygame.init()

#SCREEN
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Paint App")

clock=pygame.time.Clock()

#COLORS
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#CANVAS
canvas=pygame.Surface(screen.get_size())
canvas.fill(BLACK)

#VARIABLES
mode="brush"
current_color=WHITE
points=[]
shape_start=None
radius=5


#Draw smooth line for brush and eraser
def drawLineBetween(surface,start,end,width,color):
    dx=start[0]-end[0]
    dy=start[1]-end[1]
    iterations=max(abs(dx),abs(dy))

    for i in range(iterations):
        progress=i/iterations if iterations!=0 else 0
        x=int(start[0]*(1-progress)+end[0] * progress)
        y=int(start[1]*(1-progress)+end[1] * progress)
        pygame.draw.circle(surface,color,(x,y),width)


#MAIN LOOP
while True:
    for event in pygame.event.get():
        #Exit program
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Keyboard controls
        if event.type==pygame.KEYDOWN:

            #Choose color
            if event.key==pygame.K_r:
                current_color=RED
            elif event.key==pygame.K_g:
                current_color=GREEN
            elif event.key==pygame.K_b:
                current_color=BLUE
            elif event.key==pygame.K_w:
                current_color=WHITE

            #Choose tool
            elif event.key==pygame.K_1:
                mode="brush"
            elif event.key==pygame.K_2:
                mode="rect"
            elif event.key==pygame.K_3:
                mode="circle"
            elif event.key==pygame.K_4:
                mode="eraser"
            elif event.key==pygame.K_5:
                mode="square"
            elif event.key==pygame.K_6:
                mode="right_triangle"
            elif event.key==pygame.K_7:
                mode="equilateral_triangle"
            elif event.key==pygame.K_8:
                mode="rhombus"

        #Mouse button down
        if event.type==pygame.MOUSEBUTTONDOWN:
            if mode in [
                "rect",
                "circle",
                "square",
                "right_triangle",
                "equilateral_triangle",
                "rhombus"
            ]:
                shape_start=event.pos

            points=[event.pos]

        #Mouse movement for brush and eraser
        if event.type==pygame.MOUSEMOTION:
            if event.buttons[0]:
                if mode=="brush":
                    points.append(event.pos)
                    if len(points)>1:
                        drawLineBetween(canvas,points[-2],points[-1],radius,current_color)

                elif mode=="eraser":
                    points.append(event.pos)
                    if len(points)>1:
                        drawLineBetween(canvas,points[-2],points[-1],radius,BLACK)

        #Mouse button up
        if event.type==pygame.MOUSEBUTTONUP:
            end=event.pos

            #Draw rectangle
            if mode=="rect" and shape_start:
                rect=pygame.Rect(
                    shape_start[0],
                    shape_start[1],
                    end[0]-shape_start[0],
                    end[1]-shape_start[1]
                )
                pygame.draw.rect(canvas,current_color,rect)
                shape_start=None

            #Draw circle
            elif mode=="circle" and shape_start:
                radius_circle=int(math.sqrt(
                    (end[0]-shape_start[0])**2+
                    (end[1]-shape_start[1])**2
                ))
                pygame.draw.circle(canvas,current_color,shape_start,radius_circle)
                shape_start=None

            #Draw square
            elif mode=="square" and shape_start:
                size=min(
                    abs(end[0]-shape_start[0]),
                    abs(end[1]-shape_start[1])
                )

                x=shape_start[0]
                y=shape_start[1]

                if end[0]<shape_start[0]:
                    x=shape_start[0]-size
                if end[1]<shape_start[1]:
                    y=shape_start[1]-size

                pygame.draw.rect(canvas,current_color,pygame.Rect(x,y,size,size))
                shape_start=None

            #Draw right triangle
            elif mode=="right_triangle" and shape_start:
                points_triangle=[
                    shape_start,
                    (shape_start[0],end[1]),
                    end
                ]
                pygame.draw.polygon(canvas,current_color,points_triangle)
                shape_start=None

            #Draw equilateral triangle
            elif mode=="equilateral_triangle" and shape_start:
                side=end[0]-shape_start[0]
                height=int(abs(side)*math.sqrt(3)/2)

                if end[1]<shape_start[1]:
                    height=-height

                points_triangle=[
                    shape_start,
                    (shape_start[0]+side,shape_start[1]),
                    (shape_start[0]+side//2,shape_start[1]+height)
                ]

                pygame.draw.polygon(canvas,current_color,points_triangle)
                shape_start=None

            #Draw rhombus
            elif mode=="rhombus" and shape_start:
                center_x=(shape_start[0]+end[0])//2
                center_y=(shape_start[1]+end[1])//2

                points_rhombus=[
                    (center_x,shape_start[1]),
                    (end[0],center_y),
                    (center_x,end[1]),
                    (shape_start[0],center_y)
                ]

                pygame.draw.polygon(canvas,current_color,points_rhombus)
                shape_start=None

            points=[]

    #Draw canvas on screen
    screen.blit(canvas,(0,0))

    pygame.display.flip()
    clock.tick(60)
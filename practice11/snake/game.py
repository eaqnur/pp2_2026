import pygame
import sys
import random
import time

pygame.init()

#SCREEN
SCREEN_WIDTH=600
SCREEN_HEIGHT=400

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock=pygame.time.Clock()

#COLORS
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)
ORANGE=(255,165,0)
WHITE=(255,255,255)

#SNAKE
snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]]

direction="RIGHT"
change_to=direction

#GAME DATA
score=0
level=1

#Food timer
FOOD_LIFETIME=5000
food_spawn_time=pygame.time.get_ticks()

#Game start time
start_time=pygame.time.get_ticks()

font=pygame.font.SysFont("Arial",25)
big_font=pygame.font.SysFont("Arial",50)


#FUNCTIONS
def spawn_food():
    #Generate random food position
    pos=[
        random.randrange(0,SCREEN_WIDTH//10)*10,
        random.randrange(0,SCREEN_HEIGHT//10)*10
    ]

    #Food must not spawn on snake body
    while pos in snake_body:
        pos=[
            random.randrange(0,SCREEN_WIDTH//10)*10,
            random.randrange(0,SCREEN_HEIGHT//10)*10
        ]

    #Generate random food weight
    weight=random.choice([1,2,3])

    return pos,weight


def get_food_color(weight):
    #Different food weights have different colors
    if weight==1:
        return RED
    elif weight==2:
        return YELLOW
    else:
        return ORANGE


def game_over_screen():
    #Calculate final game time
    final_time=(pygame.time.get_ticks()-start_time)//1000

    screen.fill(BLACK)

    game_over_text=big_font.render("GAME OVER",True,RED)
    score_text=font.render(f"Score:{score}",True,WHITE)
    level_text=font.render(f"Level:{level}",True,WHITE)
    time_text=font.render(f"Time:{final_time}seconds",True,WHITE)

    screen.blit(game_over_text,(150,100))
    screen.blit(score_text,(230,180))
    screen.blit(level_text,(230,220))
    screen.blit(time_text,(200,260))

    pygame.display.update()
    time.sleep(3)

    pygame.quit()
    sys.exit()


#Create first food
food_pos,food_weight=spawn_food()


#GAME LOOP
while True:
    #EVENTS
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                change_to="UP"
            if event.key==pygame.K_DOWN:
                change_to="DOWN"
            if event.key==pygame.K_LEFT:
                change_to="LEFT"
            if event.key==pygame.K_RIGHT:
                change_to="RIGHT"

    #Prevent reverse direction
    if change_to=="UP" and direction!="DOWN":
        direction="UP"
    if change_to=="DOWN" and direction!="UP":
        direction="DOWN"
    if change_to=="LEFT" and direction!="RIGHT":
        direction="LEFT"
    if change_to=="RIGHT" and direction!="LEFT":
        direction="RIGHT"
    #MOVE SNAKE
    if direction=="UP":
        snake_pos[1]-=10
    if direction=="DOWN":
        snake_pos[1]+=10
    if direction=="LEFT":
        snake_pos[0]-=10
    if direction=="RIGHT":
        snake_pos[0]+=10

    #Add new head
    snake_body.insert(0,list(snake_pos))

    #EAT FOOD
    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        #Add points according to food weight
        score+=food_weight

        #Generate new food and restart timer
        food_pos,food_weight=spawn_food()
        food_spawn_time=pygame.time.get_ticks()
    else:
        snake_body.pop()

    #Food disappears after some time
    current_time=pygame.time.get_ticks()

    if current_time-food_spawn_time>FOOD_LIFETIME:
        food_pos,food_weight=spawn_food()
        food_spawn_time=pygame.time.get_ticks()

    #LEVEL SYSTEM
    level=score//3+1

    #DRAW
    screen.fill(BLACK)

    #Draw snake
    for block in snake_body:
        pygame.draw.rect(screen,GREEN,pygame.Rect(block[0],block[1],10,10))

    #Draw food with color depending on weight
    food_color=get_food_color(food_weight)
    pygame.draw.rect(screen,food_color,pygame.Rect(food_pos[0],food_pos[1],10,10))

    #Draw score, level, food weight and time
    game_time=(pygame.time.get_ticks()-start_time)//1000
    time_left=(FOOD_LIFETIME-(current_time-food_spawn_time))//1000

    score_text=font.render(f"Score:{score}",True,WHITE)
    level_text=font.render(f"Level:{level}",True,WHITE)
    food_text=font.render(f"Food weight:{food_weight}",True,WHITE)
    timer_text=font.render(f"Food timer:{time_left}s",True,WHITE)
    time_text=font.render(f"Time:{game_time}s",True,WHITE)

    screen.blit(score_text,(10,10))
    screen.blit(level_text,(10,40))
    screen.blit(food_text,(10,70))
    screen.blit(timer_text,(10,100))
    screen.blit(time_text,(10,130))

    #WALL COLLISION
    if snake_pos[0]<0 or snake_pos[0]>=SCREEN_WIDTH:
        game_over_screen()

    if snake_pos[1]<0 or snake_pos[1]>=SCREEN_HEIGHT:
        game_over_screen()

    #SELF COLLISION
    for block in snake_body[1:]:
        if snake_pos==block:
            game_over_screen()

    #SPEED INCREASE
    clock.tick(10+level*2)

    pygame.display.update()
import pygame
import sys
import random

pygame.init()
#SCREEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

#COLORS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#SNAKE
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

direction = "RIGHT"
change_to = direction

#FOOD
food_pos = [
    random.randrange(0, SCREEN_WIDTH // 10) * 10,
    random.randrange(0, SCREEN_HEIGHT // 10) * 10
]

#GAME DATA
score = 0
level = 1

font = pygame.font.SysFont("Arial", 25)

#FUNCTIONS
def spawn_food():
    pos = [
        random.randrange(0, SCREEN_WIDTH // 10) * 10,
        random.randrange(0, SCREEN_HEIGHT // 10) * 10
    ]

    # food must NOT spawn on snake
    while pos in snake_body:
        pos = [
            random.randrange(0, SCREEN_WIDTH // 10) * 10,
            random.randrange(0, SCREEN_HEIGHT // 10) * 10
        ]

    return pos


#GAME LOOP
while True:

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # prevent reverse direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    #MOVE SNAKE
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # add new head
    snake_body.insert(0, list(snake_pos))

    #EAT FOOD
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_pos = spawn_food()
    else:
        snake_body.pop()

    #LEVEL SYSTEM
    level = score // 3 + 1

    #DRAW
    screen.fill(BLACK)

    # draw snake
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))

    # draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # draw score + level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    #WALL COLLISION
    if snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH:
        pygame.quit()
        sys.exit()

    if snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT:
        pygame.quit()
        sys.exit()

    #SELF COLLISION
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    #SPEED INCREASE
    clock.tick(10 + level * 2)

    pygame.display.update()
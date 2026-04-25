import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#Frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

#Colors
BLACK=(0,0,0)
RED=(255,0,0)

#Screen size
SCREEN_WIDTH=400
SCREEN_HEIGHT=600

#Game variables
SPEED=5
SCORE=0
COIN_SCORE=0

#Enemy speed increases after every N coins
N=5
NEXT_SPEED_UP=N

#Background movement variables
bg_y1=0
bg_y2=-SCREEN_HEIGHT

#Game start time
start_time=pygame.time.get_ticks()

#Fonts
font=pygame.font.SysFont("Verdana",60)
font_small=pygame.font.SysFont("Verdana",20)
font_medium=pygame.font.SysFont("Verdana",25)

#Game over text
game_over=font.render("Game Over",True,BLACK)

#Load and scale background
background=pygame.image.load("AnimatedStreet.png")
background=pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))

#Create display window
DISPLAYSURF=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Load enemy image
        self.image=pygame.image.load("Enemy.png")
        self.rect=self.image.get_rect()

        #Set random starting position
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        global SCORE

        #Move enemy downward
        self.rect.move_ip(0,SPEED)

        #Reset enemy when it leaves the screen
        if self.rect.top>SCREEN_HEIGHT:
            SCORE+=1
            self.rect.top=0
            self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Load player image
        self.image=pygame.image.load("Player.png")
        self.rect=self.image.get_rect()

        #Initial player position
        self.rect.center=(160, 520)

    def move(self):
        pressed_keys=pygame.key.get_pressed()

        #Move left
        if pressed_keys[K_LEFT] and self.rect.left>0:
            self.rect.move_ip(-5,0)

        #Move right
        if pressed_keys[K_RIGHT] and self.rect.right<SCREEN_WIDTH:
            self.rect.move_ip(5,0)

        #Move forward (up)
        if pressed_keys[K_UP] and self.rect.top>0:
            self.rect.move_ip(0,-5)

        #Move backward (down)
        if pressed_keys[K_DOWN] and self.rect.bottom<SCREEN_HEIGHT:
            self.rect.move_ip(0,5)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Load original coin image
        self.original_image=pygame.image.load("coin.png")
        self.generate_coin()

    def generate_coin(self):
        #Random coin weight (value)
        self.weight=random.choice([1, 2, 3])

        #Different size depending on weight
        if self.weight==1:
            size=30
        elif self.weight==2:
            size=40
        else:
            size=50

        #Resize coin image
        self.image=pygame.transform.scale(self.original_image,(size,size))
        self.rect=self.image.get_rect()

        #Set random position on the road
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        #Move coin downward
        self.rect.move_ip(0,SPEED)

        #Regenerate coin when it leaves screen
        if self.rect.top>SCREEN_HEIGHT:
            self.generate_coin()


#Create game objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Groups for enemies and coins
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

#Group containing all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


while True:

    #Handle events
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    #Move background to simulate road motion
    bg_y1+=SPEED
    bg_y2+=SPEED

    if bg_y1>=SCREEN_HEIGHT:
        bg_y1=-SCREEN_HEIGHT

    if bg_y2>=SCREEN_HEIGHT:
        bg_y2=-SCREEN_HEIGHT

    #Draw moving background
    DISPLAYSURF.blit(background,(0,bg_y1))
    DISPLAYSURF.blit(background,(0,bg_y2))

    #Calculate game time in seconds
    current_time=pygame.time.get_ticks()
    game_time=(current_time-start_time)//1000

    #Render score, coins, speed and time
    score_text=font_small.render(f"Score:{SCORE}",True,BLACK)
    coin_text=font_small.render(f"Coins:{COIN_SCORE}",True,BLACK)
    speed_text=font_small.render(f"Speed:{SPEED}",True,BLACK)
    time_text=font_small.render(f"Time:{game_time}s",True,BLACK)

    DISPLAYSURF.blit(score_text,(10,10))
    DISPLAYSURF.blit(coin_text,(10,30))
    DISPLAYSURF.blit(speed_text,(10,50))
    DISPLAYSURF.blit(time_text,(10,70))

    #Draw and update all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image,entity.rect)
        entity.move()

    #Check collision with coin
    if pygame.sprite.spritecollideany(P1,coins):
        for coin in coins:
            COIN_SCORE+=coin.weight
            coin.generate_coin()

        #Increase speed after collecting N coins
        if COIN_SCORE>=NEXT_SPEED_UP:
            SPEED+=1
            NEXT_SPEED_UP+=N

    #Check collision with enemy
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)

        #Display final results
        final_score=font_medium.render(f"Score:{SCORE}",True,BLACK)
        final_coins = font_medium.render(f"Coins:{COIN_SCORE}",True,BLACK)
        final_time = font_medium.render(f"Time:{game_time} seconds",True,BLACK)

        DISPLAYSURF.blit(game_over,(30,180))
        DISPLAYSURF.blit(final_score,(120,280))
        DISPLAYSURF.blit(final_coins,(120,320))
        DISPLAYSURF.blit(final_time,(90,360))

        pygame.display.update()
        time.sleep(3)

        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
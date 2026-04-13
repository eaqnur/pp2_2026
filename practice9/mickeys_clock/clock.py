import pygame
import datetime
import math


class MickeyClock:
    def __init__(self):
        self.background=pygame.image.load("images/mickeyclock.jpeg")
        self.background=pygame.transform.scale(self.background, (800, 800))
        self.center=(400,400)
        self.minute_length=220
        self.second_length=180

    def draw_hand(self, screen, angle, length, width):
        rad=math.radians(angle - 90)

        end_x=self.center[0]+length*math.cos(rad)
        end_y=self.center[1]+length*math.sin(rad)
        pygame.draw.line(
            screen,
            (0,0,0),
            self.center,
            (end_x,end_y),
            width
        )

    def draw(self, screen):
        now=datetime.datetime.now()
        minutes=now.minute
        seconds=now.second
        minute_angle=minutes*6
        second_angle=seconds*6
        screen.blit(self.background,(0, 0))
        # minute hand
        self.draw_hand(screen, minute_angle, self.minute_length, 6)
        # second hand
        self.draw_hand(screen, second_angle, self.second_length, 4)

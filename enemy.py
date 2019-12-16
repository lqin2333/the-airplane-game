import random
import pygame
from game_sprites import *

class Enemy(GameSprite):

    def __init__(self):
        super().__init__('./images/enemy.png')
        # random speed
        self.speed = random.randint(1, 3)
        # random position
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
 


    
import pygame
from game_sprites import *

class Hero(GameSprite):

    def __init__(self):
        super().__init__('./images/enemy.png')
        self.rect.y = 0
        self.rect.x = 

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
 


    
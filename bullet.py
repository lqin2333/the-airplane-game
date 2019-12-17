import pygame
from game_sprites import *

class Bullet(GameSprite):

    def __init__(self):
        super().__init__('./images/bullet.png', -2)
        

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
 
    def fire(self):
        print('fire.....')

    
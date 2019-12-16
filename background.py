import pygame
from game_sprites import *

class Background(GameSprite):

    def __init__(self, is_alt = False, speed = 1):
        super().__init__('./images/background.jpg')
        
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


    
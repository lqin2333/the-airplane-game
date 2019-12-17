import pygame
from game_sprites import *
from bullet import *


class Hero(GameSprite):

    def __init__(self):
        super().__init__('./images/plane.png')
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.rect.centerx = SCREEN_RECT.centerx

        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
 
    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y
        bullet.rect.centerx = self.rect.centerx
        self.bullet_group.add(bullet)

    
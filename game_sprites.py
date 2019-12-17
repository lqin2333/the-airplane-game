import pygame

# config
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
SCREEN_SPEED = 1
FRAME_PER_SEC = 60
HERO_MOVING_SENSITIVITY = 3
HERO_FIRE_EVENT = pygame.USEREVENT + 1

# define event constant
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    
    def __init__(self, image_name, speed = SCREEN_SPEED):
        super().__init__()
        self.image = pygame.image.load(image_name)
        # position
        self.rect = self.image.get_rect()
        self.speed = speed
         
    def update(self):
        self.rect.y += self.speed

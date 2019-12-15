import pygame
from game_sprites import *

# game init
pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load('./images/background.jpg')
screen.blit(background, (0, 0))

hero = pygame.image.load('./images/plane.png')

screen.blit(hero, (180, 480))

hero_rect = pygame.Rect(180, 400, 120, 120)

# Enemies
enemy1 = GameSprite('./images/enemy.png', 1)
enemy2 = GameSprite('./images/enemy.png', 2)
enemy_group = pygame.sprite.Group(enemy1, enemy2)

clock = pygame.time.Clock()


# game loop
while True:
    clock.tick(60)
    hero_rect.y -= 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # re-draw bg everytime
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    # add enemy to the game screen
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

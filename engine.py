import pygame

# game init
pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load('./images/background.jpg')
screen.blit(background, (0, 0))

hero = pygame.image.load('./images/plane.png')

screen.blit(hero, (180, 480))

hero_rect = pygame.Rect(180, 400, 120, 120)

clock = pygame.time.Clock()


# game loop
while True:
    clock.tick(60)
    hero_rect.y -= 1
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

pygame.quit()

import pygame
from game_sprites import *
from background import *
from enemy import *
from hero import *

class PlaneGame(object):

    def __init__(self):
        print("init")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        # @event_id = CREATE_ENEMY_EVENT
        # @every 1000 ms
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    # private methods ===========
    def __create_sprites(self):
        # background
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('emeny created')
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = HERO_MOVING_SENSITIVITY
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -HERO_MOVING_SENSITIVITY
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemis = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemis) > 0:
            self.hero.kill()
            self.__game_over()


    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    # private methods end =======

    def start_game(self):
        print("start")
        while True:
            self.clock.tick(FRAME_PER_SEC) # frame
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    @staticmethod
    def __game_over():
        print("game over")
        pygame.quit()
        exit()
    
if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()

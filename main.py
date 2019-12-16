import pygame
from game_sprites import *
from background import *
from enemy import *

class PlaneGame(object):

    def __init__(self):
        print("init")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        # @event_id = CREATE_ENEMY_EVENT
        # @every 1000 ms
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    # private methods ===========
    def __create_sprites(self):
        # background
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('emeny created')
                enemy = Enemy()
                self.enemy_group.add(enemy)

    def __check_collide(self):
        pass
    
    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

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

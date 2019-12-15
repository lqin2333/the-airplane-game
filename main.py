import pygame
from game_sprites import *

class PlaneGame(object):

    def __init__(self):
        print("init")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    # private methods ===========
    def __create_sprites(self):
        pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass
    
    def __update_sprites(self):
        pass

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

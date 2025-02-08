import sys
import pygame
import utils
import config
from config import width_prct


class Window:
    def __init__(self):
        pygame.init()

        self.width = utils.WIDTH
        self.height = utils.HEIGHT

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.top_left = pygame.Surface([config.width_prct(self.width, 50), config.height_prct(self.height, 50)])
        self.top_right = pygame.Surface([config.width_prct(self.width, 50), config.height_prct(self.height, 50)])
        self.bottom_left = pygame.Surface([config.width_prct(self.width, 50), config.height_prct(self.height, 50)])
        self.bottom_right = pygame.Surface([config.width_prct(self.width, 50), config.height_prct(self.height, 50)])

        self.top_left.fill('red')
        self.top_right.fill('blue')
        self.bottom_left.fill('green')
        self.bottom_right.fill('yellow')

        self.clock = pygame.time.Clock()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def mainloop(self):
        while True:
            self.event_handler()
            self.screen.blit(self.top_left, (0,0))
            self.screen.blit(self.top_right, (0, config.height_prct(self.height, 50)))
            self.screen.blit(self.bottom_left, (config.width_prct(self.width, 50), config.height_prct(self.height, 50)))
            self.screen.blit(self.bottom_right, (config.width_prct(self.width, 50), 0))

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    window = Window()
    window.mainloop()
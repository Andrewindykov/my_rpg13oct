import pygame
from constants import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.bsckground = pygame.image.load(data/background.jpg)
        self.running = True
        self.main_loop()

    def handle_events(self):
        pass

    def render(self):

        self.screen.blit(self.bsckground(0,0))
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            self.render()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
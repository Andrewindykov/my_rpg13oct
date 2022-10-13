import pygame
from constants import *

class Player():
    def __init__(self):
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.direction = RIGHT
        self.name = 'Lancelot'
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ['data/archerr.png','data/archerd.png','data/archerl.png','data/archeru.png']
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i=[]
            i.append(temp.subsurface(0,0,64,64))
            i.append(temp.subsurface(64, 0, 64, 64))
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)
        self.mooving[0, 0, 0, 0]

    def moove(self):
        pass

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        pass



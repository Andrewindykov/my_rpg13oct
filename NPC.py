import pygame as pg

from messages import Message
from settings import *


class NPC(pg.sprite.Sprite):
    """Class for creating Non-Player Characters."""

    def __init__(self, game, pos, image, items={'soul':1}):
        """Initialize required variables."""
        self._layer = GROUND_LAYER
        groups = game.all_sprites, game.walls
        super().__init__(groups)
        self.game = game
        self.image = image
        self.items = items
        self.rect = self.image.get_rect(center=pos)
        self.message = Message(game, (pos[0], pos[1]-40),f'I have: {self.items}')

    def update(self):
        """Update current message."""
        # Show current message when colliding with the player
        if self.rect.colliderect(self.game.player):
            self.message.set_text(f'NPC have {self.items}')
            self.message.print(15, (self.rect.center[0], self.rect.center[1] - 40))
            self.game.player.sosed.add(self)
        elif self.message.groups():
            self.message.reset()
            self.game.player.sosed.clear()

        # Display a message at a specific point in time
        # if 8000 < pg.time.get_ticks() < 8020:
        #     self.message.set_text('The 8 time has come.')

        # if 2000 < pg.time.get_ticks() < 2020:
        #     self.message.set_text(f'i have {self.items}')
        # if 6000 < pg.time.get_ticks() < 6020:
        #      self.message.set_text(f'прошло {pg.time.get_ticks()//1000} сек')

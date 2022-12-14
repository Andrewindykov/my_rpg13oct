import pygame as pg

from player import Player
from NPC import NPC
from world import TileMap, Camera
from helper import res
from settings import *


class Game:
    """Generic class for holding game attributes."""

    def __init__(self):
        """Create the game window."""
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        pg.display.set_icon(pg.image.load(res/'sprites'/'frog.png'))
        self.running = True
        self.state="1"

    def new(self):
        """Initialize all the sprites."""
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.map = TileMap(self, res/'map'/'map.csv', res/'map'/'rpg_tileset.png', 16)
        self.camera = Camera(self.map.width, self.map.height)
        self.player = Player(self, res/'sprites'/'player_sheet.png', (100, 100))
        #self.NPC = NPC(self, (200, 100), self.map.image_list[119])
        self.NPC = NPC(self, (200, 100), self.map.image_list[125],{'frog':1,'sparrow':4})
        self.NPC2 = NPC(self, (300, 100), self.map.image_list[119],{'1':4,'2':88,'3':3})
        self.NPC4 = NPC(self, (50, 250), self.map.image_list[119], {})
        self.NPC5 = NPC(self, (350, 80), self.map.image_list[109], {'109':2})
        self.NPC6 = NPC(self, (400, 150), self.map.image_list[110], {'110':2})
        self.NPC7 = NPC(self, (450, 190), self.map.image_list[111], {'111':2})
        self.NPC8 = NPC(self, (100, 290), self.map.image_list[110], {'110':2})


    def _events(self):
        """Check for input events."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                        and event.key == pg.K_ESCAPE):
                self.running = False

    def _update(self):
        """Update everything that's on the screen."""
        self.all_sprites.update()
        self.camera.update(self.player)

    def _draw(self):
        """Draw every sprite."""
        pg.display.set_caption(f'{GAME_TITLE} FPS: {int(self.clock.get_fps())}')
        for sprite in self.all_sprites:
            # print(sprite, self.camera.apply(sprite.rect))
            self.screen.blit(sprite.image, self.camera.apply(sprite.rect))
        pg.display.flip()

    def _draw_player_hitbox(self):
        """Display player hitbox. For debug purposes only."""
        # Draw player rectangle
        pg.draw.rect(self.screen, (0, 180, 0), self.camera.apply(self.player.rect))
        # Draw the player
        self.screen.blit(self.player.image, self.camera.apply(self.player.rect))
        # Draw player physics body
        pg.draw.rect(self.screen, (0, 0, 0), self.camera.apply(self.player.phys_body))


    def run(self):
        """The game loop."""
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            #print(self.dt)
            self._events()
            self._update()
            self._draw()
            #print(pg.time.get_ticks())


if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()

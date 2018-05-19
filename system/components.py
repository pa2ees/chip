import logging
log = logging.getLogger(__name__)

import pygame

class GameThing(object):
    def __init__(self, *args, **kwargs):
        pass

class MovingThing(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.id = kwargs.get('id', 0)
        self.grid_coords = (0, 0)
        self.image = None
        self.l_image = None
        self.r_image = None
        self.group = kwargs.get('group', None)

class StationaryThing(GameThing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

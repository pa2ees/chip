import pygame
import logging
log = logging.getLogger(__name__)

from system.components import MovingThing
from config import *

class Player(MovingThing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = pygame.image.load('resources/popcorn.png')
        self.l_image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.r_image = pygame.transform.flip(self.l_image, True, False)
        self.x = GRID_XCOORD_START
        self.y = GRID_YCOORD_START
        if 'group' in kwargs:
            self.add(kwargs['group'])
        self.rect = self.l_image.get_rect()

    def update_sprite_pos(self):
        self.rect.x = self.x * GRID_BOX_WIDTH
        self.rect.y = self.y * GRID_BOX_HEIGHT
        
    
        

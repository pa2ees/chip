from config import *

import logging
log = logging.getLogger(__name__)

def move(entity, direction):
    if direction == LEFT:
        player.x -= 1
        if player.x < 0:
            player.x = 0
    if direction == RIGHT:
        player.x += 1
        if player.x >= GRID_WIDTH:
            player.x = GRID_WIDTH - 1
    if direction == UP:
        player.y -= 1
        if player.y < 0:
            player.y = 0
    if direction == DOWN:
        player.y += 1
        if player.y >= GRID_HEIGHT:
            player.y = GRID_HEIGHT - 1
    player.update_sprite_pos()

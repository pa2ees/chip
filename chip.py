import pygame
from pygame.locals import *
from entities.player import Player
from config import *

from system.movement import *

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(name)s | %(message)s')

log = logging.getLogger(__name__)

def main():
    pygame.init()
    id_counter = 0

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    all_sprites_list = pygame.sprite.Group()
    
    player = Player(id=id_counter, group=all_sprites_list)
    id_counter += 1

    game_done = False
    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log.debug("Game Done!")
                game_done = True
                continue

            if event.type == pygame.KEYDOWN:
                if (event.key == K_q or event.key == K_ESCAPE):
                    log.debug("Pressed q or ESC")
                    game_done = True
                    continue
                elif event.key == K_RIGHT:
                    move(player, RIGHT)
                elif event.key == K_LEFT:
                    move(player, LEFT)
                elif event.key == K_UP:
                    move(player, UP)
                elif event.key == K_DOWN:
                    move(player, DOWN)

        screen.fill(WHITE)

        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

            
    

    
    
if __name__ == '__main__':
    main()

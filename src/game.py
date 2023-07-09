import pygame

from const import *


class Game:

    def __init__(self):
        pass

    # show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 237) # light
                else:
                    color = (119, 148, 85) # dark
                
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, rect)
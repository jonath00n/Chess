import pygame

from const import *

class Game:

    def __init__(self):
        pass

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    # light
                    color = (235, 232, 226)
                else:
                    # dark
                    color = (0, 49, 82)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)
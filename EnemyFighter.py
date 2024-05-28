from pygame.locals import *
import pygame
from color import *

class EnemyFighter:
    def __init__(self, x = -1, y = -1, window_height = 640, window_width = 480, cell_size = 3):
        self.x = x
        self.y = y
        self.window_height = window_height
        self.window_width = window_width

        self.cell_size = cell_size
        if self.x == -1:
            self.x = self.window_width // 2
        if self.y == -1:
            self.y = 10

        self.fighterList = []
        return
    
    def drawComponent(self, grid):

        return
    
    def generateFighter(self):
        return
from pygame.locals import *
from Fighter import Fighter
import pygame
from color import *

class FighterMissile:
    def __init__(self, fireMissilePerIndex = 5, missileLength = 6, cell_size = 3):
        self.missiles = []
        self.fireMissilePerIndex = fireMissilePerIndex
        self.missileLength = missileLength
        self.cell_size = 3

        return
    
    def fireMissile(self, fighter: Fighter, index):
        if index % self.fireMissilePerIndex == 0:
            x = fighter.x
            y = fighter.y - fighter.fighterLength * self.cell_size

            missile = [x, y]
            self.missiles.append(missile)
        return
    
    def flyMissile(self):
        filter = []
        for ind, missile in enumerate(self.missiles):
            self.missiles[ind][1] -= self.cell_size * 2
            if self.missiles[ind][1] > 0:
                filter.append(self.missiles[ind])
        self.missiles = filter

    def drawComponent(self, grid):
        for missile in self.missiles:
            for i in range(self.missileLength):
                x = missile[0]
                y = missile[1] - (self.cell_size * i)
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, BLUE, rect)
            continue
    
from pygame.locals import *
from EnemyFighter import EnemyFighter
import pygame
from color import *

class EnemyFighterMissile:
    def __init__(self, fireMissilePerIndex = 5, missileLength = 6, cell_size = 3, window_height = 640, window_width = 480):
        self.missiles = []
        self.fireMissilePerIndex = fireMissilePerIndex
        self.missileLength = missileLength
        self.cell_size = cell_size
        self.window_height = window_height
        self.window_width = window_width

        self.MissileColor = RED

        return
    
    def fireMissile(self, fighters: EnemyFighter, index):
        for ind, fighter in enumerate(fighters.fighterList):
            if fighters.fighterListStatus[ind] == 'DEAD':
                continue
            if index % self.fireMissilePerIndex == 0:
                x = fighter[0]
                y = fighter[1] + fighters.fighterLength * self.cell_size

                missile = [x, y]
                self.missiles.append(missile)
        return
    
    def flyMissile(self):
        filter = []
        for ind, missile in enumerate(self.missiles):
            self.missiles[ind][1] += self.cell_size * 2
            if self.missiles[ind][1] + self.missileLength * self.cell_size < self.window_height:
                filter.append(self.missiles[ind])
        self.missiles = filter

    def drawComponent(self, grid):
        for missile in self.missiles:
            for i in range(self.missileLength):
                x = missile[0]
                y = missile[1] + (self.cell_size * i)
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, RED, rect)
            continue
    
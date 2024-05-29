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
        for fighter in self.fighterList:
            x = fighter[0]
            y = fighter[1]
            for i in range(20):
                diff = i * self.cell_size
                diff_x = self.cell_size * 0
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [7, 6]:
                    pygame.draw.rect(grid, RED, rect)
            for i in range(2, 16):
                diff = i * self.cell_size
                diff_x = self.cell_size * 1
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [5, 6]:
                    pygame.draw.rect(grid, RED, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [5, 6]:
                    pygame.draw.rect(grid, RED, rect)
            for i in range(2, 16):
                diff = i * self.cell_size
                diff_x = self.cell_size * 2
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
            for i in range(1, 9):
                diff = i * self.cell_size
                diff_x = self.cell_size * 3
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [1, 2, 3]:
                    pygame.draw.rect(grid, RED, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [1, 2, 3]:
                    pygame.draw.rect(grid, RED, rect)
            for i in range(1, 7):
                diff = i * self.cell_size
                diff_x = self.cell_size * 4
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [1, 2]:
                    pygame.draw.rect(grid, RED, rect)
                if i in [6]:
                    pygame.draw.rect(grid, BLUE, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [1, 2]:
                    pygame.draw.rect(grid, RED, rect)
                if i in [6]:
                    pygame.draw.rect(grid, BLUE, rect)
            for i in range(3, 11):
                diff = i * self.cell_size
                diff_x = self.cell_size * 5
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [10, 9]:
                    pygame.draw.rect(grid, RED, rect)
                if i in [5]:
                    pygame.draw.rect(grid, BLUE, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [10, 9]:
                    pygame.draw.rect(grid, RED, rect)
                if i in [5]:
                    pygame.draw.rect(grid, BLUE, rect)
            for i in range(3, 5):
                diff = i * self.cell_size
                diff_x = self.cell_size * 6
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
            for i in range(3, 4):
                diff = i * self.cell_size
                diff_x = self.cell_size * 7
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
            for i in range(3, 9):
                diff = i * self.cell_size
                diff_x = self.cell_size * 8
                rect = pygame.Rect(x + diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [8, 7]:
                    pygame.draw.rect(grid, RED, rect)
                rect = pygame.Rect(x - diff_x, y + diff, self.cell_size, self.cell_size)
                pygame.draw.rect(grid, WHITE, rect)
                if i in [8, 7]:
                    pygame.draw.rect(grid, RED, rect)
        return
    
    def generateFighter(self):
        if len(self.fighterList) == 0:
            coord = (self.x, self.y)
            self.fighterList.append(coord)
            return
        return
    
    def moveFighter(self):
        return
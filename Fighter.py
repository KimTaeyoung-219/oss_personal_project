from pygame.locals import *
import pygame
from color import *

class Fighter:
    def __init__(self, x = -1, y = -1, window_height = 640, window_width = 480, cell_size = 3):
        self.window_width = window_width
        self.window_height = window_height
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.fighterLength = 20

        if self.x == -1:
            self.x = self.window_width // 2
        if self.y == -1:
            self.y = self.window_height - 10
        return
    
    def setDirection(self, event):
        if event == K_RIGHT:
            if self.x < self.window_width - self.cell_size:
                self.x += self.cell_size
        elif event == K_LEFT:
            if self.x > self.cell_size:
                self.x -= self.cell_size
        # print(f"x: {self.x}, y: {self.y}")
    
    def setDirection2(self, to_x):
        self.x += to_x * self.cell_size * 2
        if self.x < 0:
            self.x = 0
        elif self.x > self.window_width:
            self.x = self.window_width
    
    def drawComponent(self, grid):
        for i in range(19):
            diff = i * self.cell_size
            rect = pygame.Rect(self.x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [8, 7, 18, 17, 16]:
                pygame.draw.rect(grid, RED, rect)
        for i in range(3, 15):
            diff = i * self.cell_size
            diff_x = self.cell_size * 1
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [6, 7]:
                pygame.draw.rect(grid, RED, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [6, 7]:
                pygame.draw.rect(grid, RED, rect)
        for i in range(2, 11):
            diff = i * self.cell_size
            diff_x = self.cell_size * 2
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
        for i in range(1, 10):
            diff = i * self.cell_size
            diff_x = self.cell_size * 3
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [1, 2, 3]:
                pygame.draw.rect(grid, RED, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [1, 2, 3]:
                pygame.draw.rect(grid, RED, rect)
        for i in range(1, 10):
            diff = i * self.cell_size
            diff_x = self.cell_size * 4
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [0, 1, 2]:
                pygame.draw.rect(grid, RED, rect)
            if i in [9]:
                pygame.draw.rect(grid, BLUE, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [0, 1, 2]:
                pygame.draw.rect(grid, RED, rect)
            if i in [9]:
                pygame.draw.rect(grid, BLUE, rect)
        for i in range(4, 13):
            diff = i * self.cell_size
            diff_x = self.cell_size * 5
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [12, 11]:
                pygame.draw.rect(grid, RED, rect)
            if i in [8]:
                pygame.draw.rect(grid, BLUE, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [12, 11]:
                pygame.draw.rect(grid, RED, rect)
            if i in [8]:
                pygame.draw.rect(grid, BLUE, rect)
        for i in range(3, 8):
            diff = i * self.cell_size
            diff_x = self.cell_size * 6
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
        for i in range(2, 7):
            diff = i * self.cell_size
            diff_x = self.cell_size * 7
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
        for i in range(1, 6):
            diff = i * self.cell_size
            diff_x = self.cell_size * 8
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
        for i in range(0, 10):
            diff = i * self.cell_size
            diff_x = self.cell_size * 9
            rect = pygame.Rect(self.x + diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [9, 8]:
                pygame.draw.rect(grid, RED, rect)
            rect = pygame.Rect(self.x - diff_x, self.y - diff, self.cell_size, self.cell_size)
            pygame.draw.rect(grid, WHITE, rect)
            if i in [9, 8]:
                pygame.draw.rect(grid, RED, rect)
        return
    
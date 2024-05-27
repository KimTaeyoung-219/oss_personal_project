import pygame
from Fighter import Fighter
from EnemyFighter import EnemyFighter

class TopGun:
    def __init__ (self, window_width = 640, window_height = 480, cell_size = 10, fps = 10):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
        self.fps = fps

        self.X = self.window_width / self.cell_size
        self.Y = self.window_height / self.cell_size

        self.Fighter = Fighter()
        self.EnemyFighters = []

        self.FighterMissile = []
        self.EnemyFightersMissile = []

        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.window_height, self.window_width))
        pygame.display.set_caption('Top Gun')
    
    def start(self):

        self.drawComponents()
        running = True
        while running:
            event = self.getKeyEvent()
            self.drawComponents()

            self.fps_clock.tick(self.fps)
        return

    def drawComponents(self):
        self.Fighter.drawComponent(self.display)
        for EnemyFighter in self.EnemyFighter:
            EnemyFighter.drawComponent(self.display)

        for missile in self.FighterMissile:
            missile.drawComponent(self.display)

    def getKeyEvent(self):
        return
    
    def checkForKey(self):
        return
    
    def checkFighterDead(self):
        return
    
    def checkEnemyFighterDead(self):
        return
 
if __name__ == "__main__":
    game = TopGun()
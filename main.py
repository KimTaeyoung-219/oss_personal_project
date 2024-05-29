import pygame, sys
from pygame.locals import *
from Fighter import Fighter
from EnemyFighter import EnemyFighter
from FighterMissile import FighterMissile
from EnemyFighterMissile import EnemyFighterMissile
from color import *

# make enemy fighter
# make enemy fighter fire missile
# set when missile is hit in opponent aircraft
# set THE END of something like that

class TopGun:
    def __init__ (self, window_height = 640, window_width = 480, cell_size = 10, fps = 10):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
        self.fps = fps

        self.X = self.window_width / self.cell_size
        self.Y = self.window_height / self.cell_size

        fighter_x = self.window_width // 2
        fighter_y = self.window_height - 20

        self.Fighter = Fighter(x = fighter_x, y = fighter_y, window_height = self.window_height, window_width = self.window_width)
        self.EnemyFighter = EnemyFighter(window_height = self.window_height, window_width = self.window_width)

        self.FighterMissile = FighterMissile()
        self.EnemyFightersMissile = EnemyFighterMissile()

        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.display_grid = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Top Gun')
    
    def start(self):
        running = True
        to_x = 0
        index = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        to_x = 1
                    elif event.key == pygame.K_LEFT:
                        to_x = -1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        to_x = 0
                    elif event.key == pygame.K_LEFT:
                        to_x = 0
            self.Fighter.setDirection2(to_x)

            self.FighterMissile.flyMissile()
            self.FighterMissile.fireMissile(self.Fighter, index)

            self.EnemyFighter.generateFighter()
            self.EnemyFightersMissile.flyMissile()
            # self.EnemyFightersMissile.fireMissile(self.Fighter, index)

            # draw airplane, opponents and missiles into the Grid
            self.drawComponents()
            self.fps_clock.tick(self.fps)
            index += 1
        return

    def drawComponents(self):
        self.display_grid.fill(BGCOLOR)
        self.Fighter.drawComponent(self.display_grid)
        self.FighterMissile.drawComponent(self.display_grid)
        self.EnemyFighter.drawComponent(self.display_grid)
        pygame.display.update()
    
    def checkFighterDead(self):
        return
    
    def checkEnemyFighterDead(self):
        return
    
    def theEnd(self):
        pygame.quit()
        sys.exit()
 
if __name__ == "__main__":
    game = TopGun()
    game.start()
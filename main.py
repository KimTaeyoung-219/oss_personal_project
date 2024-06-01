import pygame, sys
from pygame.locals import *
from Fighter import Fighter
from EnemyFighter import EnemyFighter
from FighterMissile import FighterMissile
from EnemyFighterMissile import EnemyFighterMissile
from color import *

# draw crash, move Enemyfighter when range is outerbound
# set sound effect
# set when fighter get crashed
# decorate Enemyfighter

class TopGun:
    def __init__ (self, window_height = 640, window_width = 480, cell_size = 10, fps = 20):
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

        self.crashEffect1 = []
        self.crashEffect2 = []

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

            self.EnemyFighter.moveFighter()
            self.EnemyFighter.generateFighter()
            self.EnemyFightersMissile.flyMissile()
            self.EnemyFightersMissile.fireMissile(self.EnemyFighter, index)

            self.checkMissilesHit()
            self.checkEnemyFighterDead()
            self.checkFighterDead()

            # draw airplane, opponents and missiles into the Grid
            self.drawComponents()
            self.fps_clock.tick(self.fps)
            index += 1
            # input()
        return

    def drawComponents(self):
        self.display_grid.fill(BGCOLOR)
        self.Fighter.drawComponent(self.display_grid)
        self.FighterMissile.drawComponent(self.display_grid)
        self.EnemyFighter.drawComponent(self.display_grid)
        self.EnemyFightersMissile.drawComponent(self.display_grid)
        self.drawCrash()
        pygame.display.update()

    def checkMissilesHit(self):
        filter = []
        Enemyfilter = []
        EnemyMissileLength = self.EnemyFightersMissile.cell_size * self.EnemyFightersMissile.missileLength
        MissileLength = self.FighterMissile.cell_size * self.FighterMissile.missileLength
        for ind1, missile in enumerate(self.FighterMissile.missiles):
            for ind2, Enemymissile in enumerate(self.EnemyFightersMissile.missiles):
                if missile[0] == Enemymissile[0]:
                    if abs(missile[1]- Enemymissile[1]) < EnemyMissileLength + MissileLength:
                        mid = (missile[1] + Enemymissile[1]) // 2
                        # self.drawCrash(missile[0], mid)
                        self.crashEffect1.append((missile[0], mid)) 
                        filter.append(missile)
                        Enemyfilter.append(Enemymissile)
        filter2 = []
        Enemyfilter2 = []
        for missile in self.FighterMissile.missiles:
            if missile not in filter:
                filter2.append(missile)
        for missile in self.EnemyFightersMissile.missiles:
            if missile not in Enemyfilter:
                Enemyfilter2.append(missile)
        self.EnemyFightersMissile.missiles = Enemyfilter2
        self.FighterMissile.missiles = filter2
        return
    
    def checkFighterDead(self):
        for Enemymissile in self.EnemyFightersMissile.missiles:
            y = Enemymissile[1] + self.EnemyFightersMissile.cell_size * self.EnemyFightersMissile.missileLength
            flag = self.Fighter.checkHit(Enemymissile[0], y)
            if flag is True:
                print("DEAD!!")
        return
    
    def checkEnemyFighterDead(self):
        for missile in self.FighterMissile.missiles:
            y = missile[1] - self.FighterMissile.cell_size * self.FighterMissile.missileLength
            flag = self.EnemyFighter.checkHit(missile[0], y)
            if flag is True:
                print("CRASH!!")
        return
    
    def drawCrash(self):
        lineWidth = 5
        for x, y in self.crashEffect1:
            self.drawImpact(x, y)
        for x, y in self.crashEffect2:
            self.drawImpact(x, y)
        self.crashEffect2 = self.crashEffect1
        self.crashEffect1 = []
        return
    
    def drawImpact(self, x, y):
        lineWidth = 5
        pygame.draw.circle(self.display_grid, WHITE, [x, y], 20, 5)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x + 30, y], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x, y + 30], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x - 30, y], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x, y - 30], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x + 15, y + 26], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x + 15, y - 26], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x - 15, y + 26], lineWidth)
        pygame.draw.line(self.display_grid, WHITE, [x, y], [x - 15, y - 26], lineWidth)
        return
    
    def end(self):
        pygame.quit()
        sys.exit()
 
if __name__ == "__main__":
    game = TopGun()
    game.start()
    game.end()
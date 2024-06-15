import pygame, sys
from pygame.locals import *
from Fighter import Fighter
from EnemyFighter import EnemyFighter
from FighterMissile import FighterMissile
from EnemyFighterMissile import EnemyFighterMissile
from color import *

class TopGun:
    def __init__ (self, window_height = 640, window_width = 480, cell_size = 3, fps = 20):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
        self.fps = fps
    

        self.X = self.window_width / self.cell_size
        self.Y = self.window_height / self.cell_size

        self.fighter_x = self.window_width // 2
        self.fighter_y = self.window_height - 20

        self.Fighter = Fighter(x = self.fighter_x, y = self.fighter_y, window_height = self.window_height, window_width = self.window_width)
        self.EnemyFighter = EnemyFighter(window_height = self.window_height, window_width = self.window_width)

        self.FighterMissile = FighterMissile(cell_size = self.cell_size, window_height = self.window_height, window_width = self.window_width)
        self.EnemyFightersMissile = EnemyFighterMissile(cell_size = self.cell_size, window_height = self.window_height, window_width = self.window_width)

        self.crashEffect1 = []
        self.crashEffect2 = []

        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.display_grid = pygame.display.set_mode((self.window_width, self.window_height))
        self.basic_font = pygame.font.Font('freesansbold.ttf', 18)
        self.bomb_image = pygame.image.load('source/bomb.gif').convert_alpha()
        self.bomb_size = 100
        self.bomb_image = pygame.transform.scale(self.bomb_image, (self.bomb_size, self.bomb_size))
        pygame.display.set_caption('Top Gun')

        
        ###Phase2##########    
        self.setIcon_image = pygame.image.load('source/setIcon.png')
        self.setIcon_width = 40
        self.setIcon_height = 40
        self.setIcon_image = pygame.transform.scale(self.setIcon_image, (self.setIcon_width, self.setIcon_height))
        self.setIcon_x = self.window_width - self.setIcon_width - 10
        self.setIcon_y = 10
        
        self.pause = False
        self.pause_texts = [
            ("Resume Game", (self.window_width // 2, 200))
        ]
        self.pause_text_rects = []
        ###Phase2##########    

        self.firstIntro()

    def init(self):
        self.Fighter = Fighter(x = self.fighter_x, y = self.fighter_y, window_height = self.window_height, window_width = self.window_width)
        self.EnemyFighter = EnemyFighter(window_height = self.window_height, window_width = self.window_width)

        self.FighterMissile = FighterMissile(cell_size = self.cell_size, window_height = self.window_height, window_width = self.window_width)
        self.EnemyFightersMissile = EnemyFighterMissile(cell_size = self.cell_size, window_height = self.window_height, window_width = self.window_width)

        self.crashEffect1 = []
        self.crashEffect2 = []
        return
    
    def start(self):
        self.init()
        running = True
        to_x = 0
        to_y = 0
        index = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False 
                ###Phase2##########    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #mouse left click 
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        
                        if self.pause:
                            self.handle_pause_click(mouse_x, mouse_y)
                        else:
                            setIcon_rect = self.setIcon_image.get_rect(topleft=(self.setIcon_x, self.setIcon_y))
                            if setIcon_rect.collidepoint(mouse_x, mouse_y):
                                self.pause = not self.pause
                                if self.pause:
                                    #On setting page
                                    self.showSetting()
                ###Phase2##########    
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        to_x = 1
                    elif event.key == pygame.K_LEFT:
                        to_x = -1
                    elif event.key == pygame.K_UP:
                        to_y = -1
                    elif event.key == pygame.K_DOWN:
                        to_y = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        to_x = 0
                    elif event.key == pygame.K_LEFT:
                        to_x = 0
                    elif event.key == pygame.K_UP:
                        to_y = 0
                    elif event.key == pygame.K_DOWN:
                        to_y = 0
            ###Phase2##########    
            if self.pause:
                    continue
            ###Phase2##########    
            self.Fighter.setDirection2(to_x, to_y)

            self.FighterMissile.flyMissile()
            self.FighterMissile.fireMissile(self.Fighter, index)

            self.EnemyFighter.moveFighter()
            self.EnemyFightersMissile.flyMissile()
            self.EnemyFightersMissile.fireMissile(self.EnemyFighter, index)

            # draw airplane, opponents and missiles into the Grid
            self.drawComponents()

            self.checkMissilesHit()
            if self.checkEnemyFighterDead() is True:
                return "Win"
            if self.checkFighterDead() is True:
                return "Loss"

            # # draw airplane, opponents and missiles into the Grid
            # self.drawComponents()
            self.fps_clock.tick(self.fps)
            index += 1
            # input()
    ###Phase2##########    
    def showSetting(self):
        self.display_grid.fill((0,0,0))

        self.pause_text_rects = []
        font = pygame.font.Font(None, 36)
        for text, pos in self.pause_texts:
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=pos)
            self.pause_text_rects.append(text_rect)
            self.display_grid.blit(text_surface, text_rect)
        pygame.display.flip()


    def handle_pause_click(self, mouse_x, mouse_y):
        for index, rect in enumerate(self.pause_text_rects):
            if rect.collidepoint(mouse_x, mouse_y):
                self.perform_pause_action(index)

    def perform_pause_action(self, index):
        if index == 0:  # Resume Game
            self.pause = False
            print("Resume Game...")
    ###Phase2########## 
     
       
    def drawComponents(self):
        self.display_grid.fill(BGCOLOR)
        self.Fighter.drawComponent(self.display_grid)
        self.FighterMissile.drawComponent(self.display_grid)
        self.EnemyFighter.drawComponent(self.display_grid)
        self.EnemyFightersMissile.drawComponent(self.display_grid)
        ###Phase2##########    
        self.display_grid.blit(self.setIcon_image, (self.setIcon_x, self.setIcon_y))
        ###Phase2##########    
        self.drawCrash()
        pygame.display.update()

    def firstIntro(self):
        self.display_grid.fill(BGCOLOR)
        self.Fighter.drawComponent(self.display_grid)
        self.gameover('First')

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
                return True
        return False
    
    def checkEnemyFighterDead(self):
        for missile in self.FighterMissile.missiles:
            y = missile[1] - self.FighterMissile.cell_size * self.FighterMissile.missileLength
            flag = self.EnemyFighter.checkHit(missile[0], y, self)
            if flag is True:
                return True
        return False
    
    def drawCrash(self):
        for x, y in self.crashEffect1:
            self.display_grid.blit(self.bomb_image,(x - self.bomb_size / 2, y - self.bomb_size / 2))
        for x, y in self.crashEffect2:
            self.display_grid.blit(self.bomb_image,(x - self.bomb_size / 2, y - self.bomb_size / 2))
        self.crashEffect2 = self.crashEffect1
        self.crashEffect1 = []
        return
    
    def end(self):
        pygame.quit()
        sys.exit()

    def gameover(self, res):
        gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
        if res == "Win":
            gameSurf = gameOverFont.render('You', True, WHITE)
            overSurf = gameOverFont.render('Win!!', True, WHITE)
        elif res == 'Loss':
            gameSurf = gameOverFont.render('Game', True, WHITE)
            overSurf = gameOverFont.render('Over', True, WHITE)
        elif res == 'First':
            gameSurf = gameOverFont.render('Top', True, WHITE)
            overSurf = gameOverFont.render('Gun', True, WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (self.window_width / 2, 10)
        overRect.midtop = (self.window_width / 2, gameRect.height + 10 + 25)

        self.display_grid.blit(gameSurf, gameRect)
        self.display_grid.blit(overSurf, overRect)
        
        self.drawPressKeyMsg()
        
        pygame.display.update()
        pygame.time.wait(500)

        self.checkForKeyPress() # clear out any key presses in the event queue

        while True:
            if self.checkForKeyPress():
                pygame.event.get() # clear event queue
                return
                    
    def checkForKeyPress(self):
        if len(pygame.event.get(QUIT)) > 0:
            self.terminate()

        keyUpEvents = pygame.event.get(KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == K_ESCAPE:
            self.terminate()
        return keyUpEvents[0].key
    
    def drawPressKeyMsg(self):
        pressKeySurf = self.basic_font.render('Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (self.window_width - 200, self.window_height - 30)
        self.display_grid.blit(pressKeySurf, pressKeyRect)
 
if __name__ == "__main__":
    game = TopGun()
    #game = TopGun( 640, 480, 3, 60)

    while True:
        res = game.start()
        game.gameover(res)
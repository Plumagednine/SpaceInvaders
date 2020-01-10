from BasicGame import *
from pygame import *
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform, randint
import time

#add your classes here
from Player import *
from Projectile import *
# from Alien import *
from Wave import *
from UFO import *

#constants
FPS = 60 #Frames per second

class SpaceInvaders(BasicGame):
    def __init__(self):
        self.w, self.h = 800, 800
        self.bkg_color = (0,0,0)
        BasicGame.__init__(self, size=(self.w, self.h))
        self.bkgimg = pygame.image.load('images/background.jpg').convert_alpha()
        self.bkgimg = pygame.transform.scale(self.bkgimg, (self.w, self.h))
        self.goimg = pygame.image.load('images/game-over.jpg').convert_alpha()
        self.stimg = pygame.image.load('images/game-menu.png').convert_alpha()
        
        #create walls for the game
        self.LEFT_WALL = 0
        self.RIGHT_WALL = self.w
        self.TOP_WALL = 0
        self.BOTTOM_WALL = self.h
        self.shooting = False
        self.ufo = False
        self.count = 0
        self.score = 0
        self.alienshooting = False
        self.playeralive = False
        self.startmenu = True
        self.gameover = False
        self.winmenu = False

        #create a single Player
        self.Player = Player(self.w / 2, self.h - 75,0,0,5)
        self.UFO = UFO(self.LEFT_WALL, self.TOP_WALL+50, 5 , 0 , 'mystery.png')
        self.Wave = Wave(5, 10, 50, 100, 125,10,5)
        
    def update(self): 
        self.keyPoll()
        self.draw()
        if self.playeralive == True:
            self.count += 1
            self.Player.move()
            self.win()
            if self.ufo == True:
                self.UFO.move()
            if self.count%30 == 0:
                self.count = 0
                self.Wave.move()
                if self.ufo == False:
                        ufochance = randint(0,10)
                        if ufochance == 1:
                            self.ufo = True

            self.handle_collisions(self.Player, self.UFO, self.Wave)
            if self.shooting == True:
                self.PlayerProjectile.move()
            alienshotchance = randint(0,10)
            if alienshotchance == 1:
                if self.alienshooting == False:
                    self.alienshooting = True
                    self.Wave.shoot()

            if self.alienshooting == True:
                self.Wave.AlienProjectile.move()
            
        
        
        
    def handle_collisions(self, Player, UFO, Wave):
        if Player.right() > self.RIGHT_WALL:
            Player.x = self.LEFT_WALL
        elif Player.left() < self.LEFT_WALL:
            Player.x = self.RIGHT_WALL-Player.right()
        elif Player.top() < self.TOP_WALL:
            Player.bounce_vert()    
        elif Player.bottom() > self.BOTTOM_WALL:
            Player.bounce_vert()

        if self.shooting == True:
            if self.PlayerProjectile.bottom() < self.TOP_WALL:
                self.shooting = False
                self.PlayerProjectile.hit = False
           
            if self.PlayerProjectile.top() < Wave.bottom() and self.PlayerProjectile.left() < Wave.right() and self.PlayerProjectile.right() > Wave.left():
                if Wave.kill((int(((self.PlayerProjectile.left()-self.PlayerProjectile.right())/2)+self.PlayerProjectile.left()),int(self.PlayerProjectile.top()))) == True:
                    self.shooting = False
                    self.PlayerProjectile.hit = False
                    self.score += 2

            if UFO.dead == False:
                if self.PlayerProjectile.top() < UFO.bottom() and self.PlayerProjectile.left() > UFO.left() and self.PlayerProjectile.right() < UFO.right():
                    self.shooting = False
                    self.PlayerProjectile.hit = True
                    self.ufo = False
                    UFO.x = self.LEFT_WALL-UFO.right()/2
                    self.score += randint(3,10)

        if self.alienshooting == True:
            if Wave.AlienProjectile.bottom() > self.BOTTOM_WALL:
                self.alienshooting = False
                Wave.AlienProjectile.hit = False

            if Wave.AlienProjectile.bottom() > Player.top() and Wave.AlienProjectile.left() < Player.right() and Wave.AlienProjectile.right() > Player.left():
                self.playeralive = False
                self.alienshooting = False
                self.gameover = True
                Wave.AlienProjectile.hit = False

        if UFO.right() > self.RIGHT_WALL:
            self.ufo = False
            UFO.x = self.LEFT_WALL

        if self.count%30 == 0:    
            if Wave.right() > self.RIGHT_WALL:
                Wave.bounce_horiz()
                Wave.move_vert()
            elif Wave.left() < self.LEFT_WALL:
                Wave.bounce_horiz()
                Wave.move_vert() 
            
        #add code for the other three walls
        
        
    def keyPoll(self): 
        #use this function if you want to handle multiple key presses
        #this function must be called in update
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            pass #maybe "right" player moves down and right at same time?
        if keys[pygame.K_d] and keys[pygame.K_x]:
            pass #maybe "left" player moves down and right

    def set_Player_color(self, color):
        self.Player.set_color(color)
    
    def keyDown(self, key):
        if key == pygame.K_RIGHT:
            self.Player.dx = 2 
        elif key == pygame.K_LEFT:
            self.Player.dx = -2
        elif key == pygame.K_SPACE:
            if self.shooting == False:
                self.PlayerProjectile = Projectile(self.Player.imgmid, self.Player.y, 0 , -10 , 'laser.png' )
                self.shooting = True
       
        else:
            pass

    def keyUp(self, key):
        self.Player.dx = 0
        if self.gameover == True:
            time.sleep(.5)
            if key == pygame.K_SPACE:
                self.reset()
        elif self.startmenu == True:
            if key == pygame.K_SPACE:
                self.reset()
                self.startmenu = False
                self.playeralive = True
        elif self.winmenu == True:
            time.sleep(.5)
            if key == pygame.K_TAB:
                self.reset()
            if key == pygame.K_SPACE:
                self.gamecontinue()

            
    def mouseUp(self, button, pos):
        # self.Wave.kill(pos)
        if button == 1:
            pass
     
    def mouseDown(self, button, pos):
        if button == 1:
            pass    
        
    def mouseMotion(self, buttons, pos, rel):
        left, mid, right = buttons
        if left == 1:
            pass

    def reset(self):
        self.startmenu = True
        self.gameover = False
        self.score = 0
        self.shooting = False
        self.alienshooting = False
        self.winmenu = False
        self.Wave.reset()

    def gamecontinue(self):
        self.startmenu = False
        self.playeralive = True
        self.gameover = False
        self.shooting = False
        self.alienshooting = False
        self.winmenu = False
        self.Wave.reset()

    def scoretext(self, image, text, size, x, y):
        font = pygame.font.Font('fonts/space_invaders.ttf', size)
        scoretxt = "Score: " + text
        text_surface = font.render(scoretxt, True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        image.blit(text_surface, text_rect)
    
    def text(self, image, text, size, x, y):
        font = pygame.font.Font('fonts/space_invaders.ttf', size)
        text_surface = font.render(text, True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        image.blit(text_surface, text_rect)

    def win(self):
        if self.Wave.wavedie() == True:
            self.winmenu = True
            self.playeralive = False


    def draw(self):
        if self.playeralive == True:
            self.screen.blit(self.bkgimg,(0,0)) #clear screen
            self.Player.draw(self.screen)
            self.scoretext(self.screen, str(self.score), 18, self.RIGHT_WALL/2, 10)
            if self.shooting == True:
                self.PlayerProjectile.draw(self.screen)
            if self.ufo == True:
                self.UFO.draw(self.screen)
            self.Wave.draw(self.screen)
            if self.alienshooting == True:
                self.Wave.AlienProjectile.draw(self.screen)        
        elif self.gameover == True:
            self.screen.fill(self.bkg_color)
            self.text(self.screen, str("Game Over"), 75, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2-100))
            self.text(self.screen, str("Press SPACE to restart"), 25, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2))
            self.scoretext(self.screen, str(self.score), 25, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2 + 50))
        elif self.startmenu == True:
            self.screen.blit(self.bkgimg,(0,0))
            self.text(self.screen, str("Space Invaders"), 75, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2-100))
            self.text(self.screen, str("Press SPACE to start"), 25, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2))
        elif self.winmenu == True:
            self.screen.fill(self.bkg_color)
            self.text(self.screen, str("You Win"), 75, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2-100))
            self.text(self.screen, str("Press SPACE to continue or press TAB to restart"), 25, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2))
            self.scoretext(self.screen, str(self.score), 25, self.RIGHT_WALL/2, (self.BOTTOM_WALL/2 + 50))


        
        

        
s = SpaceInvaders()
s.mainLoop(FPS)

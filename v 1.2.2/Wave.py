import sys
import math
import pygame
import os
import random
if os.name == 'nt':
    os.environ['SDL_VIDEODRIVER'] = 'windib'
from Alien import *
from Projectile import *
#Task: create a two-dimensional Wave container that can be used for making games.
#How: write the bodies of the functions below.

class Wave:
    def __init__(self, num_rows, num_cols, size, x, y, dx, dy):
        self.startpos = x,y
        self.x = x
        self.y = y 
        self.dx = dx
        self.dy = dy
        self.move_down = False
        self.square = pygame.Surface((size,size))
        # self.color = (0, 0, 200)
        # self.sqwidth = 0
        # self.sqheight = 0
        # self.square.fill(self.color)
        self.sqwidth = self.square.get_width()
        self.sqheight = self.square.get_height()
        #create a list of lists with start_value as the initial value of each cell.
        self.Wave = [[0 for i in range(num_cols)]for j in range(num_rows)]
        self.fillWave()
        self.dead = False
        # self.x -= self.right()/4

        #create a pygame.Surface that is a square size x size

        # self.square.set_alpha(0)
        # create a font object for drawing text
    def fillWave(self):
        directory = "images\enemys\enemy1"
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                if y == 0:
                    directory = "images\enemys\enemy1"
                    directory2 = "images\explosionpurple.png"
                elif y == 1 or y == 2:
                    directory = "images\enemys\enemy2"
                    directory2 = "images\explosionblue.png"
                elif y == 3 or y == 4:
                    directory = "images\enemys\enemy3"
                    directory2 = "images\explosiongreen.png"
                self.set((x,y),Alien(directory,directory2))

    def get(self, pos):
        #return the value at the given position where pos = (x, y)
        x, y = pos
        return self.Wave[y][x]
    
    def set(self, pos, dead):
        #set the position to the given value where pos = (x, y)
        x, y = pos
        self.Wave[y][x] = dead
    
    def set_all(self, dead):
        #set all cells to the given value
        pass
    
    def num_cols(self):
        #return the number of columns in the Wave
        #hint: return the len() of the first list
        return len(self.Wave[0])
    
    def num_rows(self):
        #return the number of rows in the Wave
        #return the len() of the Wave 
        return len(self.Wave)
    
    def size(self):
        # use get_width to return the size of the square Surface you made in the
        # __init__ function
        return self.square.get_width()
    
    def Wave2pixel(self, pos):
        # given a position where pos = (x, y) is in Wave coordinates
        # return the pixel coordinates of the northwest corner of pos 
        x, y = pos
        x *= self.size()
        y *= self.size()
        x += self.x
        y += self.y
        return (x,y)
    
    def pixel2Wave(self, pos):
        # given a position where pos = (x, y) is in pixel coordinates
        # return the Wave coordinates of the northwest corner of pos
        x, y = pos
        x -= self.x
        y -= self.y
        return (x // self.size(), y // self.size())
    
    def draw(self, image):
        # draw the entire Grid onto the given image
        # make a double nested loop then
        # use draw_cell to draw a single cel
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                self.draw_cell(image,(x,y))
        

    def draw_cell(self, image, pos):
        # draw a single cell
        alien = self.get(pos)
        if alien.dead == False:
            alienimg = alien.getimg()
            image.blit(alienimg, self.Wave2pixel(pos))

    def kill(self, pos):
        alien = self.get(self.pixel2Wave(pos))
        if alien.dead == False:
            alien.dieing = True
            return True
        else:
            return False

    def wavedie(self):
        alive = []
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                alien = self.get((x,y))
                if alien.dead == False:
                    alive.append((x,y))
        if len(alive) == 0:
            return True
        else:
            alive.clear()
            return False


    def move(self):
        self.imagechange()
        self.move_horz()
    
    def imagechange(self):
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                alien = self.get((x,y))
                if alien.dieing == True:
                    alien.dead = True
                if alien.dead == False:
                    alien.imgchange()


    #write a comment
    def right(self):
        for x in range(self.num_cols()-1,-1,-1):
            for y in range(self.num_rows()):
                alien = self.get((x,y))
                if alien.dead == False:
                    rightside = self.x + (x+1)*self.sqwidth
                    return rightside
        return self.x
    
    #write a comment
    def left(self):
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                alien = self.get((x,y))
                if alien.dead == False:
                    leftside = self.x + (x)*self.sqwidth
                    return leftside
        return self.x


    #write a comment
    def top(self):
        for y in range(self.num_rows()):   
            for x in range(self.num_cols()):
                alien = self.get((x,y))
                if alien.dead == False:
                    self.topside = self.y + (y)*self.sqheight
                    return self.topside
        return self.y         
          
    #write a comment
    def bottom(self):
        for y in range(self.num_rows()-1,-1,-1):   
            for x in range(self.num_cols()):
                alien = self.get((x,y))
                if alien.dead == False:
                    self.bottomside = self.y + (y+1)*self.sqheight
                    return self.bottomside
        return self.y            
    
    def move_horz(self):
        self.x = self.x + self.dx
        return self.x

    

    def move_vert(self):
        self.y  = self.y + self.dy
        return self.y

    def bounce_horiz(self):
        self.dx = (-1*self.dx)
        return self.dx

    
    #write a comment
    def bounce_vert(self):
        self.dy = (-1*self.dy)
        return self.dy

    def bottomaliens(self):
        botalien = []
        for x in range(self.num_cols()):
            for y in range(self.num_rows()-1,-1,-1):
                alien = self.get((x,y))
                if alien.dead == False:
                    botalien.append((x,y))
                    break
        return botalien

    def shoot(self):
        alienpos = self.Wave2pixel(random.choice(self.bottomaliens()))
        x , y = alienpos
        y += self.sqheight
        x += self.sqwidth/2
        self.AlienProjectile = Projectile(x, y, 0, 10, 'enemylaser.png' )
        return self.AlienProjectile

    def reset(self):
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                alien = self.get((x,y))
                if alien.dead == True:
                    alien.dead = False
                    alien.dieing = False
                alien.reset()
        self.x,self.y = self.startpos


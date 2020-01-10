import math
import pygame

class UFO:
    def __init__(self, x = 0, y=0, dx=0, dy=0, ufoimg = ''):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = 30
        self.ufoimg = ufoimg.strip(' ')
        self.imgpath = 'images/'+self.ufoimg
        self.ufo = pygame.image.load(self.imgpath).convert_alpha()
        self.ufo = pygame.transform.scale(self.ufo, (int(self.ufo.get_width()/3), int(self.ufo.get_height()/3)))
        self.x = self.x - self.ufo.get_width()
        self.dead = False

        
    #UFO methods
    #draw: UFO, image -> image
    #draw the UFO on an image
    def draw(self, image):
        if self.dead == False:
            image.blit(self.ufo, (self.x,self.y))
            return image
        

    
    
    #move: UFO -> None
    def move(self):
        self.move_horz()
        self.move_vert()
    
    #write a comment
    def right(self):
        return self.x + self.ufo.get_width()
        
    
    #write a comment
    def left(self):
        return self.x

    #write a comment
    def top(self):
        return self.y     
          
    #write a comment
    def bottom(self):
        return self.y + self.ufo.get_height()         
    
    #move: UFO -> None
    #move the move horizontally
    #Hint: add x + dx 
    def move_horz(self):
        self.x = self.x + self.dx
        return self.x

    
    #move: UFO -> None
    #move the move vertically
    #Hint: add y + dy
    def move_vert(self):
        self.y  = self.y + self.dy
        return self.y
      
    

   
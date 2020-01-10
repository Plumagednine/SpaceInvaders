import math
import pygame

class Projectile:
    def __init__(self, x = 0, y=0, dx=0, dy=0, laser = ''):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = 30
        self.laser = laser.strip(' ')
        self.imgpath = 'images/'+self.laser
        self.shot = pygame.image.load(self.imgpath).convert_alpha()
        self.x = self.x - self.shot.get_width()/2
        self.hit = False

        
    #Projectile methods
    #draw: Projectile, image -> image
    #draw the Projectile on an image
    def draw(self, image):
        if self.hit == False:
            image.blit(self.shot, (self.x,self.y))
        return image

    
    
    #move: Projectile -> None
    def move(self):
        self.move_horz()
        self.move_vert()
    
    #write a comment
    def right(self):
        return self.x + self.shot.get_width()
        
    
    #write a comment
    def left(self):
        return self.x

    #write a comment
    def top(self):
        return self.y     
          
    #write a comment
    def bottom(self):
        return self.y + self.shot.get_height()         
    
    #move: Projectile -> None
    #move the move horizontally
    #Hint: add x + dx 
    def move_horz(self):
        self.x = self.x + self.dx
        return self.x

    
    #move: Projectile -> None
    #move the move vertically
    #Hint: add y + dy
    def move_vert(self):
        self.y  = self.y + self.dy
        return self.y
      
    

   
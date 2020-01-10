import math
import pygame


class Player:
    def __init__(self, x = 0, y=0, dx=0, dy=0, hp=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = 30
        self.hp = hp
        self.playership = pygame.image.load('images/ship.png').convert_alpha()
        self.imgmid = self.x + self.playership.get_width()/2
        self.x = self.x - self.playership.get_width()/2

        
    #Player methods
    #draw: Player, image -> image
    #draw the Player on an image
    def draw(self, image):
        image.blit(self.playership, (self.x,self.y))
        return image

    
    
    #move: Player -> None
    def move(self):
        self.move_horz()
        self.move_vert()
        self.imgmid = self.x + self.playership.get_width()/2
    
    #write a comment
    def right(self):
        return self.x + self.playership.get_width()
        
    
    #write a comment
    def left(self):
        return self.x

    #write a comment
    def top(self):
        return self.y     
          
    #write a comment
    def bottom(self):
        return self.y + self.playership.get_height()         
    
    #move: Player -> None
    #move the move horizontally
    #Hint: add x + dx 
    def move_horz(self):
        self.x = self.x + self.dx
        return self.x

    
    #move: Player -> None
    #move the move vertically
    #Hint: add y + dy
    def move_vert(self):
        self.y  = self.y + self.dy
        return self.y
      
    #write a comment
    def bounce_horiz(self):
        self.dx = (-self.dx)

    
    #write a comment
    def bounce_vert(self):
        self.dy = (-self.dy)
    

   
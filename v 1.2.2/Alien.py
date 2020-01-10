import math
import pygame
import os

class Alien:
    def __init__(self,directory = '', directorydeath = ''):
        self.images = []
        directory = os.fsencode(directory)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            image = pygame.image.load(os.path.join(os.fsdecode(directory), filename)).convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width()/3.5), int(image.get_height()/3.5)))
            self.images.append(image)
        self.currentimage = self.images[0].convert_alpha()
        self.height = int(self.currentimage.get_height())
        self.width = int(self.currentimage.get_width())
        self.deathimg = pygame.image.load(directorydeath).convert_alpha()
        self.deathimg = pygame.transform.scale(self.deathimg, (self.width, self.height))
        self.dead = False
        self.imgv1 = True
        self.dieing = False

        
    def getimg(self):
        if self.dieing == True:
            return self.deathimg
        else:
            return self.currentimage

    def imgchange(self):
        if self.dieing == False:
            if self.imgv1 == True:
                self.currentimage = self.images[1]
                self.imgv1 = False
            else:
                self.currentimage = self.images[0]
                self.imgv1 = True

    def reset(self):
        self.currentimage = self.images[0].convert_alpha()
        self.imgv1 = True

        
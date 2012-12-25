import pygame
from pygame import *

class Gallows():

    def __init__(self,surface,pos):
        self.attempt = 1
        self.surface = surface
        self.pos = pos
        self.attempts(1)


    def attempts(self,attempt=-1):
        if attempt < 0:
            attempt = self.attempt + 1

        self.attempt = attempt
        if self.attempt > 8:
            return False

        image_name = 'assets\\hangman%d.gif' % self.attempt

        self.pic = image.load(image_name)
        self.surface.blit(self.pic,self.pos)
        display.update()
        if self.attempt == 8:
            return False
        return True
import pygame
from pygame import *


class Letter():


    def __init__(self,letter):
        self.letter = letter
        pygame.init()
        self.font = font.SysFont("assets\\freesansbold.ttf",48)

        self.used = False

    def display_available(self,surface,pos):
        s = self.font.render(self.letter,True,(255,255,255))
        self.pos = pos
        self.surface = surface
        surface.blit(s,pos)
        display.update((pos),self.font.size(self.letter))
        return s

    def mark_used(self):
        x1 = self.pos[0]
        y1 = self.pos[1]
        s = self.font.size(self.letter)
        x2 = x1+s[0]
        y2 = y1+s[1]
        draw.line(self.surface,Color(255,0,0),(x2,y1),(x1,y2),5)
        display.update((self.pos),self.font.size(self.letter))
        self.used = True


    def size(self):
        return self.font.size(self.letter)
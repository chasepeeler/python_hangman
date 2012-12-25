import pygame
from pygame import *
import random
import string

class Word():



    def __init__(self,surface):
        pygame.init()
        self.surface = surface
        file = open('assets\\words.txt','r')
        wordlist = file.readlines()
        self.word = wordlist[random.randint(0,len(wordlist)-1)]
        self.word = string.strip(self.word,'\n')
        self.letters = []
        self.font = font.SysFont("assets\\freesansbold.ttf",48)

        self.draw_blanks()
        self.found = [False]
        self.found = self.found * len(self.word)


    def draw_blanks(self):
        max_w = 0
        max_h = 0
        for l in list(self.word):
            w = self.font.size(l)
            max_w = max(max_w,w[0])
            max_h = max(max_h,w[1])

        self.max_w = max_w
        self.max_h = max_h
        word_width = max_w*len(self.word) + 5*len(self.word)
        x = (640/2) - (word_width/2)
        y = 300

        for l in list(self.word):
            self.letters.append((x,y))
            y1 = y + max_h + 5
            start = (x,y1)
            x = x + max_w
            end = (x,y1)
            pygame.draw.line(self.surface,Color(255,255,255),start,end,3)
            x = x + 5


        display.update()


    def draw_letter_at_index(self,index):
        letter = self.word[index]
        pos = self.letters[index]
        f = self.font.render(letter,True,(255,255,255))
        s = self.font.size(letter)
        y = pos[1] + self.max_h - s[1]
        x = pos[0] + (self.max_w/2) - (s[0]/2)
        self.surface.blit(f,(x,y))
        display.update()

    def guess_letter(self,letter):
        letter_found = False
        i = 0
        for l in list(self.word):
            if l == letter:
                self.draw_letter_at_index(i)
                letter_found = True
                self.found[i] = True
            i = i + 1
        return letter_found

    def all_found(self):
        for f in self.found:
            if f == False:
                return False
        return True

    def draw_remaining(self):
        i = 0
        for f in self.found:
            if not f:
                self.draw_letter_at_index(i)
            i = i + 1


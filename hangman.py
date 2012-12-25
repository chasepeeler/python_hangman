import pygame
from pygame import *
import string
import random

class Hangman():

    def __init__(self,screen):
        self.screen = screen
        self.padding_size = 5

    def setup(self):
        self.screen.fill(pygame.Color(0,0,0))
        self.letters = {}
        x = 10
        y = 10
        max_h = 0
        for ll in string.lowercase:
            ll = ll.upper()
            l = Letter(ll)
            self.letters[ll] = l
            s = l.size()
            if x + s[0] >= 300:
                x = 10
                y = y + max_h + 5
            max_h = max(max_h,s[1])
            l.display_available(self.screen,(x,y))

            x = x + s[0] + self.padding_size

        self.gallows = Gallows(self.screen,(350,10))
        self.word = Word(self.screen)

    def display_end_message(self,message):
        f = pygame.font.Font(None,48)
        y = 300 + self.word.max_h + 5 + 3 + 5

        d = f.size(message)
        x = (640/2) - (d[0]/2);

        r = f.render(message,True,pygame.Color(255,255,0))
        self.screen.blit(r,(x,y))

        f = pygame.font.Font(None,24)
        y = y + d[1] + 5
        d = f.size("Play Again? Y/N")

        x = (640/2) - (d[0]/2)
        r = f.render("Play Again? Y/N",True,pygame.Color(255,255,255))
        self.screen.blit(r,(x,y))
        pygame.display.update()

    def check_letter(self,letter):
        letter.mark_used()
        has_word = self.word.guess_letter(letter.letter)
        if has_word:
            if self.word.all_found():
                return 2
        elif not self.gallows.attempts():
            return 3
        return 0

    def check_clicked_letter(self,event):
        for k in self.letters:
            l = self.letters[k]
            r = pygame.Rect((l.pos),(l.size()))
            if r.collidepoint(event.pos) and not l.used:
                return self.check_letter(l)
        return 0    

    def check_typed_letter(self,l):
        return self.check_letter(self.letters[l])

    def main(self):
        quit = 0
        while quit == 0:

            for ourevent in pygame.event.get():
                if ourevent.type == QUIT:
                    quit = 1
                if ourevent.type == KEYDOWN:
                    if ourevent.key == K_a:
                        quit = self.check_typed_letter("A")
                    if ourevent.key == K_b:
                        quit = self.check_typed_letter("B")
                    if ourevent.key == K_c:
                        quit = self.check_typed_letter("C")
                    if ourevent.key == K_d:
                        quit = self.check_typed_letter("D")
                    if ourevent.key == K_e:
                        quit = self.check_typed_letter("E")
                    if ourevent.key == K_f:
                        quit = self.check_typed_letter("F")
                    if ourevent.key == K_g:
                        quit = self.check_typed_letter("G")
                    if ourevent.key == K_h:
                        quit = self.check_typed_letter("H")
                    if ourevent.key == K_i:
                        quit = self.check_typed_letter("I")
                    if ourevent.key == K_j:
                        quit = self.check_typed_letter("J")
                    if ourevent.key == K_k:
                        quit = self.check_typed_letter("K")
                    if ourevent.key == K_l:
                        quit = self.check_typed_letter("L")
                    if ourevent.key == K_m:
                        quit = self.check_typed_letter("M")
                    if ourevent.key == K_n:
                        quit = self.check_typed_letter("N")
                    if ourevent.key == K_o:
                        quit = self.check_typed_letter("O")
                    if ourevent.key == K_p:
                        quit = self.check_typed_letter("P")
                    if ourevent.key == K_q:
                        quit = self.check_typed_letter("Q")
                    if ourevent.key == K_r:
                        quit = self.check_typed_letter("R")
                    if ourevent.key == K_s:
                        quit = self.check_typed_letter("S")
                    if ourevent.key == K_t:
                        quit = self.check_typed_letter("T")
                    if ourevent.key == K_u:
                        quit = self.check_typed_letter("U")
                    if ourevent.key == K_v:
                        quit = self.check_typed_letter("V")
                    if ourevent.key == K_w:
                        quit = self.check_typed_letter("W")
                    if ourevent.key == K_x:
                        quit = self.check_typed_letter("X")
                    if ourevent.key == K_y:
                        quit = self.check_typed_letter("Y")
                    if ourevent.key == K_z:
                        quit = self.check_typed_letter("Z")
                if ourevent.type == MOUSEBUTTONDOWN:
                    quit = self.check_clicked_letter(ourevent)

        if quit == 1:
            return False
        elif quit == 2:
            self.display_end_message("Winner!!")
        elif quit == 3:
            self.display_end_message("Loser!!")
            self.word.draw_remaining()

        while True:
            for ourevent2 in event.get():
                if ourevent2.type == QUIT:
                    return False
                if ourevent2.type == KEYDOWN:
                    if ourevent2.key == K_n:
                        return False
                    if ourevent2.key == K_y:
                        return True


class Letter():

    def __init__(self,letter):
        self.letter = letter
        pygame.init()
        self.font = font.Font(None,48)

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


class Word():

    def __init__(self,surface):
        pygame.init()
        self.surface = surface
        file = open('assets\\words.txt','r')
        wordlist = file.readlines()
        self.word = wordlist[random.randint(0,len(wordlist)-1)]
        self.word = string.strip(self.word,'\n')
        self.letters = []
        self.font = font.Font(None,48)

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


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.mouse.set_visible(True)
    pygame.display.set_caption('Hangman')
    h = Hangman(screen)
    c = True
    while c:
        h.setup()
        c = h.main()

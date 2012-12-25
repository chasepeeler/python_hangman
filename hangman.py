import pygame
from pygame import *
import letter
import string
import gallows
import word

pygame.init()
screen = display.set_mode((640, 480))
pygame.mouse.set_visible(True)
display.set_caption('Hangman')


def setup():
    global _gallows, gallows, word, _word, pygame, letters, x, y, max_h, string, quit
    screen.fill(Color(0,0,0))
    quit = 0
    letters = {}

    x = 10
    y = 10
    max_h = 0
    for ll in string.lowercase:
        ll = ll.upper()
        l = letter.Letter(ll)
        letters[ll] = l
        s = l.size()
        if x + s[0] >= 300:
            x = 10
            y = y + max_h + 5
        max_h = max(max_h,s[1])
        l.display_available(screen,(x,y))

        x = x + s[0] + 5

    _gallows = gallows.Gallows(screen,(350,10))
    _word = word.Word(screen)

def display_end_message(message):
    f = font.SysFont("assets\\freesansbold.ttf",48)

    y = 300 + _word.max_h + 5 + 3 + 5

    d = f.size(message)

    x = (640/2) - (d[0]/2);

    r = f.render(message,True,Color(255,255,0))
    screen.blit(r,(x,y))

    f = font.SysFont("assets\\freesansbold.ttf",24)
    y = y + d[1] + 5
    d = f.size("Play Again? Y/N")

    x = (640/2) - (d[0]/2)
    r = f.render("Play Again? Y/N",True,Color(255,255,255))
    screen.blit(r,(x,y))
    display.update()

def check_letter(letter):
    global quit
    letter.mark_used()
    has_word = _word.guess_letter(letter.letter)
    if has_word:
        if _word.all_found():
            quit = 2
    else:
        cont = _gallows.attempts()
        if not cont:
            quit = 3

def check_clicked_letter(event):
    for k in letters:
        l = letters[k]
        r = pygame.Rect((l.pos),(l.size()))
        if r.collidepoint(event.pos) and not l.used:
            check_letter(l)
            break

def check_typed_letter(l):
    check_letter(letters[l])

def main():
    global quit
    while quit == 0:


        for ourevent in event.get():
            if ourevent.type == QUIT:
                quit = 1
            if ourevent.type == KEYDOWN:
                if ourevent.key == K_SPACE:
                    quit = 1
                if ourevent.key == K_a:
                    check_typed_letter("A")
                if ourevent.key == K_b:
                    check_typed_letter("B")
                if ourevent.key == K_c:
                    check_typed_letter("C")
                if ourevent.key == K_d:
                    check_typed_letter("D")
                if ourevent.key == K_e:
                    check_typed_letter("E")
                if ourevent.key == K_f:
                    check_typed_letter("F")
                if ourevent.key == K_g:
                    check_typed_letter("G")
                if ourevent.key == K_h:
                    check_typed_letter("H")
                if ourevent.key == K_i:
                    check_typed_letter("I")
                if ourevent.key == K_j:
                    check_typed_letter("J")
                if ourevent.key == K_k:
                    check_typed_letter("K")
                if ourevent.key == K_l:
                    check_typed_letter("L")
                if ourevent.key == K_m:
                    check_typed_letter("M")
                if ourevent.key == K_n:
                    check_typed_letter("N")
                if ourevent.key == K_o:
                    check_typed_letter("O")
                if ourevent.key == K_p:
                    check_typed_letter("P")
                if ourevent.key == K_q:
                    check_typed_letter("Q")
                if ourevent.key == K_r:
                    check_typed_letter("R")
                if ourevent.key == K_s:
                    check_typed_letter("S")
                if ourevent.key == K_t:
                    check_typed_letter("T")
                if ourevent.key == K_u:
                    check_typed_letter("U")
                if ourevent.key == K_v:
                    check_typed_letter("V")
                if ourevent.key == K_w:
                    check_typed_letter("W")
                if ourevent.key == K_x:
                    check_typed_letter("X")
                if ourevent.key == K_y:
                    check_typed_letter("Y")
                if ourevent.key == K_z:
                    check_typed_letter("Z")
            if ourevent.type == MOUSEBUTTONDOWN:
                check_clicked_letter(ourevent)




def post_main():
    if quit == 2:
        display_end_message("Winner!!")
    elif quit == 3:
        display_end_message("Loser!!")
        _word.draw_remaining()

    while not quit == 1:

        for ourevent2 in event.get():
            if ourevent2.type == QUIT:
                return False
            if ourevent2.type == KEYDOWN:
                if ourevent2.key == K_n:
                    return False
                if ourevent2.key == K_y:
                    return True


while True:
    setup()
    main()
    if not post_main():
        break






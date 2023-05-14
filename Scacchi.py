import pygame, sys
from pygame.locals import *
pygame.init()
WINDOW_SIZE=(1000,600)
screen=pygame.display.set_mode(WINDOW_SIZE)
screen.fill((240,240,180))
pygame.display.set_caption("Finestra base")


clock=pygame.time.Clock()
fps=60

class Square:
    def __init__(self, x, y, larg, alt) -> None:
        self.larg=larg
        self.alt=alt

        self.x=x
        self.xtot=x*larg

        self.y=y
        self.ytot=y*alt

        self.color="light" if (x+y)%2==0 else "dark"
        self.norm_color=(245, 237, 198) if self.color=="light" else(75,37,17)
        
        self.pezzo=None
        self.rect=pygame.Rect(self.xtot, self.ytot, self.larg, self.alt)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.pezzo!=None:
            pass



class Pawn:
    pass

class King:
    pass

class Queen:
    pass

class Bishop:
    pass

class Knight:
    pass

class Rook:
    pass


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        
    
        

    pygame.display.update()
    clock.tick(fps)
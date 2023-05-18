import pygame, sys
from pygame.locals import *
pygame.init()
WINDOW_SIZE=(1200,680)
screen=pygame.display.set_mode(WINDOW_SIZE)
screen.fill((240,240,180))
pygame.display.set_caption("Scacchi")


clock=pygame.time.Clock()
fps=60

class Square:
    def __init__(self, x, y, larg, alt, pezzo=None) -> None:
        self.larg=larg
        self.alt=alt

        self.x=x
        self.xtot=x*larg+344
        
        self.y=y
        self.ytot=y*alt+84

        self.color="light" if (x+y)%2==0 else "dark"
        self.norm_color=(245, 237, 198) if self.color=="light" else(75,37,17)
        
        self.pezzo=pezzo
        self.rect=pygame.Rect(self.xtot, self.ytot, self.larg, self.alt)


    def draw(self):
        pygame.draw.rect(screen, self.norm_color, self.rect)            



class Pawn:
    def __init__(self, colore, pos=None) -> None:
        self.colore=colore
        self.pos=pos
    
    def draw(self):
        self.image=pygame.image.load("pb.png").convert() if self.colore=="B" else pygame.image.load("pn.png").convert()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=40
        self.rect.height=40
        self.image=pygame.transform.scale(self.image,(40,40))
        screen.blit(self.image, self.rect)

class King:
    def __init__(self, colore, pos=None) -> None:
        self.colore=colore
        self.pos=pos
    
    def draw(self):
        self.image=pygame.image.load("reb.png").convert() if self.colore=="B" else pygame.image.load("ren.png").convert()
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        self.rect.width=40
        self.rect.height=40
        screen.blit(self.image, self.rect)

class Queen:
    def __init__(self, colore, pos=None) -> None:
        self.colore=colore
        self.pos=pos
    
    def draw(self):
        self.image=pygame.image.load("regb.png").convert() if self.colore=="B" else pygame.image.load("regn.png").convert()
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        self.rect.width=40
        self.rect.height=40
        screen.blit(self.image, self.rect)

class Bishop:
    def __init__(self, colore, pos=None) -> None:
        self.colore=colore
        self.pos=pos
    
    def draw(self):
        self.image=pygame.image.load("ab.png").convert() if self.colore=="B" else pygame.image.load("an.png").convert()
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        self.rect.width=40
        self.rect.height=40
        screen.blit(self.image, self.rect)


class Knight:
    def __init__(self, colore, pos=None) -> None:
        self.colore=colore
        self.pos=pos
    
    def draw(self):
        self.image=pygame.image.load("cb.png").convert() if self.colore=="B" else pygame.image.load("cn.png").convert()
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        self.rect.width=40
        self.rect.height=40
        screen.blit(self.image, self.rect)

class Rook:
    def __init__(self, colore, pos=None) -> None:
        self.colore=colore
        self.pos=pos
    
    def draw(self):
        self.image=pygame.image.load("tb.png").convert() if self.colore=="B" else pygame.image.load("tn.png").convert()
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        self.rect.width=40
        self.rect.height=40
        screen.blit(self.image, self.rect)




class Board:
    def __init__(self) -> None:
        self.board=[[Square(c, r, 64, 64) for c in range(8)] for r in range(8)]
        self.pezzi=[]

    def draw(self):
        for r in range(8):
            for c in range(8):
                self.board[r][c].draw()

        for pezzo in self.pezzi:
            pezzo.draw()

Scacchiera=Board()
for i in range(8):
    Scacchiera.board[0][i].pezzo=Pawn("N", (Scacchiera.board[0][i].xtot, Scacchiera.board[0][i].ytot))
    Scacchiera.pezzi.append(Scacchiera.board[0][i].pezzo)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        
    Scacchiera.draw()
        

    pygame.display.update()
    clock.tick(fps)
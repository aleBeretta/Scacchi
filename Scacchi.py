import pygame, sys
from pygame.locals import *
pygame.init()
WINDOW_SIZE=(1200,680)
screen=pygame.display.set_mode(WINDOW_SIZE)
screen.fill((240,240,180))
pygame.display.set_caption("Scacchi")


clock=pygame.time.Clock()
fps=60

print("prova")      

class Square:
    def __init__(self, x, y, larg, alt, pezzo=None) -> None:
        self.larg=larg
        self.alt=alt

        self.x=x
        self.xtot=x*larg+344
        
        self.y=y
        self.ytot=y*alt+84

        self.coord=(self.xtot,self.ytot)

        self.color="light" if (x+y)%2==0 else "dark"
        self.norm_color=(245, 237, 198) if self.color=="light" else(75,37,17)
        
        self.rect=pygame.Rect(self.xtot, self.ytot, self.larg, self.alt)


    def draw(self):
        pygame.draw.rect(screen, self.norm_color, self.rect)            



class Pawn:
    def __init__(self, colore, coord) -> None:
        self.colore=colore
        self.coord=coord
        self.pos=(self.coord[1]*64+344, self.coord[0]*64+84)
        self.image=pygame.image.load("pb.png").convert_alpha() if self.colore=="B" else pygame.image.load("pn.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=64
        self.rect.height=64
        self.image=pygame.transform.scale(self.image,(64,64))
    
    def draw(self):
        screen.blit(self.image, self.rect)

    

class King:
    def __init__(self, colore, coord) -> None:
        self.colore=colore
        self.coord=coord
        self.pos=(self.coord[1]*64+344, self.coord[0]*64+84)
        self.image=pygame.image.load("reb.png").convert_alpha() if self.colore=="B" else pygame.image.load("ren.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=64
        self.rect.height=64
        self.image=pygame.transform.scale(self.image,(64,64))
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Queen:
    def __init__(self, colore, coord) -> None:
        self.colore=colore
        self.coord=coord
        self.pos=(self.coord[1]*64+344, self.coord[0]*64+84)
        self.image=pygame.image.load("regb.png").convert_alpha() if self.colore=="B" else pygame.image.load("regn.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=64
        self.rect.height=64
        self.image=pygame.transform.scale(self.image,(64,64))
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Bishop:
    def __init__(self, colore, coord) -> None:
        self.colore=colore
        self.coord=coord
        self.pos=(self.coord[1]*64+344, self.coord[0]*64+84)
        self.image=pygame.image.load("ab.png").convert_alpha() if self.colore=="B" else pygame.image.load("an.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=64
        self.rect.height=64
        self.image=pygame.transform.scale(self.image,(64,64))
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Knight:
    def __init__(self, colore, coord) -> None:
        self.colore=colore
        self.coord=coord
        self.pos=(self.coord[1]*64+344, self.coord[0]*64+84)
        self.image=pygame.image.load("cb.png").convert_alpha() if self.colore=="B" else pygame.image.load("cn.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=64
        self.rect.height=64
        self.image=pygame.transform.scale(self.image,(64,64))
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Rook:
    def __init__(self, colore, coord) -> None:
        self.colore=colore
        self.coord=coord
        self.pos=(self.coord[1]*64+344, self.coord[0]*64+84)
        self.image=pygame.image.load("tb.png").convert_alpha() if self.colore=="B" else pygame.image.load("tn.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=self.pos)
        self.rect.width=64
        self.rect.height=64
        self.image=pygame.transform.scale(self.image,(64,64))
    
    def draw(self):
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
# Scacchiera.board[0][0].pezzo, Scacchiera.board[0][7].pezzo=Rook("N", Scacchiera.board[0][0].coord), Rook("N", Scacchiera.board[0][7].coord)
# Scacchiera.board[7][0].pezzo, Scacchiera.board[7][7].pezzo=Rook("B", Scacchiera.board[7][0].coord), Rook("B", Scacchiera.board[7][7].coord)
# Scacchiera.board[0][1].pezzo, Scacchiera.board[0][6].pezzo=Knight("N", Scacchiera.board[0][1].coord), Knight("N", Scacchiera.board[0][6].coord)
# Scacchiera.board[7][1].pezzo, Scacchiera.board[7][6].pezzo=Knight("B", Scacchiera.board[7][1].coord), Knight("B", Scacchiera.board[7][6].coord)
# Scacchiera.board[0][2].pezzo, Scacchiera.board[0][5].pezzo=Bishop("N", Scacchiera.board[0][2].coord), Bishop("N", Scacchiera.board[0][5].coord)
# Scacchiera.board[7][2].pezzo, Scacchiera.board[7][5].pezzo=Bishop("B", Scacchiera.board[7][2].coord), Bishop("B", Scacchiera.board[7][5].coord)
# Scacchiera.board[0][3].pezzo, Scacchiera.board[0][4].pezzo=Queen("N", Scacchiera.board[0][3].coord), King("N", Scacchiera.board[0][4].coord)
# Scacchiera.board[7][3].pezzo, Scacchiera.board[7][4].pezzo=Queen("B", Scacchiera.board[7][3].coord), King("B", Scacchiera.board[7][4].coord)
# for i in range(8):
#     Scacchiera.board[1][i].pezzo=Pawn("N", Scacchiera.board[1][i].coord)
#     Scacchiera.board[6][i].pezzo=Pawn("B", Scacchiera.board[6][i].coord)
#     Scacchiera.pezzi.append(Scacchiera.board[1][i].pezzo)
#     Scacchiera.pezzi.append(Scacchiera.board[6][i].pezzo)
#     Scacchiera.pezzi.append(Scacchiera.board[0][i].pezzo)
#     Scacchiera.pezzi.append(Scacchiera.board[7][i].pezzo)

for i in range(8):
    Scacchiera.pezzi.append(Pawn("N", (1,i)))
    Scacchiera.pezzi.append(Pawn("B", (6,i)))
Scacchiera.pezzi.append(Rook("N", (0, 0)))
Scacchiera.pezzi.append(Rook("N", (0, 7)))
Scacchiera.pezzi.append(Rook("B", (7, 0)))
Scacchiera.pezzi.append(Rook("B", (7, 7)))
Scacchiera.pezzi.append(Knight("N", (0, 1)))
Scacchiera.pezzi.append(Knight("N", (0, 6)))
Scacchiera.pezzi.append(Knight("B", (7, 1)))
Scacchiera.pezzi.append(Knight("B", (7, 6)))
Scacchiera.pezzi.append(Bishop("N", (0, 2)))
Scacchiera.pezzi.append(Bishop("N", (0, 5)))
Scacchiera.pezzi.append(Bishop("B", (7, 2)))
Scacchiera.pezzi.append(Bishop("B", (7, 5)))
Scacchiera.pezzi.append(King("N", (0, 4)))
Scacchiera.pezzi.append(King("B", (7, 4)))
Scacchiera.pezzi.append(Queen("N", (0, 3)))
Scacchiera.pezzi.append(Queen("B", (7, 3)))





while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            pos = pygame.mouse.get_pos()
            for pezzo in Scacchiera.pezzi:
                if pezzo.rect.collidepoint(pos):
                   pass

    Scacchiera.draw()


    
    
    pygame.display.update()
    clock.tick(fps)
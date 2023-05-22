import pygame
import sys
from pygame.locals import *
pygame.init()
WINDOW_SIZE = (1200, 680)
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill((240, 240, 180))
pygame.display.set_caption("Scacchi")


clock = pygame.time.Clock()
fps = 60



class Board:
    def __init__(self, screen, size) -> None:
        self.board = [[Square(c, r, 64, 64) for c in range(8)]
                      for r in range(8)]
        self.size=size
        self.pezzi = []
        self.image=pygame.Surface(size)
        x = screen.get_width() // 2 - size[0] // 2
        y = screen.get_height() // 2 - size[1] // 2
        self.rect=pygame.Rect(x, y, size[0], size[1])

    def inizializza(self):
        for i in range(8):
            self.pezzi.append(Pawn("N", (1, i)))
            self.pezzi.append(Pawn("B", (6, i)))
        self.pezzi.append(Rook("N", (0, 0)))
        self.pezzi.append(Rook("N", (0, 7)))
        self.pezzi.append(Rook("B", (7, 0)))
        self.pezzi.append(Rook("B", (7, 7)))
        self.pezzi.append(Knight("N", (0, 1)))
        self.pezzi.append(Knight("N", (0, 6)))
        self.pezzi.append(Knight("B", (7, 1)))
        self.pezzi.append(Knight("B", (7, 6)))
        self.pezzi.append(Bishop("N", (0, 2)))
        self.pezzi.append(Bishop("N", (0, 5)))
        self.pezzi.append(Bishop("B", (7, 2)))
        self.pezzi.append(Bishop("B", (7, 5)))
        self.pezzi.append(King("N", (0, 4)))
        self.pezzi.append(King("B", (7, 4)))
        self.pezzi.append(Queen("N", (0, 3)))
        self.pezzi.append(Queen("B", (7, 3)))        

    def draw(self):
        for r in range(8):
            for c in range(8):
                self.board[r][c].draw()
        screen.blit(self.image, self.rect)



class Square:
    def __init__(self, board, x, y, larg, alt, pezzo=None) -> None:
        self.larg = larg
        self.alt = alt

        self.x = x
        self.xtot = x*larg+344

        self.y = y
        self.ytot = y*alt+84

        self.coord = (self.xtot, self.ytot)

        self.color = "light" if (x+y) % 2 == 0 else "dark"
        self.norm_color = (245, 237, 198) if self.color == "light" else (75, 37, 17)

        self.image=pygame.Surface((self.larg, self.alt))
        self.rect = pygame.Rect(self.xtot, self.ytot, self.larg, self.alt)
        self.pezzo = pezzo

        self.board=board

    def draw(self):
        self.image.fill(self.color)
        self.pezzo.draw()
        self.board.image.blit(self.image, self.rect)

    def drawcircle(self):
        colore = (0, 65, 10)
        raggio = 15
        print(self.rect.center)
        pygame.draw.circle(screen, colore, self.rect.center, raggio)


class Pawn:
    def __init__(self, colore, square) -> None:
        self.colore = colore
        self.square=square
        self.coord=(self.square.x, self.square.y)
        self.pos = self.square.coord
        self.image = pygame.image.load("pb.png").convert_alpha() if self.colore == "B" else pygame.image.load("pn.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect.width = 64
        self.rect.height = 64
        self.image = pygame.transform.scale(self.image, (64, 64))

    def draw(self):
        screen.blit(self.image, self.rect)

    def showmoves(self):
        possmoves = []
        if self.colore == "N":
            if Scacchiera.board[self.coord[0]+1][self.coord[1]].pezzo == None:
                possmoves.append(Scacchiera.board[self.coord[0]+1][self.coord[1]])
        else:
            if Scacchiera.board[self.coord[0]-1][self.coord[1]].pezzo == None:
                possmoves.append(Scacchiera.board[self.coord[0]-1][self.coord[1]])
        
        for move in possmoves:
            move.drawcircle()
        return possmoves


class King:
    def __init__(self, colore, coord) -> None:
        self.colore = colore
        self.coord = coord
        self.pos = (self.coord[1]*64+344, self.coord[0]*64+84)
        self.image = pygame.image.load("reb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("ren.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect.width = 64
        self.rect.height = 64
        self.image = pygame.transform.scale(self.image, (64, 64))

    def draw(self):
        screen.blit(self.image, self.rect)


class Queen:
    def __init__(self, colore, coord) -> None:
        self.colore = colore
        self.coord = coord
        self.pos = (self.coord[1]*64+344, self.coord[0]*64+84)
        self.image = pygame.image.load("regb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("regn.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect.width = 64
        self.rect.height = 64
        self.image = pygame.transform.scale(self.image, (64, 64))

    def draw(self):
        screen.blit(self.image, self.rect)


class Bishop:
    def __init__(self, colore, coord) -> None:
        self.colore = colore
        self.coord = coord
        self.pos = (self.coord[1]*64+344, self.coord[0]*64+84)
        self.image = pygame.image.load("ab.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("an.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect.width = 64
        self.rect.height = 64
        self.image = pygame.transform.scale(self.image, (64, 64))

    def draw(self):
        screen.blit(self.image, self.rect)


class Knight:
    def __init__(self, colore, coord) -> None:
        self.colore = colore
        self.coord = coord
        self.pos = (self.coord[1]*64+344, self.coord[0]*64+84)
        self.image = pygame.image.load("cb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("cn.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect.width = 64
        self.rect.height = 64
        self.image = pygame.transform.scale(self.image, (64, 64))

    def draw(self):
        screen.blit(self.image, self.rect)


class Rook:
    def __init__(self, colore, coord) -> None:
        self.colore = colore
        self.coord = coord
        self.pos = (self.coord[1]*64+344, self.coord[0]*64+84)
        self.image = pygame.image.load("tb.png").convert_alpha() if self.colore == "B" else pygame.image.load("tn.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect.width = 64
        self.rect.height = 64
        self.image = pygame.transform.scale(self.image, (64, 64))

    def draw(self):
        screen.blit(self.image, self.rect)





Scacchiera = Board()

for pezzo in Scacchiera.pezzi:
    Scacchiera.board[pezzo.coord[0]][pezzo.coord[1]].pezzo = pezzo


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for pezzo in Scacchiera.pezzi:
                if pezzo.rect.collidepoint(pos):
                    possmoves = pezzo.showmoves()

    Scacchiera.draw()

    pygame.display.update()
    clock.tick(fps)

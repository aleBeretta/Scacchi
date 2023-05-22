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
        self.board = [[Square(self, c, r, size[0]/8, size[1]/8) for c in range(8)]
                      for r in range(8)]
        self.size = size
        self.image = pygame.Surface(size)
        x = screen.get_width() // 2 - size[0] // 2
        y = screen.get_height() // 2 - size[1] // 2
        self.rect = pygame.Rect(x, y, size[0], size[1])

    def inizializza(self):
        for i in range(8):
            self.board[1][i].pezzo = Pawn("N", self.board[1][i])
            self.board[6][i].pezzo = Pawn("B", self.board[6][i])
        self.board[0][0].pezzo, self.board[0][7].pezzo=Rook("N", self.board[0][0]), Rook("N", self.board[0][7])
        self.board[7][0].pezzo, self.board[7][7].pezzo=Rook("B", self.board[7][0]), Rook("B", self.board[7][7])
        self.board[0][1].pezzo, self.board[0][6].pezzo=Knight("N", self.board[0][1]), Knight("N", self.board[0][6])
        self.board[7][1].pezzo, self.board[7][6].pezzo=Knight("B", self.board[7][1]), Knight("B", self.board[7][6])
        self.board[0][2].pezzo, self.board[0][5].pezzo=Bishop("N", self.board[0][2]), Bishop("N", self.board[0][5])
        self.board[7][2].pezzo, self.board[7][5].pezzo=Bishop("B", self.board[7][2]), Bishop("B", self.board[7][5])
        self.board[0][3].pezzo, self.board[0][4].pezzo=King("N", self.board[0][3]), Queen("N", self.board[0][4])
        self.board[7][3].pezzo, self.board[7][4].pezzo=King("B", self.board[7][3]), Queen("B", self.board[7][4])


    def draw(self):
        for r in range(8):
            for c in range(8):
                self.board[r][c].draw()
        screen.blit(self.image, self.rect)


class Square:
    def __init__(self, board, x, y, larg, alt, pezzo=None, cerchio=False) -> None:
        self.larg = larg
        self.alt = alt

        self.x = x
        self.xtot = x*larg

        self.y = y
        self.ytot = y*alt

        self.coord = (x, y)
        self.pos = (self.xtot, self.ytot)

        self.color = "light" if (x+y) % 2 == 0 else "dark"
        self.norm_color = (
            245, 237, 198) if self.color == "light" else (75, 37, 17)

        self.image = pygame.Surface((self.larg, self.alt))
        self.rect = pygame.Rect(self.xtot, self.ytot, self.larg, self.alt)
        self.pezzo = pezzo

        self.board = board
        self.cerchio = cerchio

    def draw(self):
        self.image.fill(self.norm_color)
        if self.pezzo != None:
            self.pezzo.draw()
        if self.cerchio:
            pygame.draw.circle(self.image, (0, 65, 10),
                               (self.larg/2, self.alt/2), 15)
        self.board.image.blit(self.image, self.rect)


class Pawn:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = self.square.pos
        self.coord = self.square.coord
        self.image = pygame.image.load("pb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("pn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    # def showmoves(self):
    #     possmoves = []
    #     if self.colore == "N":
    #         if Scacchiera.board[self.coord[0]+1][self.coord[1]].pezzo == None:
    #             possmoves.append(
    #                 Scacchiera.board[self.coord[0]+1][self.coord[1]])
    #     else:
    #         if Scacchiera.board[self.coord[0]-1][self.coord[1]].pezzo == None:
    #             possmoves.append(
    #                 Scacchiera.board[self.coord[0]-1][self.coord[1]])

    #     for move in possmoves:
    #         move.drawcircle()
    #     return possmoves


class King:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = self.square.pos
        self.coord = self.square.coord
        self.image = pygame.image.load("reb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("ren.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        (self.pos)
        self.square.image.blit(self.image, self.rect)


class Queen:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = self.square.pos
        self.coord = self.square.coord
        self.image = pygame.image.load("regb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("regn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)


class Bishop:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = self.square.pos
        self.coord = self.square.coord
        self.image = pygame.image.load("ab.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("an.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)


class Knight:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = self.square.pos
        self.coord = self.square.coord
        self.image = pygame.image.load("cb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("cn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)


class Rook:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = self.square.pos
        self.coord = self.square.coord
        self.image = pygame.image.load("tb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("tn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)


Scacchiera = Board(screen, (512, 512))

Scacchiera.inizializza()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    #     pos = pygame.mouse.get_pos()
    #     for pezzo in Scacchiera.pezzi:
    #         if pezzo.rect.collidepoint(pos):
    #             possmoves = pezzo.showmoves()

    Scacchiera.draw()

    pygame.display.update()
    clock.tick(fps)

import pygame
import sys
from pygame.locals import *
pygame.init()
pygame.font.init()
WINDOW_SIZE = (1200, 680)
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill((240, 240, 180))
pygame.display.set_caption("Scacchi")


clock = pygame.time.Clock()
fps = 60


disegnaschermo=True


Font=pygame.font.SysFont("Calibri", 80)
FontBottone=pygame.font.SysFont("Calibri", 30)
class Bottone:
    def __init__(self, surf, pos, dim, scritta):
        self.surf=surf
        self.dim=list(dim)
        self.pos=list(pos)

        self.scritta=FontBottone.render(scritta, True, "White")
        self.rect=pygame.Rect(pos[0], pos[1], dim[0], dim[1])
    

    def disegna(self):
        self.surf.blit(self.scritta, (self.pos[0]+self.dim[1]//10, self.pos[1]+self.dim[1]//2))


class Schermata:
    def __init__(self, surf) -> None:
        self.surf=surf

        self.d = pygame.image.load('scacchi_image.webp').convert() 
        self.d = pygame.transform.scale(self.d, (1200, 680))
        self.rect_d = self.d.get_rect()
        self.scritta1=Font.render("Chess", True, "White")
        self.scrittarect1=pygame.Rect(self.surf.get_width()//2-100, self.surf.get_height()//2-150, 600, 300)

        self.bottone=Bottone(self.surf, (self.surf.get_width()//2-230, self.surf.get_height()//2), (300,200), "Clicca in qualsiasi punto per giocare")
    def disegna(self):
        self.surf.blit(self.d, self.rect_d)
        self.bottone.disegna()
        self.surf.blit(self.scritta1, self.scrittarect1)

class Schermata_finale:
    def __init__(self, surf, vincente=None) -> None:
        self.surf=surf
        self.surf.fill("Black")
        if vincente=="B":
            self.vincente="bianco"
        elif vincente=="N":
            self.vincente="nero"
        else:
            self.vincente="bel giuoco"
        self.scritta1=Font.render(f"Ha vinto il {self.vincente}", True, "White")
        self.scrittarect1=pygame.Rect(self.surf.get_width()//2-100, self.surf.get_height()//2-150, 600, 300)

        self.bottone=Bottone(self.surf, (self.surf.get_width()//2-230, self.surf.get_height()//2), (300,200), "Clicca in qualsiasi punto per giocare ancora")
    def disegna(self):
        self.surf.fill("Black")
        self.bottone.disegna()
        self.surf.blit(self.scritta1, self.scrittarect1)

schermo=Schermata(screen)
schermofinale=Schermata_finale(screen)
class Board:
    def __init__(self, screen, size) -> None:
        self.board = [[Square(self, y, x, size[0]/8, size[1]/8) for x in range(8)]
                      for y in range(8)]
        self.size = size
        self.image = pygame.Surface(size)
        self.x = screen.get_width() // 2 - size[0] // 2
        self.y = screen.get_height() // 2 - size[1] // 2
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])


        self.possmoves = []
        self.casellaprec = None

        self.mossa = 0
        self.scacco=False
        self.matto=False
    def inizializza(self):
        self.possmoves = []
        self.casellaprec = None

        self.mossa = 0
        self.scacco=False
        self.matto=False
        for i in range(8):
            self.board[i][1].pezzo = Pawn("N", self.board[i][1])
            self.board[i][6].pezzo = Pawn("B", self.board[i][6])
        self.board[0][0].pezzo, self.board[7][0].pezzo = Rook(
            "N", self.board[0][0]), Rook("N", self.board[7][0])
        self.board[0][7].pezzo, self.board[7][7].pezzo = Rook(
            "B", self.board[0][7]), Rook("B", self.board[7][7])
        self.board[1][0].pezzo, self.board[6][0].pezzo = Knight(
            "N", self.board[1][0]), Knight("N", self.board[6][0])
        self.board[1][7].pezzo, self.board[6][7].pezzo = Knight(
            "B", self.board[1][7]), Knight("B", self.board[6][7])
        self.board[2][0].pezzo, self.board[5][0].pezzo = Bishop(
            "N", self.board[2][0]), Bishop("N", self.board[5][0])
        self.board[2][7].pezzo, self.board[5][7].pezzo = Bishop(
            "B", self.board[2][7]), Bishop("B", self.board[5][7])
        self.board[3][0].pezzo, self.board[4][0].pezzo = King(
            "N", self.board[3][0]), Queen("N", self.board[4][0])
        self.board[3][7].pezzo, self.board[4][7].pezzo = King(
            "B", self.board[3][7]), Queen("B", self.board[4][7])

    def draw(self):
        screen.fill((240, 240, 180))
        if self.mossa%2==0:
            for x in range(8):
                for y in range(8):
                    self.board[x][y].pos=[self.board[x][y].xtot, y*self.board[x][y].larg]
                    self.board[x][y].rect.top=y*self.board[x][y].larg
                    self.board[x][y].draw()
        else:
            for x in range(8):
                for y in range(8):
                    self.board[x][y].pos=[self.board[x][y].xtot, (7-y)*self.board[x][y].larg]
                    self.board[x][y].rect.top=(7-y)*self.board[x][y].larg
                    self.board[x][y].draw()
        screen.blit(self.image, self.rect)


    def controllascacco(self, cond=False):
        casellescacco=[]
        self.scacco=False
        if self.mossa%2==0:
            colore="B" 
        else:
            colore="N"

        xre = None

        for linea in Scacchiera.board:
            for casella in linea:
                if type(casella.pezzo)==King and casella.pezzo.colore==colore:
                    xre=casella.coord[0]
                    yre=casella.coord[1]

        if xre != None:
            x=xre+1
            y=yre
            while x<8:
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Rook or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                x+=1

            x=xre-1
            y=yre
            while x>=0:
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Rook or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                x-=1

            x=xre
            y=yre+1
            while y<8:
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Rook or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                y+=1


            x=xre
            y=yre-1
            while y>=0:
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Rook or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                y-=1



            x=xre+1
            y=yre+1
            while x<8 and y<8 :
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Bishop or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                x+=1
                y+=1


            x=xre-1
            y=yre+1
            while x>=0 and y<8 :
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Bishop or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                x-=1
                y+=1

            
            x=xre+1
            y=yre-1
            while x<8 and y>=0:
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Bishop or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                x+=1
                y-=1


            x=xre-1
            y=yre-1
            while x>=0 and y>=0:
                casella=Scacchiera.board[x][y]
                if casella.pezzo!=None and casella.pezzo.colore==colore:
                    break
                if casella.pezzo!=None and casella.pezzo.colore!=colore:
                    if type(casella.pezzo)==Bishop or type(casella.pezzo)==Queen:
                        self.scacco=True
                        casellescacco.append(casella.coord)
                        break
                    else:
                        break
                x-=1
                y-=1

            mossecavallo=[]
            aggiuntamosse=[(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
            for (u, v) in aggiuntamosse:
                if xre+u>=0 and xre+u<8 and yre+v>=0 and yre+v<8:
                    mossecavallo.append((Scacchiera.board[xre+u][yre+v]))

            for casella in mossecavallo:
                if casella.pezzo!=None and type(casella.pezzo)==Knight and casella.pezzo.colore!=colore:
                    self.scacco=True
                    casellescacco.append(casella.coord)
                    break

            mossere=[]
            aggiuntamosse=[(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for (u, v) in aggiuntamosse:
                if xre+u>=0 and xre+u<8 and yre+v>=0 and yre+v<8:
                    mossere.append((Scacchiera.board[xre+u][yre+v]))

            for casella in mossere:
                if casella.pezzo!=None and type(casella.pezzo)==King and casella.pezzo.colore!=colore:
                    self.scacco=True
                    casellescacco.append(casella.coord)
                    break


            if colore=="N":
                if xre-1>=0 and xre-1<=7 and yre+1>=0 and yre+1<=7:
                    if Scacchiera.board[xre-1][yre+1].pezzo!=None and type(Scacchiera.board[xre-1][yre+1].pezzo)==Pawn and Scacchiera.board[xre-1][yre+1].pezzo.colore!=colore:
                        self.scacco=True
                        casellescacco.append((xre-1, yre+1))
                
                if xre+1>=0 and xre+1<=7 and yre+1>=0 and yre+1<=7:
                    if Scacchiera.board[xre+1][yre+1].pezzo!=None and type(Scacchiera.board[xre+1][yre+1].pezzo)==Pawn and Scacchiera.board[xre+1][yre+1].pezzo.colore!=colore:
                        self.scacco=True
                        casellescacco.append((xre+1, yre+1))

            if colore=="B":
                if xre-1>=0 and xre-1<=7 and yre-1>=0 and yre-1<=7:
                    if Scacchiera.board[xre-1][yre-1].pezzo!=None and type(Scacchiera.board[xre-1][yre-1].pezzo)==Pawn and Scacchiera.board[xre-1][yre-1].pezzo.colore!=colore:
                        self.scacco=True
                        casellescacco.append((xre-1, yre-1))
                
                if xre+1>=0 and xre+1<=7 and yre-1>=0 and yre-1<=7:
                    if Scacchiera.board[xre+1][yre-1].pezzo!=None and type(Scacchiera.board[xre+1][yre-1].pezzo)==Pawn and Scacchiera.board[xre+1][yre-1].pezzo.colore!=colore:
                        self.scacco=True
                        casellescacco.append((xre+1, yre-1))


    def controllamatto(self):
        if self.controllascacco():
            colore="B" if self.mossa%2==0 else "N"
            for linea in Scacchiera.board:
                for casella in linea:
                    if casella.pezzo!=None and casella.pezzo.colore==colore:
                        for mossa in casella.pezzo.showmoves():
                            pezzo_arrivo=mossa.pezzo
                            mossa.pezzo=casella.pezzo
                            casella.pezzo=None
                            mossa.pezzo.square=mossa
                            mossa.pezzo.coord=mossa.coord
                            if not self.controllascacco():
                                casella.pezzo=mossa.pezzo
                                mossa.pezzo=pezzo_arrivo
                                casella.pezzo.square=casella
                                casella.pezzo.coord=casella.coord
                                return False
                            
                            else:
                                casella.pezzo=mossa.pezzo
                                mossa.pezzo=pezzo_arrivo
                                casella.pezzo.square=casella
                                casella.pezzo.coord=casella.coord
            return True
        
        return False
    

    def controllapatta(self):
        totmosse=[]
        colore="B" if self.mossa%2==0 else "N"
        if not self.controllascacco():
            for linea in self.board:
                for casella in linea:
                    if casella.pezzo!=None and casella.pezzo.colore==colore:
                        totmosse+=casella.pezzo.showmoves()


        if len(totmosse)==0:
            return True

    def move(self, pos):
        colore = "B" if self.mossa % 2 == 0 else "N"
        newpos = [pos[0]-self.x, pos[1]-self.y]
        for linea in self.board:
            for casella in linea:
                if casella.rect.collidepoint(newpos):
                    # se tocco su un pezzo senza avere già delle mosse
                    if casella.pezzo != None and len(self.possmoves) == 0 and casella.pezzo.colore == colore:
                        self.possmoves = casella.pezzo.showmoves()
                        if self.controllascacco():
                            for arrivo in self.possmoves:
                                pezzo_arrivo=arrivo.pezzo
                                arrivo.pezzo=casella.pezzo
                                casella.pezzo=None
                                arrivo.pezzo.square=arrivo
                                arrivo.pezzo.coord=arrivo.coord
                                if self.controllascacco(True):
                                    print(arrivo.coord)
                                    self.possmoves.remove(arrivo)
                                casella.pezzo=arrivo.pezzo
                                arrivo.pezzo=pezzo_arrivo
                                casella.pezzo.square=casella
                                casella.pezzo.coord=casella.coord
                                
                        self.casellaprec = casella
                        for arrivo in self.possmoves:
                            arrivo.cerchio = True

                    # se tocco nel vuoto senza muovere
                    if casella.pezzo == None and len(self.possmoves) > 0 and not casella in self.possmoves:
                        for arrivo in self.possmoves:
                            arrivo.cerchio = False
                        self.casellaprec = None
                        self.possmoves.clear()

                    # se tocco su un pezzo alleato
                    if casella.pezzo != None and len(self.possmoves) > 0 and not casella in self.possmoves and casella.pezzo.colore == colore:
                        if type(self.casellaprec.pezzo)==King and type(casella.pezzo)==Rook:
                            self.casellaprec.pezzo, casella.pezzo=casella.pezzo, self.casellaprec.pezzo
                            self.casellaprec.pezzo.coord, casella.pezzo.coord=self.casellaprec.coord,casella.coord
                            self.casellaprec.pezzo.coord, casella.pezzo.coord=self.casellaprec.coord,casella.coord

                        for arrivo in self.possmoves:
                            arrivo.cerchio = False
                        self.possmoves.clear()
                        self.casellaprec = casella
                        self.possmoves = casella.pezzo.showmoves()
                        if self.controllascacco():
                            for arrivo in self.possmoves:
                                pezzo_arrivo=arrivo.pezzo
                                arrivo.pezzo=casella.pezzo
                                casella.pezzo=None
                                arrivo.pezzo.square=arrivo
                                arrivo.pezzo.coord=arrivo.coord
                                if self.controllascacco(True):
                                    print(arrivo.coord)
                                    self.possmoves.remove(arrivo)
                                casella.pezzo=arrivo.pezzo
                                arrivo.pezzo=pezzo_arrivo
                                casella.pezzo.square=casella
                                casella.pezzo.coord=casella.coord
                                
                        self.casellaprec = casella
                        for arrivo in self.possmoves:
                            arrivo.cerchio = True

                    # se tocco nel vuoto muovendo
                    if casella.pezzo == None and len(self.possmoves) > 0 and casella in self.possmoves:
                        for arrivo in self.possmoves:
                            arrivo.cerchio = False
                        casella.pezzo = self.casellaprec.pezzo
                        casella.pezzo.coord = list(casella.coord)
                        casella.pezzo.square = casella
                        self.casellaprec.pezzo = None
                        self.casellaprec = None
                        self.possmoves.clear()

                        if type(casella.pezzo) == King or type(casella.pezzo) == Pawn or type(casella.pezzo)==Rook:
                            casella.pezzo.mosso = True
                        

                        self.mossa += 1
                        if self.controllamatto():
                            self.matto=True

                            


                    # se tocco su un pezzo nemico che può essere catturato
                    if casella.pezzo != None and len(self.possmoves) > 0 and casella in self.possmoves and casella.pezzo.colore != colore:
                        for arrivo in self.possmoves:
                            arrivo.cerchio = False
                        self.possmoves.clear()

                        casella.pezzo = self.casellaprec.pezzo
                        casella.pezzo.coord = list(casella.coord)
                        casella.pezzo.square = casella
                        self.casellaprec.pezzo = None
                        self.casellaprec = None
                        self.possmoves.clear()
                        if type(casella.pezzo) == King or type(casella.pezzo) == Pawn or type(casella.pezzo)==Rook:
                            casella.pezzo.mosso = True


                        self.mossa += 1
                        if self.controllamatto():
                            self.matto=True


class Square:
    def __init__(self, board, x, y, larg, alt, pezzo=None, cerchio=False) -> None:
        self.larg = larg
        self.alt = alt

        self.x = int(x)
        self.xtot = int(x*larg)

        self.y = int(y)
        self.ytot = int(y*alt)

        self.coord = [self.x, self.y]
        self.pos = [self.xtot, self.ytot]

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
        if self.cerchio and self.pezzo==None:
            pygame.draw.circle(self.image, (0, 65, 10),
                               (self.larg/2, self.alt/2), 15)      
        if self.cerchio and self.pezzo!=None:
            pygame.draw.circle(self.image, (0, 65, 10),
                               (self.larg//2, self.alt//2), self.alt//2, 5)  
        self.board.image.blit(self.image, self.rect)


class Pawn:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.mosso = False

        self.pos = list(self.square.pos)
        self.coord = list(self.square.coord)
        self.image = pygame.image.load("pb.png").convert_alpha() if self.colore == "B" else pygame.image.load("pn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    def showmoves(self):
        possmoves = []

        x = self.coord[0]
        y = self.coord[1]

        if self.colore == "N":
            if Scacchiera.board[x][y+1].pezzo == None:
                possmoves.append(Scacchiera.board[x][y+1])
            if x > 0:
                if Scacchiera.board[x-1][y+1].pezzo != None and Scacchiera.board[x-1][y+1].pezzo.colore != 'N':
                    possmoves.append(Scacchiera.board[x-1][y+1])
            if x < 7:
                if Scacchiera.board[x+1][y+1].pezzo != None and Scacchiera.board[x+1][y+1].pezzo.colore != 'N':
                    possmoves.append(Scacchiera.board[x+1][y+1])
            if not self.mosso and Scacchiera.board[x][y+1].pezzo == None and Scacchiera.board[x][y+2].pezzo == None:
                possmoves.append(Scacchiera.board[x][y+2])

        else:
            if Scacchiera.board[x][y-1].pezzo == None:
                possmoves.append(Scacchiera.board[x][y-1])
            if x > 0:
                if Scacchiera.board[x-1][y-1].pezzo != None and Scacchiera.board[x-1][y-1].pezzo.colore != 'B':
                    possmoves.append(Scacchiera.board[x-1][y-1])
            if x < 7:
                if Scacchiera.board[x+1][y-1].pezzo != None and Scacchiera.board[x+1][y-1].pezzo.colore != 'B':
                    possmoves.append(Scacchiera.board[x+1][y-1])
            if not self.mosso and Scacchiera.board[x][y-1].pezzo == None and Scacchiera.board[x][y-2].pezzo == None:
                possmoves.append(Scacchiera.board[x][y-2])

        return possmoves


class King:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.mosso = False

        self.pos = list(self.square.pos)
        self.coord = list(self.square.coord)
        self.image = pygame.image.load("reb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("ren.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    def showmoves(self):
        moves = []
        x = self.coord[0]
        y = self.coord[1]

        mosse_possibili = [(0, 1), (1, 0), (-1, 0), (0, -1),
                           (1, -1), (-1, 1), (1, 1), (-1, -1)]
        for (px, py) in mosse_possibili:
            x1 = x + px
            y1 = y + py
            if x1 >= 0 and x1 < 8 and y1 >= 0 and y1 < 8:
                square = Scacchiera.board[x1][y1]
                if square.pezzo == None or square.pezzo.colore != self.colore:
                    moves.append(square)

        if self.mosso==False:
            if type(Scacchiera.board[x+3][y].pezzo)==Rook and Scacchiera.board[x+3][y].pezzo.mosso==False and Scacchiera.board[x+1][y].pezzo==None and Scacchiera.board[x+2][y].pezzo==None:
                moves.append(Scacchiera.board[x+3][y])
            if type(Scacchiera.board[x-4][y].pezzo)==Rook and Scacchiera.board[x-4][y].pezzo.mosso==False and Scacchiera.board[x-1][y].pezzo==None and Scacchiera.board[x-2][y].pezzo==None and Scacchiera.board[x-3][y].pezzo==None:
                moves.append(Scacchiera.board[x-4][y])
        return moves


class Queen:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = list(self.square.pos)
        self.coord = list(self.square.coord)
        self.image = pygame.image.load("regb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("regn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    def showmoves(self):
        mosse = []
        x = self.coord[0]
        y = self.coord[1]

        i = x + 1
        j = y + 1

        while i >= 0 and j >= 0 and i < 8 and j < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i += 1
            j += 1

        i = x + 1
        j = y - 1
        while i < 8 and j >= 0 and i >= 0 and j < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i += 1
            j -= 1

        i = x - 1
        j = y + 1
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i -= 1
            j += 1

        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0 and j < 8 and i < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i -= 1
            j -= 1

        for i in range(x-1, -1, -1):
            if Scacchiera.board[i][y].pezzo == None:
                mosse.append((i, y))
            else:
                # per mangiare
                if Scacchiera.board[i][y].pezzo.colore != self.colore:
                    mosse.append((i, y))
                break

        for i in range(x+1, 8, 1):
            if Scacchiera.board[i][y].pezzo == None:
                mosse.append((i, y))
            else:
                # per mangiare
                if Scacchiera.board[i][y].pezzo.colore != self.colore:
                    mosse.append((i, y))
                break

        # verticale
        for i in range(y-1, -1, -1):
            if Scacchiera.board[x][i].pezzo == None:
                mosse.append((x, i))
            else:
                if Scacchiera.board[x][i].pezzo.colore != self.colore:
                    mosse.append((x, i))
                break

        for i in range(y+1, 8, 1):
            if Scacchiera.board[x][i].pezzo is None:
                mosse.append((x, i))
            else:
                if Scacchiera.board[x][i].pezzo.colore != self.colore:
                    mosse.append((x, i))
                break

        possmoves = [Scacchiera.board[i][j] for (i, j) in mosse]
        return possmoves


class Bishop:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = list(self.square.pos)
        self.coord = list(self.square.coord)
        self.image = pygame.image.load("ab.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("an.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    def showmoves(self):
        mosse = []
        x = self.coord[0]
        y = self.coord[1]

        i = x + 1
        j = y + 1

        while i >= 0 and j >= 0 and i < 8 and j < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i += 1
            j += 1

        i = x + 1
        j = y - 1
        while i < 8 and j >= 0 and i >= 0 and j < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i += 1
            j -= 1

        i = x - 1
        j = y + 1
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i -= 1
            j += 1

        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0 and j < 8 and i < 8:
            if Scacchiera.board[i][j].pezzo == None:
                mosse.append((i, j))
            else:
                if Scacchiera.board[i][j].pezzo.colore != self.colore:
                    mosse.append((i, j))
                break
            i -= 1
            j -= 1

        possmoves = [Scacchiera.board[i][j] for (i, j) in mosse]
        return possmoves


class Knight:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.pos = list(self.square.pos)
        self.coord = list(self.square.coord)
        self.image = pygame.image.load("cb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("cn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    def showmoves(self):
        mosse = []
        x = self.coord[0]
        y = self.coord[1]

        mosse_possibili = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                           (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for (px, py) in mosse_possibili:
            x1 = x + px
            y1 = y + py
            if x1 >= 0 and x1 < 8 and y1 >= 0 and y1 < 8:
                square = Scacchiera.board[x1][y1]
                if square.pezzo == None or square.pezzo.colore != self.colore:
                    mosse.append(square)

        return mosse


class Rook:
    def __init__(self, colore, square) -> None:
        self.colore = colore

        self.square = square

        self.mosso=False
        self.pos = list(self.square.pos)
        self.coord = list(self.square.coord)
        self.image = pygame.image.load("tb.png").convert_alpha(
        ) if self.colore == "B" else pygame.image.load("tn.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.square.larg, self.square.alt))
        self.rect = pygame.Rect(0, 0, self.square.larg, self.square.alt)

    def draw(self):
        self.square.image.blit(self.image, self.rect)

    def showmoves(self):
        mosse = []
        x = self.coord[0]
        y = self.coord[1]

        # orizzontale
        for i in range(x-1, -1, -1):
            if Scacchiera.board[i][y].pezzo == None:
                mosse.append((i, y))
            else:
                # per mangiare
                if Scacchiera.board[i][y].pezzo.colore != self.colore:
                    mosse.append((i, y))
                break

        for i in range(x+1, 8, 1):
            if Scacchiera.board[i][y].pezzo == None:
                mosse.append((i, y))
            else:
                # per mangiare
                if Scacchiera.board[i][y].pezzo.colore != self.colore:
                    mosse.append((i, y))
                break

        # verticale
        for i in range(y-1, -1, -1):
            if Scacchiera.board[x][i].pezzo is None:
                mosse.append((x, i))
            else:
                if Scacchiera.board[x][i].pezzo.colore != self.colore:
                    mosse.append((x, i))
                break

        for i in range(y+1, 8, 1):
            if Scacchiera.board[x][i].pezzo is None:
                mosse.append((x, i))
            else:
                if Scacchiera.board[x][i].pezzo.colore != self.colore:
                    mosse.append((x, i))
                break

        possmoves = [Scacchiera.board[i][j] for (i, j) in mosse]
        return possmoves


Scacchiera = Board(screen, (512, 512))

Scacchiera.inizializza()
fine = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = list(pygame.mouse.get_pos())
            disegnaschermo=False

            if Scacchiera.rect.collidepoint(pos):
                Scacchiera.move(pos)
            if Scacchiera.matto:
                if Scacchiera.mossa%2==0:
                    vincente="N"
                else:
                    vincente="B"
            if Scacchiera.controllapatta():
                vincente="Pareggio"
                
        if Scacchiera.matto or Scacchiera.controllapatta():
            fine=True
            if vincente=="N":
                schermofinale.vincente="nero"
            elif vincente=="B":
                schermofinale.vincente="bianco"
            else:
                schermofinale.vincente="bel giuoco"
            schermofinale.disegna()
        else:
            if not disegnaschermo:        
                Scacchiera.draw()
            else:
                schermo.disegna()


        if fine and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Scacchiera.inizializza()
            fine=False

    pygame.display.update()
    clock.tick(fps)

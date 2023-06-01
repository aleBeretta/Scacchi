import pygame

#pedone
def move_pedone(self, board):
    mosse = []
    x, y = self.pos

    if self.colore == 'B':
        if y > 0 and board[y-1][x].pezzo is None:
            mosse.append((x, y-1))
            if y == 6 and board[y-2][x].pezzo is None:
                mosse.append((x, y-2))
        #per mangiare
        if y > 0 and x > 0 and board[y-1][x-1].pezzo is not None:
            mosse.append((x-1, y-1))
        if y > 0 and x < 7 and board[y-1][x+1].pezzo is not None:
            mosse.append((x+1, y-1))

    elif self.colore == 'N':
        if y < 7 and board[y+1][x].pezzo is None:
            mosse.append((x, y+1))
            if y == 1 and board[y+2][x].pezzo is None:
                mosse.append((x, y+2))
        #per mangiare
        if y < 7 and x > 0 and board[y+1][x-1].pezzo is not None:
            mosse.append((x-1, y+1))
        if y < 7 and x < 7 and board[y+1][x+1].pezzo is not None:
            mosse.append((x+1, y+1))
    return mosse

#torre
def move_torre(self, board):
    mosse = []
    x, y = self.pos

    #orizzontale
    for i in range(x-1, -1, -1):
        if board[y][i].pezzo is None:
            mosse.append((i,y))
        else:
            #per mangiare
            if board[y][i].pezzo.colore != self.colore:
                mosse.append((i,y))
            break

    for i in range(x+1, 8):
        if board[y][i].pezzo is None:
            mosse.append((i,y))
        else:
            #per mangiare
            if board[y][i].pezzo.colore != self.colore:
                mosse.append((i,y))
            break
    
    #verticale
    for i in range(y-1, -1, -1):
        if board[i][x].pezzo is None:
            mosse.append((x, i))
        else:
            if board[i][x].pezzo.colore != self.colore:
                mosse.append((x, i))
            break
    
    for i in range(y+1, 8):
        if board[i][x].pezzo is None:
            mosse.append((x, i))
        else:
            if board[i][x].pezzo.colore != self.colore:
                mosse.append((x, i))
            break

    return mosse

#cavallo
def move_cavallo(self, board):
    mosse = []
    x, y = self.pos

    mosse_possibili = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)] 
    for px, py in mosse_possibili:
        x1 = x + px
        y1 = y + py
        if x1 >= 0 and x1 < 8 and y1 >= 0 and y1 < 8:
            square = board[x1][y1]
            if square.pezzo is None or square.pezzo.colore != self.colore:
                mosse.append(square)
    
    return mosse

#alfiere
def move_alfiere(self, board):
    mosse = []
    x, y = self.pos

    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i -= 1
        j -= 1

    i = x + 1
    j = y - 1
    while i < 8 and j >= 0:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i += 1
        j -= 1  

    i = x - 1
    j = y + 1
    while i >= 0 and j < 8:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i -= 1
        j += 1  
    
    i = x + 1
    j = y + 1
    while i >= 0 and j >= 0:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i += 1
        j += 1

#re
def move_re(self, board):
    mosse = []
    x, y = self.pos

    mosse_possibili = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y+1)]
    for mossa in mosse_possibili:
        i, j = mossa
        if i >= 0 and i < 8 and j >= 0 and j < 8:
            if board[j][i].pezzo is None or board[j][i].pezzo.colore != self.colore:
                mosse.append((i, j))
    return mosse

#regina
def move_regina(self, board):
    mosse = []
    x, y = self.pos

    #orizzontale
    for i in range(x-1, -1, -1):
        if board[y][i].pezzo is None:
            mosse.append((i,y))
        else:
            #per mangiare
            if board[y][i].pezzo.colore != self.colore:
                mosse.append((i,y))
            break

    for i in range(x+1, 8):
        if board[y][i].pezzo is None:
            mosse.append((i,y))
        else:
            #per mangiare
            if board[y][i].pezzo.colore != self.colore:
                mosse.append((i,y))
            break
    
    #verticale
    for i in range(y-1, -1, -1):
        if board[i][x].pezzo is None:
            mosse.append((x, i))
        else:
            if board[i][x].pezzo.colore != self.colore:
                mosse.append((x, i))
            break
    
    for i in range(y+1, 8):
        if board[i][x].pezzo is None:
            mosse.append((x, i))
        else:
            if board[i][x].pezzo.colore != self.colore:
                mosse.append((x, i))
            break
    
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i -= 1
        j -= 1

    i = x + 1
    j = y - 1
    while i < 8 and j >= 0:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i += 1
        j -= 1  

    i = x - 1
    j = y + 1
    while i >= 0 and j < 8:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i -= 1
        j += 1  
    
    i = x + 1
    j = y + 1
    while i >= 0 and j >= 0:
        if board[j][i].pezzo is None:
            mosse.append((i,j))
        else:
            if board[j][i].pezzo.colore != self.colore:
                mosse.append((i,j))
            break
        i += 1
        j += 1
    
    return mosse

#arrocco
def arrocco(board, pos_ini, pos_fin):
    if abs(pos_fin[1]-pos_ini[1]) == 2:
        if pos_fin[1] == 2:
            rook_pos_ini = (pos_ini[0], 7)
            rook_pos_fin = (pos_ini[0], 5)
        elif pos_fin[1] == 6:
            rook_pos_ini = (pos_ini[0], 0)
            rook_pos_fin = (pos_ini[0], 3)
        
        king = board[pos_ini[0]][pos_fin[0]]
        rook = board[rook_pos_ini[0]][rook_pos_ini[1]]

        board[pos_ini[0]][pos_ini[1]] = None
        board[pos_fin[0]][pos_fin[1]] = king 
        board[rook_pos_ini[0]][rook_pos_ini[1]] = None
        board[rook_pos_fin[0]][rook_pos_fin[1]] = rook

    return board
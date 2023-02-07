peiceMassList = []
board =     [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

def PrintBoard():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


class Piece:
    def __init__ (self, posX, posY, color, name):
        self.positionX = posX
        self.positionY = posY
        self.color    = color
        self.possibleMoves    = []
        self.name = name

    def GetXPosition(self):
        return self.positionX

    def GetYPosition(self):
        return self.positionY

    def GetColor(self):
        return self.color

    def GetMoves(self):
        return self.moves

    def SetPosition(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        board[self.positionY][self.positionX] = self.name

class Pawn(Piece):
    def __init__(self, posX, posY, color,  hasStarted, name):
        Piece.__init__(self, posX, posY, color, name)
        self.hasStarted = hasStarted

    def GetPossibleMoves(self):
        self.possibleMoves.clear()
        if not(self.hasStarted):
            self.hasStarted = True
            self.possibleMoves.append([[self.positionY + 1], self.positionX])
            self.possibleMoves.append([[self.positionY + 2], self.positionX])

        elif(self.hasStarted):
            self.possibleMoves.append([[self.positionY + 1], self.positionX])


class Knight(Piece):

    def GetPossibleMoves(self):
        return 0

class Bishop(Piece):

    def GetPossibleMoves(self):
        return 0

class Rook(Piece):

    def GetPossibleMoves(self):
        return 0

class Queen(Piece):

    def GetPossibleMoves(self):
        return 0

class King(Piece):
    def __init__(self, posX, posY, color, isChecked, name):
        Piece.__init__(self, posX, posY, color, name)
        self.isChecked = isChecked


# <editor-fold desc="Piece Objects and Setting">
######################BLACK###########################
bPawn1 =  Pawn(0, 1, 0, False, "bp1")
bPawn2 =  Pawn(1, 1, 0, False, "bp2")
bPawn3 =  Pawn(2, 1, 0, False, "bp3")
bPawn4 =  Pawn(3, 1, 0, False, "bp4")
bPawn5 =  Pawn(4, 1, 0, False, "bp5")
bPawn6 =  Pawn(5, 1, 0, False, "bp6")
bPawn7 =  Pawn(6, 1, 0, False, "bp7")
bPawn8 =  Pawn(7, 1, 0, False, "bp8")

bKnight1 =  Knight(1, 0, 0, "bk1")
bKnight2 =  Knight(6, 0, 0, "bk2")

bRook1 =  Rook(0, 0, 0, "br1")
bRook2 =  Knight(7, 0, 0, "br2")

bBishop1 =  Bishop(2, 0, 0, "bb1")
bBishop2 =  Bishop(5, 0, 0, "bb2")

bQueen =  Queen(3, 0, 0, "bq")

bKing =  King(4, 0, 0, False, "bking")
#############################################
######################WHITE###################
wPawn1 =  Pawn(0, 6, 0, False, "wp1")
wPawn2 =  Pawn(1, 6, 0, False, "wp2")
wPawn3 =  Pawn(2, 6, 0, False, "wp3")
wPawn4 =  Pawn(3, 6, 0, False, "wp4")
wPawn5 =  Pawn(4, 6, 0, False, "wp5")
wPawn6 =  Pawn(5, 6, 0, False, "wp6")
wPawn7 =  Pawn(6, 6, 0, False, "wp7")
wPawn8 =  Pawn(7, 6, 0, False, "wp8")

wKnight1 =  Knight(1, 7, 0, "wk1")
wKnight2 =  Knight(6, 7, 0, "wk2")

wRook1 =  Rook(0, 7, 0, "wr1")
wRook2 =  Knight(7, 7, 0, "wr2")

wBishop1 =  Bishop(2, 7, 0, "wb1")
wBishop2 =  Bishop(5, 7, 0, "wb2")

wQueen =  Queen(3, 7, 0, "wq")

wKing =  King(4, 7, False, 0, "wking")

#######################LIST#########################
peiceMassList.extend((bPawn1, bPawn2, bPawn3, bPawn4, bPawn5, bPawn6, bPawn7, bPawn8, bKnight1, bKnight2, bBishop1, bBishop2, bQueen, bKnight2, bRook1, bRook2, bKing))
peiceMassList.extend((wPawn1, wPawn2, wPawn3, wPawn4, wPawn5, wPawn6, wPawn7, wPawn8, wKnight1, wKnight2, wBishop1, wBishop2, wQueen, wKnight2, wRook1, wRook2, wKing))

for item in peiceMassList:
    item.SetPosition(item.GetXPosition(), item.GetYPosition())
# </editor-fold>


testBoard = [[bRook1.name, bKnight1.name, bBishop1.name, bQueen.name, bKing.name, bBishop2.name, bKnight2.name, bRook2.name],
         [bPawn1.name, bPawn2.name,   bPawn3.name,   bPawn4.name, bPawn5.name,bPawn6.name,   bPawn7.name,   bPawn8.name],
         [0,            0,         0,          0,        0,       0,          0,           0],
         [0,            0,         0,          0,        0,       0,          0,           0],
         [0,            0,         0,          0,        0,       0,          0,           0],
         [0,            0,         0,          0,        0,       0,          0,           0],
         [wPawn1.name, wPawn2.name,   wPawn3.name,   wPawn4.name, wPawn5.name, wPawn6.name,   wPawn7.name,   wPawn8.name],
         [wRook1.name, wKnight1.name, wBishop1.name, wQueen.name, wKing.name,  wBishop2.name, wKnight2.name, wRook2.name]
         ]


PrintBoard()




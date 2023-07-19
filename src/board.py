from const import *
from square import Square
from piece import Piece


class Board:

    def __init__(self):
         self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

         self._create()
     
    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        #pawns
        self.squares[row_pawn][col] = Square(row_pawn, col, Piece.Pawn(color))

        #kinghts
        self.squares[row_other][1] = Square(row_other, 1, Piece.Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Piece.Knight(color))

        #bishops
        self.squares[row_other][2] = Square(row_other, 2, Piece.Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Piece.Bishop(color))

        #rooks
        self.squares[row_other][0] = Square(row_other, 0, Piece.Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Piece.Rook(color))

        #queen
        self.squares[row_other][3] = Square(row_other, 3, Piece.Queen(color))

        #king
        self.squares[row_other][4] = Square(row_other, 4, Piece.King(color))
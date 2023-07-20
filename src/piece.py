import os

class Piece:

    def _init_(self, name, color, value, texture, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
        
    def add_move(self, move):
        self.moves.append(move)

    # Pawn class

    class Pawn(Piece):
        
        def _init_(self, color):
            if color == 'white':
                self.dir = -1 # white pawns move up the board
            else:
                self.dir = 1  # black pawns move down the board
                super()._init_('pawn', color, 1.0 ) # value moves for pawn is 1.0

    # Knight class
     
    class Knight(Piece):
        def _init_(self, color):
            super()._init_('knight', color, 3.0) # value for knight is 3.0

    #Bishop class
    
    class Bishop(Piece):
        def _init_(self, color):
            super()._init_('bishop', color, 3.0) # value for bishop is 3.0

    #Rook class
     
    class Rook(Piece):
        def _init_(self, color):
            super()._init_('rook', color, 5.0) # value for rook is 5.0

    #Queen class

    class Queen(Piece):
        def _init_(self, color):
            super()._init_('queen', color, 9.0) # value for queen is 9.0

    #King class

    class King(Piece):
        def _init_(self, color):
            super()._init_('king', color, 100000.0) # value for king is 0.0
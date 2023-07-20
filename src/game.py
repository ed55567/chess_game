import pygame

from const import *
from board import Board


class Game:

    def __init__(self):
        self.board = Board()

    # show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 237) # light
                else:
                    color = (119, 148, 85) # dark
                
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, rect)


    def show_pieces(self, surface, board):
        for row in range(ROWS):
            for col in range(COLS):
                
                if self.board.squares[row][col].piece:
                    piece = self.board.squares[row][col].piece
                    

                    img = pygame.image.load(piece.texture)
                    img_center = (col * SQ_SIZE + SQ_SIZE / 2, row * SQ_SIZE + SQ_SIZE / 2)
                    picee.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
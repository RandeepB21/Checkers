import pygame 
from .constants import RED, WHITE, GREY, YELLOW, SQUARE_SIZE 
 
class Piece: 
    PADDING = 15 
    OUTLINE = 2 
    def __init__(self, row, column, colour): 
        self.row = row 
        self.col = column 
        self.colour = colour 
        self.king = False 
        self.x = 0 
        self.y = 0 
        self.calculate_position() 
 

    def calculate_position(self): 
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 
 
 
    def make_king(self): 
        self.king = True 
 
 
    def draw(self, win): 
        radius = SQUARE_SIZE // 2 - self.PADDING 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) 
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius) 
 
        if self.king: 
            pygame.draw.circle(win, YELLOW, (self.x, self.y), radius // 2) 
 
 
    def move(self, row, col): 
        self.row = row 
        self.col = col 
        self.calculate_position() 
 

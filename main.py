import pygame 
from checkers.game import Game 
from checkers.constants import RED, WHITE, WIDTH, HEIGHT, SQUARE_SIZE 
from minimax.algorithm import minimax 
 
FPS = 60 
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Checkers") 
 
 
def get_row_column_from_mouse(position): 
    x, y = position 
    row = y // SQUARE_SIZE 
    col = x // SQUARE_SIZE 
    return row, col 
 
def main(): 
    run = True 
    clock = pygame.time.Clock() 
    game = Game(WIN) 
 
    while run:  
        clock.tick(FPS) 
 
        if game.turn == WHITE: 
           value, new_board = minimax(game.get_board(), 3, WHITE, game) 
           game.ai_move(new_board) 
 

        if game.winner() != None: 
            print(game.winner()) 
            run = False 
         
        for event in pygame.event.get(): 
 
            if event.type == pygame.QUIT: 
                run = False 
 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                position = pygame.mouse.get_pos() 
                row, col = get_row_column_from_mouse(position) 
                game.select(row, col) 
     
        game.update() 
 
    pygame.quit() 
     
if __name__ == "__main__": 
    main()

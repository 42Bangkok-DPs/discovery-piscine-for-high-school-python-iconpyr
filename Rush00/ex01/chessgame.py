#!/usr/bin/env python3
import pygame as pg
import sys

pg.init()

size = 150
width = height = size * 8
fps = 60

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Diddy fans chess board")

def draw_chessboard():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (66, 158, 157)
            pg.draw.rect(screen, color,
                        (col * size, row * size, size, size))
# draw pices onto board.
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * size + 17,
                                     white_locations[i][1] * size + 10))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * size + 10, white_locations[i][1] * size + 10))

            
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * size + 17,
                                     black_locations[i][1] * size + 10))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * size + 10,
                                     black_locations[i][1] * size + 10))




# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), 
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), 
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
captures_pieces_white = []
captures_pieces_black = []

# turn step and selection
turn_step = 0
selection = 100
valid = []
# set all stuff in to game include images
black_queen = pg.image.load('Rush00/ex01/img/queen_b.png')
black_queen = pg.transform.scale(black_queen, (150, 150))
black_queen_small = pg.transform.scale(black_queen, (45, 45))

black_pawn = pg.image.load('Rush00/ex01/img/pawn_b.png')
black_pawn = pg.transform.scale(black_pawn, (120, 120))
black_pawn_small = pg.transform.scale(black_pawn, (45, 45))

black_knight = pg.image.load('Rush00/ex01/img/knight_b.png')
black_knight = pg.transform.scale(black_knight, (150, 150))
black_knight_small = pg.transform.scale(black_knight, (45, 45))

black_king = pg.image.load('Rush00/ex01/img/king_b.png')
black_king = pg.transform.scale(black_king, (150, 150))
black_king_small = pg.transform.scale(black_king, (45, 45))

black_bishop = pg.image.load('Rush00/ex01/img/bishop_b.png')
black_bishop = pg.transform.scale(black_bishop, (150, 150))
black_bishop_small = pg.transform.scale(black_bishop, (45, 45))

black_rook = pg.image.load('Rush00/ex01/img/rook_b.png')
black_rook = pg.transform.scale(black_rook, (150, 150))
black_rook_small = pg.transform.scale(black_rook, (45, 45))

white_queen = pg.image.load('Rush00/ex01/img/queen_w.png')
white_queen = pg.transform.scale(white_queen, (150, 150))
white_queen_small = pg.transform.scale(white_queen, (45, 45))

white_pawn = pg.image.load('Rush00/ex01/img/pawn_w.png')
white_pawn = pg.transform.scale(white_pawn, (120, 120))
white_pawn_small = pg.transform.scale(white_pawn, (45, 45))

white_knight = pg.image.load('Rush00/ex01/img/knight_w.png')
white_knight = pg.transform.scale(white_knight, (150, 150))
white_knight_small = pg.transform.scale(white_knight, (45, 45))

white_king = pg.image.load('Rush00/ex01/img/king_w.png')
white_king = pg.transform.scale(white_king, (150, 150))
white_king_small = pg.transform.scale(white_king, (45, 45))

white_bishop = pg.image.load('Rush00/ex01/img/bishop_w.png')
white_bishop = pg.transform.scale(white_bishop, (150, 150))
white_bishop_small = pg.transform.scale(white_bishop, (45, 45))

white_rook = pg.image.load('Rush00/ex01/img/rook_w.png')
white_rook = pg.transform.scale(white_rook, (150, 150))
white_rook_small = pg.transform.scale(white_rook, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                       white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                       black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

def check_options():
    pass

def main():
    clock = pg.time.Clock()

    while True:
            draw_chessboard()
            draw_pieces()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captures_pieces_white.append(black_pieces[black_piece])
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid = []
                if turn_step > 1:
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid and selection != 100:
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captures_pieces_black.append(white_pieces[white_piece])
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid = []
            clock.tick(fps)

if __name__ == "__main__":
    main()

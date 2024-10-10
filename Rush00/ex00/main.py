board = [0] * 8

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


# check all pieces valid option on board
def check_option(pieces, location, turn):
    moves_list = []
    all_moves_list = []
    for i in range((pieces)):
        location = location[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(loation, turn)
    return all_moves_list

for i in range(len(board)):
    board[i] = ["__"] * 8

def print_board(board):
    for i, row in enumerate(board):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c"
           + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f"
             + " " * 2 + "g" + " " * 2 + "h")
    
print_board(board)
    
white_pieces_map = {
    "wP": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "wB": [(7,2), (7,5)],
    "wR": [(7,0), (7,7)],
    "wQ": [(7,3)],
    "wK": [(7,4)]
}

black_pieces_map = {
    "bP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (6, 7)],
    "bB": [(0,2), (0,5)],
    "bR": [(0,0), (0,7)],
    "bQ": [(0,3)],
    "bK": [(0,4)]
}

col_map ={
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

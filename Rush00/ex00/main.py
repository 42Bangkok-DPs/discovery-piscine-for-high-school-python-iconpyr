def create_empty_board(size):
    return [['.' for _ in range(size)] for _ in range(size)]

def print_board(board):
    output = ("  " + " ".join(map(str, range(len(board)))) + "\n")
    for i, row in enumerate(board):
        output += (f"{i} " + " ".join(row) + "\n")
    return output

def valid_pawn_moves(board, row, col):
    moves = []
    directions = [(-1, 1), (-1, -1)]  # Diagonal directions
    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < len(board) and 0 <= c < len(board):
            r += dr
            c += dc
            if 0 <= r < len(board) and 0 <= c < len(board):
                if board[r][c] == 'K':
                    return [(r, c)]

def valid_bishop_moves(board, row, col):
    moves = []
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions
    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < len(board) and 0 <= c < len(board):
            r += dr
            c += dc
            if 0 <= r < len(board) and 0 <= c < len(board):
                if board[r][c] == 'K':
                    return [(r, c)]
                elif board[r][c] != '.':
                    break  # Blocked by own piece
    return moves

def valid_rook_moves(board, row, col):
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Vertical and horizontal directions
    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < len(board) and 0 <= c < len(board):
            r += dr
            c += dc
            if 0 <= r < len(board) and 0 <= c < len(board):
                if board[r][c] == 'K':
                    return [(r, c)]
                elif board[r][c] != '.':
                    break  # Blocked by own piece
    return moves

def valid_queen_moves(board, row, col):
    return valid_rook_moves(board, row, col) + valid_bishop_moves(board, row, col)

def checkmate(board_str):
    board = [list(line) for line in board_str.strip().split('\n')]
    lines = board_str.strip().split('\n')
    board_size = len(lines)
    

    # Check the dimensions of the board
    if any(len(line) != board_size for line in lines):
        # print("Error")
        return "Error"

    for r in range(board_size):
        for c in range(board_size):
            board[r][c] = lines[r][c]



    # Find the King's position
    king_pos = None
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == 'K':
                king_pos = (r, c)


    if not king_pos:
        return "Fail"  # No King found
    


    # Check each piece's possible moves
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == 'P':
                if valid_pawn_moves(board, r, c):
                    return "Success"  # Pawn can capture King
            elif board[r][c] == 'B':
                if valid_bishop_moves(board, r, c):
                    return "Success"  # Bishop can capture King
            elif board[r][c] == 'R':
                if valid_rook_moves(board, r, c):
                    return "Success"  # Rook can capture King
            elif board[r][c] == 'Q':
                if valid_queen_moves(board, r, c):
                    return "Success"  # Queen can capture King

    return "Fail"  # King is not in check



def main():
    board1 = """\
R...
.K..
....
...B
"""
    print("Testing Board 1:")
    # print(print_board(create_empty_board(8)))  # Print empty board for clarity
    print(checkmate(board1))  

    
    board2 = """\
..P...
.K....
....K.
......
....K.
......
"""
    print("Testing Board 2:")
    # print(print_board(create_empty_board(8)))  # Print empty board for clarity
    print(checkmate(board2))  

    
    board3 = """\
........
...K....
.......P
..R.....
........
........
........
........
"""
    print("Testing Board 3:")
    # print(print_board(create_empty_board(8)))  # Print empty board for clarity
    print(checkmate(board3))  


if __name__ == "__main__":
    main()


def create_empty_board(size):
    return [['.' for _ in range(size)] for _ in range(size)]

def print_board(board):
    output = ("  " + " ".join(map(str, range(len(board)))) + "\n")
    for i, row in enumerate(board):
        output += (f"{i} " + " ".join(row) + "\n")
    return output

def valid_pawn_moves(board, row, col):
    moves = []
    # Capture diagonally
    if row < len(board) - 1:
        if col > 0 and board[row + 1][col - 1] == 'K':
            return [(row + 1, col - 1)]
        if col < len(board) - 1 and board[row + 1][col + 1] == 'K':
            return [(row + 1, col + 1)]
    return moves

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
    board = create_empty_board(8)
    lines = board_str.strip().split('\n')

    # Check the dimensions of the board
    if len(lines) != 8 or any(len(line) != 8 for line in lines):
        print("Error")

    for r in range(8):
        for c in range(8):
            board[r][c] = lines[r][c]

    # Find the King's position
    king_pos = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'K':
                king_pos = (r, c)

    if not king_pos:
        return "Fail"  # No King found

    # Check each piece's possible moves
    for r in range(8):
        for c in range(8):
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
R.......
.K......
........
...B....
........
........
........
........
"""
    print("Testing Board 1:")
    # print(print_board(create_empty_board(8)))  # Print empty board for clarity
    print(checkmate(board1))  

    
    board2 = """\
........
.K......
........
........
........
.Q......
........
........
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


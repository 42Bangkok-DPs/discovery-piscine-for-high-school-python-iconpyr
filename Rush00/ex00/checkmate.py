def find_king(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                return row, col
    return None

def is_in_bounds(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board)

def check_rook_or_queen(board, king_pos):
    row, col = king_pos
    
    # Check horizontal and vertical lines for Rook or Queen
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while is_in_bounds(board, r, c):
            if board[r][c] == 'R' or board[r][c] == 'Q':
                return True
            elif board[r][c] != '.': # If there's another piece, stop checking this direction
                break
            r, c = r + dr, c + dc
    return False

def check_bishop_or_queen(board, king_pos):
    row, col = king_pos
    
    # Check diagonals for Bishop or Queen
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] # Down-right, Down-left, Up-right, Up-left
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while is_in_bounds(board, r, c):
            if board[r][c] == 'B' or board[r][c] == 'Q':
                return True
            elif board[r][c] != '.': # If there's another piece, stop checking this direction
                break
            r, c = r + dr, c + dc
    return False

def check_pawns(board, king_pos):
    row, col = king_pos
    # Check for pawns
    directions = [(1, 1), (1, -1)] 
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if is_in_bounds(board, r, c) and board[r][c] == 'P':
            return True
    return False

def is_king_in_check(board):
    king_pos = find_king(board)
    
    if king_pos is None:
        return "Fail"  # No King found
    
    if (check_rook_or_queen(board, king_pos) or 
        check_bishop_or_queen(board, king_pos) or 
        check_pawns(board, king_pos)):
        return "Success"
    
    return "Fail"

# Example usage:
board = [
    ".......",
    "....K..",
    ".....B.",
    ".......",
    ".......",
]

result = is_king_in_check(board)
print(result)

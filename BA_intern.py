import random
import time


SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 1], [1, 0, 0]],  # L shape
    [[1, 1, 1], [0, 0, 1]],  # J shape
    [[1, 1, 0], [0, 1, 1]],  # S shape
    [[0, 1, 1], [1, 1, 0]]  # Z shape
]


BOARD_WIDTH = 10
BOARD_HEIGHT = 20

board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board():
    """Print the current state of the game board"""
    for row in board:
        print(''.join(['#' if cell else '.' for cell in row]))
    print()

def check_collision(shape, x, y):
    """Check if the current shape at the given position collides with the board"""
    for row_idx, row in enumerate(shape):
        for col_idx, cell in enumerate(row):
            if cell and (y + row_idx < 0 or y + row_idx >= BOARD_HEIGHT or x + col_idx < 0 or x + col_idx >= BOARD_WIDTH or board[y + row_idx][x + col_idx]):
                return True
    return False

def clear_lines():
    """Clear any completed lines on the board"""
    rows_to_remove = [row for row in range(BOARD_HEIGHT) if all(cell for cell in board[row])]
    if rows_to_remove:
        for row in reversed(rows_to_remove):
            board.pop(row)
            board.insert(0, [0] * BOARD_WIDTH)

def play_game():
    """Play the Tetris game until it's game over"""
    current_shape = random.choice(SHAPES)
    current_x, current_y = BOARD_WIDTH // 2 - len(current_shape[0]) // 2, 0

    while True:
        # Clear the board
        print_board()

        # Move the shape down
        if not check_collision(current_shape, current_x, current_y + 1):
            current_y += 1
        else:
            # Merge the shape with the board
            for row_idx, row in enumerate(current_shape):
                for col_idx, cell in enumerate(row):
                    if cell:
                        board[current_y + row_idx][current_x + col_idx] = cell

            # Clear any completed lines
            clear_lines()

            # Choose a new random shape
            current_shape = random.choice(SHAPES)
            current_x = BOARD_WIDTH // 2 - len(current_shape[0]) // 2
            current_y = 0

            # Check if the game is over
            if check_collision(current_shape, current_x, current_y):
                break

        time.sleep(0.5)

play_game()
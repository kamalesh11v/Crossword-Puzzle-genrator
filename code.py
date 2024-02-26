import random

def generate_grid(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def add_word_horizontal(grid, word, row, col):
    for i, letter in enumerate(word):
        grid[row][col + i] = letter

def add_word_vertical(grid, word, row, col):
    for i, letter in enumerate(word):
        grid[row + i][col] = letter

def add_word(grid, word):
    size = len(grid)
    orientation = random.choice(['horizontal', 'vertical'])
    if orientation == 'horizontal':
        max_col = size - len(word)
        row = random.randint(0, size - 1)
        col = random.randint(0, max_col)
        add_word_horizontal(grid, word, row, col)
    else:
        max_row = size - len(word)
        row = random.randint(0, max_row)
        col = random.randint(0, size - 1)
        add_word_vertical(grid, word, row, col)

def display_grid(grid):
    for row in grid:
        print(' '.join(row))

def generate_crossword(words, size):
    grid = generate_grid(size)
    for word in words:
        add_word(grid, word)
    return grid

if __name__ == "__main__":
    # Example usage
    word_list = ["PYTHON", "CROSSWORD", "PUZZLE", "GENERATOR", "GRID", "WORD"]
    puzzle_size = 10
    puzzle = generate_crossword(word_list, puzzle_size)
    display_grid(puzzle)

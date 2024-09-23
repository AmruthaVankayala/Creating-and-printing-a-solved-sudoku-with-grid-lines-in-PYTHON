def print_dynamic_sudoku(grid, sub_grid_size):
    """
    Prints a dynamic Sudoku grid with clear sub-grid lines based on the given sub-grid size.

    Args:
    grid (list of lists): A Sudoku grid to be printed.
    sub_grid_size (int): Size of the sub-grid (e.g., 3 for a 9x9 grid, 4 for a 16x16 grid).
    """
    n = sub_grid_size * sub_grid_size  # Total grid size
    
    for i in range(n):
        # Print horizontal border every 'sub_grid_size' rows
        if i % sub_grid_size == 0 and i != 0:
            print("-" * (n * 2 + sub_grid_size - 1))
        
        for j in range(n):
            # Print vertical border every 'sub_grid_size' columns
            if j % sub_grid_size == 0 and j != 0:
                print("|", end=" ")
            
            # Print the current cell; use "." for empty cells (0s)
            if j == n - 1:
                print(grid[i][j] if grid[i][j] != 0 else ".")
            else:
                print(f"{grid[i][j] if grid[i][j] != 0 else '.'}", end=" ")

def is_valid(grid, row, col, num, sub_grid_size):
    """
    Checks whether it is valid to place a number in the specified cell of the grid.

    Args:
    grid (list of lists): The Sudoku grid.
    row (int): Row index.
    col (int): Column index.
    num (int): Number to place.
    sub_grid_size (int): Size of the sub-grid.

    Returns:
    bool: True if valid, False otherwise.
    """
    n = sub_grid_size * sub_grid_size
    
    # Check row and column
    for i in range(n):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    # Check sub-grid
    start_row = (row // sub_grid_size) * sub_grid_size
    start_col = (col // sub_grid_size) * sub_grid_size
    
    for i in range(sub_grid_size):
        for j in range(sub_grid_size):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(grid, sub_grid_size):
    """
    Solves the Sudoku grid using backtracking.

    Args:
    grid (list of lists): The Sudoku grid to solve.
    sub_grid_size (int): Size of the sub-grid.

    Returns:
    bool: True if a solution is found, False otherwise.
    """
    n = sub_grid_size * sub_grid_size
    
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:  # Find empty cell
                for num in range(1, n + 1):
                    if is_valid(grid, row, col, num, sub_grid_size):
                        grid[row][col] = num
                        if solve_sudoku(grid, sub_grid_size):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Function to create an empty dynamic Sudoku grid
def create_empty_sudoku(sub_grid_size):
    """
    Creates an empty Sudoku grid of size (sub_grid_size * sub_grid_size) x (sub_grid_size * sub_grid_size).

    Args:
    sub_grid_size (int): Size of the sub-grid (e.g., 3 for a 9x9 grid).

    Returns:
    list of lists: A dynamic Sudoku grid with all zeros (empty cells).
    """
    n = sub_grid_size * sub_grid_size
    return [[0 for _ in range(n)] for _ in range(n)]


sub_grid_size = 3  # Change this value to create different Sudoku sizes
sudoku_grid = create_empty_sudoku(sub_grid_size)


sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the initial Sudoku grid
print("Initial Sudoku Grid:")
print_dynamic_sudoku(sudoku_grid, sub_grid_size)

# Solve the Sudoku
if solve_sudoku(sudoku_grid, sub_grid_size):
    print("\nSolved Sudoku Grid:")
    print_dynamic_sudoku(sudoku_grid, sub_grid_size)
else:
    print("\nNo solution exists.")

import random 
grid = [
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

def initial_sudoku(grids) : 
    for row in grids : 
        print("   ".join(str(num) for num in row ) ) 
        print("")
        if row == grids[2] or row == grids[5]: 
            print("----------------------------------")




# def is_valid(grid):
    
#     # Check rows
#     for row in grid:
#         if len(set(row)) != len(row):  # Check if all elements are unique in the row
#             return False
    
#     # Check columns
#     for col in range(9):
#         column = [grid[row][col] for row in range(9)]
#         if len(set(column)) != len(column):  # Check if all elements are unique in the column
#             return False
    
    
#     for r in range(0, 9, 3):
#         for c in range(0, 9, 3):
#             subgrid = [grid[r + i][c + j] for i in range(3) for j in range(3)]
#             if len(set(subgrid)) != len(subgrid):  # Check if all elements are unique in the subgrid
#                 return False

#     return True

# def generate_sudoku(grid):
  
#     numbers = list(range(1, 10))
    
#     for r in range(9):
#         random.shuffle(numbers)  # Shuffle numbers to fill the row
#         for c in range(9):
#             grid[r][c] = numbers[c]
    
#     return grid


def generate_neighbors(grid):
    neighbors = []
    # for row  in range(len(grid)) :  # Generate 10 neighbors for exploration
        # for col in range(len(grid))   : 
    neighbor = [value[:] for value in grid ]
                  
            # neighbor = [row[:] for row in grid]  # Make a copy of the grid
            # Randomly choose two positions in the grid and swap their values
    r1, c1 = random.randint(1, 9), random.randint(1, 9)
    r2, c2 = random.randint(1, 10), random.randint(1 ,9)
    neighbor[r1][c1], neighbor[r2][c2] = neighbor[r2][c2], neighbor[r1][c1]
    neighbors.append(neighbor)
    return neighbors


# def score(grid):
#     return sum([1 for row in grid for num in row if num == 0])


# def tabu_search(grid, max_iterations=1000):
#     # Tabu Search parameters
#     tabu_list = []
#     best_solution = grid
#     best_score = score(grid)
    
#     # Main Tabu Search Loop
#     for iteration in range(max_iterations):
#         neighbors = generate_neighbors(best_solution)
#         best_neighbor = None
#         best_neighbor_score = float('inf')
        
#         # Evaluate neighbors
#         for neighbor in neighbors:
#             if neighbor not in tabu_list:
#                 neighbor_score = score(neighbor)
#                 if neighbor_score < best_neighbor_score:
#                     best_neighbor_score = neighbor_score
#                     best_neighbor = neighbor
        
#         # Update best solution
#         if best_neighbor_score < best_score:
#             best_solution = best_neighbor
#             best_score = best_neighbor_score
        
#         # Update Tabu list
#         tabu_list.append(best_solution)
#         if len(tabu_list) > 10:  # Tabu list size
#             tabu_list.pop(0)
        
#         if is_valid(best_solution):
#             break
    
#     return best_solution


print("===============origin grid =========")
initial_sudoku(grid)

print("======== generate neighbors =========")
gridG = generate_neighbors(grid)
# solution = tabu_search(grid)

print(gridG)


"""
Exercise: Implement Tabu Search to Optimize a 9-Row Grid with Iteration Display

Problem Statement:
You are tasked with optimizing a 9-row grid of integers, where each row contains 9 random integers between 1 and 9. 
The goal is to ensure that each row contains unique values (no duplicates within a row). 
You will use the Tabu Search algorithm to iteratively improve the grid.

Steps to Follow:
                    1. Initialize the grid with 9 rows
                    2. Generate neighbor solutions by replacing duplicates in a row
                    3. Implement Tabu Search to find a unique row solution
                    4. Display each iteration with the best fitness (number of duplicates)
                    5. Apply Tabu Search to each row separately
                    6. Run the algorithm for a 9-row grid
"""

import random

def initial_grid(rows=9):
    return [[random.randint(1, 9) for _ in range(9)] for _ in range(rows)]

def count_duplicates(row):
    
    return len(row) - len(set(row))

def generate_neighbors(row):
    neighbors = []
    for i in range(len(row)):
        for new_value in range(1, 10):
            if new_value != row[i] and new_value not in row:
                neighbor = row[:]
                neighbor[i] = new_value
                neighbors.append(neighbor)
    return neighbors

def tabu_search(row, max_iterations=100, tabu_size=5):
    tabu_list = []
    best_solution = row[:]
    best_duplicates = count_duplicates(best_solution)

    for iteration in range(max_iterations):
        # Print iteration and best fitness in the same line
        print(f'\rIteration: {iteration:06} ' , end='', flush=True)

        if best_duplicates == 0:
            print()  
            return best_solution

        neighbors = generate_neighbors(best_solution)
        neighbors = [n for n in neighbors if tuple(n) not in tabu_list]

        if not neighbors:
            tabu_list = []
            continue

        # Pick the neighbor with the fewest duplicates
        
        best_neighbor = min(neighbors, key=lambda x: count_duplicates(x))
        best_neighbor_duplicates = count_duplicates(best_neighbor)

        # Update the best solution if the neighbor is better
        
        if best_neighbor_duplicates < best_duplicates:
            best_solution = best_neighbor
            best_duplicates = best_neighbor_duplicates

    
    
        tabu_list.append(tuple(best_solution))

        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    print("\nMaximum iterations reached. Returning best solution found.")
    return best_solution

def optimize_grid(grid):
    optimized_grid = []
    for i, row in enumerate(grid):
        print(f"\nOptimizing Row {i + 1}:")
        optimized_row = tabu_search(row)
        optimized_grid.append(optimized_row)
    return optimized_grid

# Run the algorithm
grid = initial_grid(rows=9)
print("\n ------   Initial Grid  : ------------")
for row in grid:
    print(row)

optimized_grid = optimize_grid(grid)
print("\n\n ------   Optimized Grid : ------------")
for row in optimized_grid:
    print(row)
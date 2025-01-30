"""
Exercise: Implement Tabu Search to Optimize an N-Row Grid

Problem Statement:
You are tasked with optimizing an 3-row grid of integers, where each row contains 9 random integers between 1 and 9. 
The goal is to ensure that each row contains unique values (no duplicates within a row). 
You will use the Tabu Search algorithm to iteratively improve the grid.

Steps to Follow:
                1. Initialize the grid with N rows
                2. Generate neighbor solutions by replacing duplicates in a row
                3. Implement Tabu Search to find a unique row solution
                4. Apply Tabu Search to each row separately
                5. Run the algorithm for a 3-row grid
"""

import random

def initial_grid(rows=3):
    return [[random.randint(1, 9) for _ in range(9)] for _ in range(rows)]

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
    
    for _ in range(max_iterations):
        if len(set(best_solution)) == len(best_solution):
            return best_solution

        neighbors = generate_neighbors(best_solution)
        neighbors = [n for n in neighbors if tuple(n) not in tabu_list]

        if not neighbors:
            continue

        best_solution = random.choice(neighbors)
        tabu_list.append(tuple(best_solution))

        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution

def optimize_grid(grid):
    return [tabu_search(row) for row in grid]

grid = initial_grid(rows=3)
print("Initial Grid:")
for row in grid:
    print(row)

optimized_grid = optimize_grid(grid)
print("\nOptimized Grid:")
for row in optimized_grid:
    print(row)
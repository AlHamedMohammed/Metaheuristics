"""
Exercise: Implement Tabu Search to Solve a 9x9 Grid Puzzle

Problem Statement:
You are tasked with solving a 9x9 grid puzzle where:
- Each row must contain unique integers from 1 to 9.
- Each column must also contain unique integers from 1 to 9.

Steps to Follow:
                1. Initialize the grid with no duplicates in rows
                2. Check if a grid is valid (no duplicates in rows or columns)
                3. Generate neighbor solutions by swapping two values in a row
                4. Implement Tabu Search to find a valid grid solution
                5. Apply Tabu Search to the grid
                6. Check if the optimized grid is valid
"""


import random
import numpy as np

def initial_grid(rows=9, cols=9):
    grid = []
    for _ in range(rows):
        row = random.sample(range(1, cols + 1), cols)  
        grid.append(row)
    return grid

def is_valid(grid):
    
    for row in grid:
        if len(set(row)) != len(row):
            return False
    
    for col in zip(*grid):
        if len(set(col)) != len(col):
            return False
    return True

def count_column_duplicates(grid):
    duplicate_count = 0
    for col in zip(*grid):
        duplicate_count += len(col) - len(set(col))
    return duplicate_count

def generate_neighbors(grid):
    neighbors = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(j + 1, len(grid[i])):
                neighbor = [row[:] for row in grid] 
                neighbor[i][j], neighbor[i][k] = neighbor[i][k], neighbor[i][j]  
                neighbors.append(neighbor)
    return neighbors

    return best_solution 

def tabu_search(grid, max_iterations=100000, tabu_size=50, restart_after=1000):
    tabu_list = []  
    best_solution = [row[:] for row in grid] 
    best_duplicates = count_column_duplicates(best_solution)
    no_improvement_count = 0

    for iteration in range(max_iterations):
        print(f'\rIteration: {iteration:06} | Best Fitness: {best_duplicates:03}', end='')

        if is_valid(best_solution):
            print("\nFound valid solution!")
            return best_solution  

        neighbors = generate_neighbors(best_solution)

        valid_neighbors = []
        for neighbor in neighbors:
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in tabu_list:
                valid_neighbors.append(neighbor)

        if not valid_neighbors:
            print("\nNo valid neighbors found. Resetting Tabu list...")
            tabu_list = [] 
            continue 

        best_neighbor = min(valid_neighbors, key=lambda x: count_column_duplicates(x))
        best_neighbor_duplicates = count_column_duplicates(best_neighbor)

        if best_neighbor_duplicates < best_duplicates:
            best_solution = [row[:] for row in best_neighbor]
            best_duplicates = best_neighbor_duplicates
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        tabu_list.append(tuple(tuple(row) for row in best_neighbor))

        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        if no_improvement_count >= restart_after:
            print("\nRestarting search due to no improvement...")
            best_solution = initial_grid()
            best_duplicates = count_column_duplicates(best_solution)
            tabu_list = []
            no_improvement_count = 0

    print("\nMaximum iterations reached. Returning best solution found.")
    return best_solution 


def print_grid(grid):
    print("\n======= Optimized Grid =======")
    for row in grid:
        print(" ".join(f"{x:2}" for x in row))
    print()

# Run the algorithm
grid = initial_grid()
print("Initial Grid (no duplicates in rows):")
print_grid(grid)

optimized_grid = tabu_search(grid)
if is_valid(optimized_grid) : 
    print("\n------- Valid Solution: ---------")
    print_grid(optimized_grid)
    
else : 
    print("not find a Solution repate other time ! ")
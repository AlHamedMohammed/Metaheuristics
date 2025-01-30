"""""
Exercise: Implement Tabu Search to Find a Unique Sequence
Problem Statement
You are tasked with finding a sequence of 9 unique integers,where each integer is between 1 and 9 (inclusive). 
The sequence should not contain any duplicate values. 
To achieve this, you will implement the Tabu Search algorithm, a metaheuristic optimization technique.

"""

import random

def initial_row():
    return [random.randint(1, 9) for _ in range(9)]  

def generate_neighbors(grid):
    neighbors = []
    for i in range(len(grid)):
        for new_value in range(1, 10): 
            if new_value != grid[i] and new_value not in grid:  
                neighbor = grid[:]
                neighbor[i] = new_value
                neighbors.append(neighbor)
    return neighbors

# 3. Tabu Search function to find a unique solution

def tabu_search(grid, max_iterations=100, tabu_size=5):
    tabu_list = [] 
    best_solution = grid[:]
    
    for _ in range(max_iterations):
        if len(set(best_solution)) == len(best_solution):  # I
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



grid = initial_row()
print("Initial Grid:", grid)

optimized_grid = tabu_search(grid)
print("Optimized Grid:", optimized_grid)

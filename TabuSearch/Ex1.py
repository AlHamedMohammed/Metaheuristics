""" 
Exercise: Minimize a Simple Mathematical Function
I want to minimize the following function using Tabu Search:


f(x) = x^2 + 4 x + 5

The goal is to find the value of 𝑥 that minimizes 𝑓 ( 𝑥 )
The search space for 𝑥 will be limited to integers between  [ - 10 , 10 ]

"""



def f(x):
    """Objective function to minimize."""
    functionX = x **2 + 4 * x + 5 
    
    return functionX 

def generate_neighbors(x, search_space):
    """Generate neighbors for the current value of x."""
    neighbors = []
    if x - 1 >= search_space[0]:
        neighbors.append(x - 1)
    if x + 1 <= search_space[1]:
    
        neighbors.append(x + 1)

    return neighbors

def tabu_search(initial_x, search_space, max_iterations, tabu_size):
    current_x = initial_x
    best_x = initial_x
    tabu_list = []

    for iteration in range(max_iterations):
        # Generate neighbors
        neighbors = generate_neighbors(current_x, search_space)

        # Find the best neighbor not in the tabu list
        best_candidate = None
        for neighbor in neighbors:
            if neighbor not in tabu_list:
                if best_candidate is None or f(neighbor) < f(best_candidate):
                    best_candidate = neighbor

        # Update current x
        current_x = best_candidate

        # Update the tabu list
        tabu_list.append(current_x)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        # Update the best solution
        if f(current_x) < f(best_x):
            best_x = current_x

        print(f"Iteration {iteration + 1}: x = {current_x}, f(x) = {f(current_x)}")

    return best_x, f(best_x)

# Problem setup
search_space = (-10, 10)  # Search space for x
initial_x = 2             # Starting point
max_iterations = 10       # Number of iterations
tabu_size = 3             # Tabu list size

# Run Tabu Search
best_x, best_value = tabu_search(initial_x, search_space, max_iterations, tabu_size)

print("\nFinal Result:")
print(f"Best x: {best_x}")
print(f"Minimum f(x): {best_value}")

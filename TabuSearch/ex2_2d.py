""" 
Exercise: Minimize a Simple Mathematical Function
I want to minimize the following function using Tabu Search:


f(x , y ) = x^2 + y^2 - 4x - 6* y +6 

The goal is to find the value of 𝑥 , y that minimizes 𝑓 ( x, y  )
The search space for x , y  will be limited to integers between  [ - 100 , 100 ]

"""


def f(x, y): 
    fun_XY = x**2 + y**2 - 4*x - 6*y + 5 
    return fun_XY

def generate_neighbors(x, y, space_search): 
    neighbors = []
    if x - 1 >= space_search[0]: 
        neighbors.append((x - 1, y)) 
    if x + 1 <= space_search[1]: 
        neighbors.append((x + 1, y)) 
    
    if y - 1 >= space_search[0]: 
        neighbors.append((x, y - 1))
    if y + 1 <= space_search[1]: 
        neighbors.append((x, y + 1))
    
    return neighbors

def tabu_search(x, y, search_space, max_iteration, tabu_size):
    current_point = (x, y)
    best_point = current_point 
    tabu_list = [] 

    for iteration in range(max_iteration):  # Fixed range here
        neighbor = generate_neighbors(current_point[0], current_point[1], search_space)  # Fixed reference
        
        best_candidate = None 
        for neighbors in neighbor: 
            if neighbors not in tabu_list: 
                if best_candidate is None or f(neighbors[0], neighbors[1]) < f(best_candidate[0], best_candidate[1]):  # Fixed comparison
                    best_candidate = neighbors 
        
        current_point = best_candidate 
        tabu_list.append(current_point)
        
        if len(tabu_list) > tabu_size: 
            tabu_list.pop(0)
        
        if f(current_point[0], current_point[1]) < f(best_point[0], best_point[1]): 
            best_point = current_point 
        
        print(f" iteration {iteration + 1} x = {current_point[0]} , y = {current_point[1]}  => f(x,y) = {f(current_point[0], current_point[1])}")  
        
    return best_point , f(best_point[0] , best_point[1])


best_point , best_value = tabu_search(5, 4, (-100, 100), 10, 3)

print(f"best point ( {best_point[0]} , {best_point[1] } ) : f(x,y) = {best_value }")
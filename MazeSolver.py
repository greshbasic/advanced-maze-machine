import heapq
import os
from time import sleep, time

start = 0
end = 0

def solve_maze(maze, option):
    if option == 1:
        maze.algo = "BFS"
        bfs(maze)
        
    if option == 2:
        maze.algo = "DFS"
        dfs(maze)
        
    if option == 3:
        maze.algo = "GBFS"
        greedy(maze)
        
    end = time()
    clear_terminal()
    maze.print_maze()
    print("Time taken: {:.2f} seconds".format(end - start))
    maze.time = "{:.2f}".format(end-start)
            
def bfs(maze):
    global start
    start = time()
    
    maze.print_maze()
    frontier_queue = []
    current = [maze.start_row, 0]
    frontier_queue.append(current)
    
    while frontier_queue:
        clear_terminal()
        maze.print_maze()
        sleep(0.1)
        current = frontier_queue.pop(0)
        current_row = current[0]
        current_col = current[1]
        maze.maze[current_row][current_col].visited = True
        
        if current_row == maze.end_row and current_col == maze.cols - 1:
            break
        
        visitable = visit_options(maze, current_row, current_col)
        for cell in visitable:
            frontier_queue.append(cell)
    
def dfs(maze):
    global start
    start = time()
    
    frontier_stack = []
    current = [maze.start_row, 0]
    frontier_stack.append(current)
    
    while frontier_stack:
        clear_terminal()
        maze.print_maze()
        sleep(0.1)
        current = frontier_stack.pop()
        current_row = current[0]
        current_col = current[1]
        maze.maze[current_row][current_col].visited = True
        
        if current_row == maze.end_row and current_col == maze.cols - 1:
            break
    
        visitable = visit_options(maze, current_row, current_col)
        for cell in visitable:
            frontier_stack.append(cell)

def greedy(maze):
    global start
    start = time()
    
    maze.print_maze()
    frontier_queue = []
    current = (maze.start_row, 0)
    heapq.heappush(frontier_queue, (0, current))
    
    while frontier_queue:
        clear_terminal()
        maze.print_maze()
        sleep(0.1)
        _, current = heapq.heappop(frontier_queue)
        current_row, current_col = current
        maze.maze[current_row][current_col].visited = True
        
        if current_row == maze.end_row and current_col == maze.cols - 1:
            break
        
        visitable = visit_options(maze, current_row, current_col)
        heur_dict = {}
        goal_state = (maze.end_row, maze.cols - 1)
        for i, cell in enumerate(visitable):
            curr_heur = h(cell, goal_state)
            heur_dict[cell] = curr_heur
            
        for cell in visitable:
            max_heur_cell = max(heur_dict, key=heur_dict.get)
            priority = -heur_dict.pop(max_heur_cell) 
            heapq.heappush(frontier_queue, (priority, max_heur_cell))
    
def visit_options(maze, current_row, current_col):
    visitable = []
    
    if current_col - 1 >= 0 and current_col < maze.cols and not maze.maze[current_row][current_col - 1].visited and not maze.maze[current_row][current_col - 1].right:
        left_cell = (current_row, current_col - 1)
        visitable.append(left_cell)
    
    if current_col >= 0 and current_col + 1 < maze.cols and not maze.maze[current_row][current_col + 1].visited and not maze.maze[current_row][current_col].right:
        right_cell = (current_row, current_col + 1)
        visitable.append(right_cell)
        
    if current_row - 1 >= 0 and current_row < maze.rows and not maze.maze[current_row - 1][current_col].visited and not maze.maze[current_row - 1][current_col].bottom:
        up_cell = (current_row - 1, current_col)
        visitable.append(up_cell)
        
    if current_row >= 0 and current_row + 1 < maze.rows and not maze.maze[current_row + 1][current_col].visited and not maze.maze[current_row][current_col].bottom:
        down_cell = (current_row + 1, current_col)
        visitable.append(down_cell)

    return visitable

def h(curr_state, goal_state):
    # Manhattan Distance based heuristic function
    heur = abs(goal_state[1] - curr_state[1]) + abs(goal_state[0] - curr_state[0])
    print(f"h: {heur}")
    return heur * -1

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

from Maze import Maze
from MazeMaker import make_maze
import heapq
import os
from time import sleep, time
from MazeMaker import compare_mazes

def solve_maze(maze, option):
    if option == 1:
        maze.algo = "BFS"
        bfs(maze)
        
    if option == 2:
        maze.algo = "DFS"
        dfs(maze)
        
    if option == 3:
        maze.algo = "BDS"
        bidir(maze)
        
    if option == 4:
        maze.algo = "GBFS"
        greedy(maze)
        
    if option == 5:
        maze.algo = "A*"
        Astar(maze)
        
    if option == 6:
        ffa_mazes = []

        # BFS
        breadth = make_maze(7, 15)
        breadth.algo = "BFS"
        ffa_mazes.append(breadth)
        bfs(breadth)
        
        # DFS
        depth = make_maze(7, 15)
        depth.algo = "DFS"
        ffa_mazes.append(depth)
        dfs(depth)
        
        #Bidirectional
        bds = make_maze(7, 15)
        bds.algo = "BDS"
        ffa_mazes.append(bds)
        bidir(bds)
        
        #Greedy best first
        greed = make_maze(7, 15)
        greed.algo = "GBFS"
        ffa_mazes.append(greed)
        greedy(greed)
        
        #A*
        astar = make_maze(7, 15)
        astar.algo = "A*"
        ffa_mazes.append(astar)
        Astar(astar)
        
        clear_terminal()
        compare_mazes(ffa_mazes)
        
def bfs(maze):
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
            
    end = time()
    clear_terminal()
    maze.print_maze()
    print("Time taken: {:.2f} seconds".format(end - start))
    maze.time = "{:.2f}".format(end-start)
      
def dfs(maze):
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
        
    end = time()
    clear_terminal()
    maze.print_maze()
    print("Time taken: {:.2f} seconds".format(end - start))
    maze.time = "{:.2f}".format(end-start)

def bidir(maze):
    start = time()
    
    # Initialize the start and goal frontier queues
    start_frontier = [(maze.start_row, 0)]
    goal_frontier = [(maze.end_row, maze.cols - 1)]
    
    # Initialize visited sets for start and goal
    start_visited = set()
    goal_visited = set()
    
    # Mark start and goal nodes as visited
    start_visited.add((maze.start_row, 0))
    goal_visited.add((maze.end_row, maze.cols - 1))
    
    while start_frontier and goal_frontier:
        clear_terminal()
        maze.print_maze()
        sleep(0.1)
        
        # Explore from the start node
        current_start = start_frontier.pop(0)
        start_row, start_col = current_start
        maze.maze[start_row][start_col].visited = True
        if current_start in goal_visited:
            break
        for neighbor in visit_options(maze, start_row, start_col):
            if neighbor not in start_visited:
                start_visited.add(neighbor)
                start_frontier.append(neighbor)
        
        # Explore from the goal node
        current_goal = goal_frontier.pop(0)
        goal_row, goal_col = current_goal
        maze.maze[goal_row][goal_col].visited = True
        if current_goal in start_visited:
            break
        for neighbor in visit_options(maze, goal_row, goal_col):
            if neighbor not in goal_visited:
                goal_visited.add(neighbor)
                goal_frontier.append(neighbor)
    
    end = time()
    clear_terminal()
    maze.print_maze()
    print("Time taken: {:.2f} seconds".format(end - start))
    maze.time = "{:.2f}".format(end - start)
      
def greedy(maze):
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
            
    end = time()
    clear_terminal()
    maze.print_maze()
    print("Time taken: {:.2f} seconds".format(end - start))
    maze.time = "{:.2f}".format(end - start)
    
def Astar(maze):
    start = time()
    
    maze.print_maze()
    frontier_queue = []
    current = (maze.start_row, 0)
    g_score = 0  # initial cost is 0
    goal_state = (maze.end_row, maze.cols - 1)
    heapq.heappush(frontier_queue, (g_score + h(current, goal_state), g_score, current))
    
    while frontier_queue:
        clear_terminal()
        maze.print_maze()
        sleep(0.1)
        _, g_score, current = heapq.heappop(frontier_queue)
        current_row, current_col = current
        maze.maze[current_row][current_col].visited = True
        
        if current_row == maze.end_row and current_col == maze.cols - 1:
            break
        
        visitable = visit_options(maze, current_row, current_col)
        for next_cell in visitable:
            next_row, next_col = next_cell
            tentative_g_score = g_score + 1  # each move has same cost
            priority = tentative_g_score + h(next_cell, goal_state)
            heapq.heappush(frontier_queue, (priority, tentative_g_score, next_cell))
            
    end = time()
    clear_terminal()
    maze.print_maze()
    print("Time taken: {:.2f} seconds".format(end - start))
    maze.time = "{:.2f}".format(end - start)
   
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

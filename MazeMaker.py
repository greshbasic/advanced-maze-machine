from Maze import Maze
from random import randint as r
from random import choice as c
import os

def make_maze(row=None, col=None):
    if not r:
        rows = int(input("Please enter an amount of rows: "))
    else:
        rows = row
    if not c:
        columns = int(input("Please enter an amount of columns: "))
    else:
        columns = col
    start = r(0, rows-1)
    end = r(0, rows-1)
    
    maze = Maze(rows, columns, start, end)
    
    stack = []
    current_top = [maze.start_row, 0]
    maze.visited = True
    stack.append(current_top)
    
    while len(stack) > 0:
        current_top = stack[-1]
        current_row = current_top[0]
        current_col = current_top[1]
        
        visitable = maze.visitable(current_top)
        if not visitable:
            stack.pop()
        else:
            random_choice = c(visitable)
            if random_choice == "L":
                left_cell = [current_row, current_col - 1]
                stack.append(left_cell)
                maze.maze[left_cell[0]][left_cell[1]].visited = True
                maze.maze[left_cell[0]][left_cell[1]].right = False
                
            if random_choice == "R":
                right_cell = [current_row, current_col + 1]
                stack.append(right_cell)
                maze.maze[right_cell[0]][right_cell[1]].visited = True
                maze.maze[current_row][current_col].right = False
                
            if random_choice == "D":
                down_cell = [current_row + 1, current_col]
                stack.append(down_cell)
                maze.maze[down_cell[0]][down_cell[1]].visited = True
                maze.maze[current_row][current_col].bottom = False
                
            if random_choice == "U":
                up_cell = [current_row - 1, current_col]
                stack.append(up_cell)
                maze.maze[up_cell[0]][up_cell[1]].visited = True
                maze.maze[up_cell[0]][up_cell[1]].bottom = False
    
    for i in range(rows):
        for j in range(columns):
            maze.maze[i][j].visited = False
        
    return maze

def compare_mazes(mazes):
    sorted_maze_list = sorted(mazes, key=lambda maze: float(maze.time)/(maze.rows * maze.cols))
    print("\n")
    
    for i, maze in enumerate(sorted_maze_list):
        if not maze.title:
            maze.title = maze.algo
            
        area = maze.rows * maze.cols
        time = float(maze.time)
        time_per_area = time/area
        time_per_area_string = "{:.2f}".format(time_per_area)
        print(f"{i+1}. {maze.title} ({maze.algo}): Took {maze.time} seconds to solve a {maze.rows}x{maze.cols} maze [{time_per_area_string} seconds per cell]")
    
    print("\n\nPlease make a selection")
    print("+-----------------------------+")
    print("| 1: Make new maze            |")
    print("| 2: Quit                     |")
    print("+-----------------------------+")
    option = int(input("Your selection: "))
    
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    
    if option == 1:
        return True

    return False

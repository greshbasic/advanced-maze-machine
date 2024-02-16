from MazeMaker import make_maze
from MazeMaker import compare_mazes
from MazeSolver import solve_maze
from MazeSolver import clear_terminal

if __name__ == "__main__":
    cont = True
    mazes = []
    
    while cont:
        
        clear_terminal()
        
        print("Please make a selection")
        print("+-----------------------------+")
        print("| 1: Breadth-First Search     |")
        print("| 2: Depth-First Search       |")
        print("| 3: Bidirectional Search     |")
        print("| 4: Greedy Best-First Search |")
        print("| 5: A* Search                |")
        print("| 6: Free-For-All             |")
        print("+-----------------------------+")
        option1 = int(input("Your selection: "))
        
        if option1 != 6:
            my_maze = make_maze()
            solve_maze(my_maze, option1)
        else:
            solve_maze(None, 6)

        
        if option1 == 6:
            exit()
        
        print("\n\nPlease make a selection")
        print("+-----------------------------+")
        print("| 1: Save maze results        |")
        print("| 2: Don't save maze results  |")
        print("+-----------------------------+")
        option2 = int(input("Your selection: "))
        
        clear_terminal()
 
        if option2 == 1:
            my_maze.title = input("Please give the maze a title: ")
            mazes.append(my_maze)
    
        print("\n\nPlease make a selection")
        print("+-----------------------------+")
        print("| 1: Make new maze            |")
        print("| 2: Compare maze results     |")
        print("| 3: Quit                     |")
        print("+-----------------------------+")
        option3 = int(input("Your selection: "))
        
        clear_terminal()
        
        if option3 == 3:
            cont = False
            
        if option3 == 2:
            cont = compare_mazes(mazes)
            clear_terminal()
            
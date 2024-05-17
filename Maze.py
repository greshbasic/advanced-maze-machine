from MazeCell import MazeCell

class Maze:
    def __init__(self, rows, cols, start_row, end_row):
        self.rows = rows
        self.cols = cols
        self.start_row = start_row
        self.end_row = end_row
        self.time = ""
        self.algo = ""
        self.title = None
        
        self.maze = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.maze[i][j] = MazeCell()
                  
    def make_cols_string(self):
        
        cols_string = "|"
        
        for i in range(self.cols):
            cols_string += "---|"
            
        return cols_string
    
    def make_rows_string(self, row_num):
        rows = ["", "|"]
        
        # leaving the starting cell's left wall open
        if row_num != self.start_row:
            rows[0] += "| "
        else:
            rows[0] += "  "

        # looping through and adding *'s and walls to respective arrays
        for i in range(self.cols):
            if self.maze[row_num][i].visited:
                rows[0] += "* "
            else:
                rows[0] += "  "

            if self.maze[row_num][i].right:
                if row_num == self.end_row and i == self.cols - 1:
                    pass
                else:
                    rows[0] += "| "
            else:
                rows[0] += "  "

            if self.maze[row_num][i].bottom:
                rows[1] += "---|"
            else:
                rows[1] += "   |"

            if row_num == self.rows - 1:
                temp = "|"
                for i in range(self.cols):
                    temp += "---|"
                rows[1] = temp

        return rows
      
    def print_maze(self):
        cols_string = self.make_cols_string()
        print(cols_string)
        
        for i in range(self.rows):
            row_pair = self.make_rows_string(i)
            print(f"{row_pair[0]}\n{row_pair[1]}")
            
    def visitable(self, coords):
        current_row = coords[0]
        current_col = coords[1]
        
        possible_moves = []
        
        if current_col - 1 >= 0 and current_col < self.cols and not self.maze[current_row][current_col - 1].visited:
            possible_moves.append("L")
        
        if current_col >= 0 and current_col + 1 < self.cols and not self.maze[current_row][current_col + 1].visited:
            possible_moves.append("R")
            
        if current_row - 1 >= 0 and current_row < self.rows and not self.maze[current_row - 1][current_col].visited:
            possible_moves.append("U")
            
        if current_row >= 0 and current_row + 1 < self.rows and not self.maze[current_row + 1][current_col].visited:
            possible_moves.append("D")
            
        if not len(possible_moves):
            return None
        
        return possible_moves

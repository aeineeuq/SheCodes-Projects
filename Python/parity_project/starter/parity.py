import csv
# parity is a method of error detection 

def load_grid(csv_file_path):
    """Loads data from a csv file.
    Args:
        csv_file_path: string representing the path to a csv file.
    Returns:
        A list of lists, where each sublist is a line in the csv file.
    """
    listoflists =[]
    with open(csv_file_path, mode="r", encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            listoflists.append(line)
    # print(load_grid_list)
    # return csv_file_path
    return listoflists 

def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.
    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    Returns:
        The same grid, with a new column added.
    """
    for row in grid: # Loop through rows
        xcount = 0    # start counter
        for char in row:
            if char == 'X': # Count X in a row
                xcount += 1 
        if xcount % 2 == 0: # if even (divisible by 2)
            row.append('O') # add O to end of row
        else:               # if not even then set X
            row.append('X') # add X to end of row
    return grid

def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.
    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    Returns:
        The same grid, with a new row added.
    """
    new_row = []                        # define variable to store values
    if grid == []:
        return grid                     # check if grid is a list of lists

    else:
        for i in range(len(grid[0])):   # loop through chars/items in list
            xcount = 0                  # start counter
            for row in grid:
                if row[i] == "X":       # if X, add to counter
                    xcount += 1
            if xcount % 2 == 0:         # if even (divisible by 2)
                new_row.append('O')     # add O to new row
            else:                       # if not divisible by 2
                new_row.append('X')     # add X to new row
    
        grid.append(new_row)            # add new row to grid

    return grid

def flip_cell(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).
    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = x: 0, y: 0
            b = x: 1, y: 0
            c = x: 0, y: 1
            d = x: 1, y: 1
    Returns:
        The same grid, with a cell switched.
    """
    if grid == []:              # check if grid is a list of lists
        return grid
    else:
        if grid[y_pos][x_pos] == 'X':   # takes input from user search grid, checks if X
            grid[y_pos][x_pos] = 'O'    # if X, swap to O
        else:
            grid[y_pos][x_pos] = 'X'    # else it is O. swap to X
    return (grid)                       # return grid with cell switch

def find_flipped_cell(grid):
    """Determines which cell/cell in the grid was flipped.
    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    Returns:
        A list containing the coordinates of the cell with the flipped cell.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 0)
            b = (1, 0)
            c = (0, 1)
            d = (1, 1)
        If 'a' was the flipped letter, this function would return: [0, 0]
    """  
    
    charcount = 0               # define /create count variable
    x_pos = 0
    y_pos = 0
    for row in grid:
        xcount = 0      
        for char in row:
            if char == 'X':     # count number of x in a row
                xcount += 1
        if xcount % 2 == 0:     # if even go to next row
            charcount += 1
        else:
            y_pos = charcount   # if odd, record the row as the changed row

    if y_pos == 0:
        y_pos = None
    for i in range(len(grid[0])):
        xcount = 0
        for row in grid:
            if row[i] == "X":  # count number of x 
                xcount += 1
        if xcount % 2 != 0:
            x_pos = i
    if x_pos == 0:
        x_pos = None
    if charcount == len(grid[0]):
        return([None,None]) 
    else:
        # print(x_pos,y_pos)
        return([x_pos,y_pos])
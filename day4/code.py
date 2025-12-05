def count_cells(grid: list[list[bool]]) -> int:
    surrounding_coordinates = [ [-1, -1], [-1, 0], [-1, 1],
                                [0, -1],           [0, 1],
                                [1, -1],  [1, 0],  [1, 1] ]
    
    count = 0
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if (grid[i][j] == False):
                continue
            
            neighbours_count = 0
            for coordinates in surrounding_coordinates:
                if grid[i + coordinates[0]][j + coordinates[1]] == True:
                    neighbours_count += 1
            
            if neighbours_count < 4:
                count += 1
    
    return count

def remove_cells(grid: list[list[bool]]) -> int:
    surrounding_coordinates = [ [-1, -1], [-1, 0], [-1, 1],
                                [0, -1],           [0, 1],
                                [1, -1],  [1, 0],  [1, 1] ]
    
    removed_count = 0
    to_remove = []
    
    while True:
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if (grid[i][j] == False):
                    continue
                
                neighbours_count = 0
                for coordinates in surrounding_coordinates:
                    if grid[i + coordinates[0]][j + coordinates[1]] == True:
                        neighbours_count += 1
                
                if neighbours_count < 4:
                    to_remove.append([i, j])
        
        to_remove_count = len(to_remove)
        if to_remove_count == 0:
            break
        
        removed_count += to_remove_count

        for coordinates in to_remove:
            grid[coordinates[0]][coordinates[1]] = False
        
        to_remove.clear()
    
    return removed_count

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    columns = len(lines[0]) + 2

    grid = []
    grid.append([False] * columns)

    for line in lines:
        grid.append([False] + [char == '@' for char in line] + [False])
    
    grid.append([False] * columns)
    
    print(count_cells(grid))
    print(remove_cells(grid))

    file.close()

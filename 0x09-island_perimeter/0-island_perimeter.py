#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid):
    """
    Function that returns the periemeter of an island
    Args:
        grid (list[list(int)]): island
    Returns:
        perimeter (int): island periemeter
    """
    perimeter = 0

    if grid != []:
        cols = len(grid[0])
        rows = len(grid)

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                if (x - 1) == -1 or grid[x - 1][y] == 0:
                    perimeter += 1
                if (x + 1) == rows or grid[x + 1][y] == 0:
                    perimeter += 1
                if (y - 1) == -1 or grid[x][y - 1] == 0:
                    perimeter += 1
                if (y + 1) == cols or grid[x][y + 1] == 0:
                    perimeter += 1

    return perimeter

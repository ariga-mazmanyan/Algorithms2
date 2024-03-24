# -*- coding: utf-8 -*-
"""BFSgrid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H7uarmkohPu3Z-vKMOCi1s6i1Ygkkx_X
"""

def bfs(grid, start):

    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        row, col = queue.pop(0)
        print(row, col)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

bfs(grid, (0, 0))
#! /usr/bin/python3.10
import csv
from typing import List


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def handle_blocks(self, grid: List[List[List[int]]]):
        """Updates grid with number of visible sides for all cells."""

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                tree_height = grid[r][c][0]

                for other_tree_r in range(len(grid)):
                    if grid[other_tree_r][c][0] <= tree_height:
                        if r < other_tree_r:
                            grid[other_tree_r][c][1][0] = 0
                        elif r > other_tree_r:
                            grid[other_tree_r][c][1][1] = 0

                for other_tree_c in range(len(grid)):
                    if grid[r][other_tree_c][0] <= tree_height:
                        if c < other_tree_c:
                            grid[r][other_tree_c][1][2] = 0
                        elif c > other_tree_c:
                            grid[r][other_tree_c][1][3] = 0

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            grid = []
            visible_count = 0

            for row in csv_reader:
                grid.append([])
                for c in row[0]:
                    # Keep track of sides of visibility [top, bot, left, right]
                    grid[-1].append([int(c), [1, 1, 1, 1]])

            self.handle_blocks(grid)

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if sum(grid[r][c][1]) > 0:
                        visible_count += 1

            print(visible_count)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
